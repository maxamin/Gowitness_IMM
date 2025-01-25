import sqlite3
import os
import logging
import time
import math
from typing import Tuple, List

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DatabaseSplitter:
    def __init__(self, original_db: str, target_table: str = "urls", max_size_mb: int = 100):
        self.original_db = os.path.abspath(original_db)
        self.target_table = target_table
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.temp_dir = "split_temp"
        self.buffer_size = 5 * 1024 * 1024
        os.makedirs(self.temp_dir, exist_ok=True)

    def safe_delete(self, path: str) -> bool:
        """Handle file deletion with retries"""
        for _ in range(3):
            try:
                if os.path.exists(path):
                    os.remove(path)
                    return True
            except (PermissionError, OSError):
                time.sleep(0.5)
        return False

    def validate_table_exists(self):
        """Verify the target table exists and has data"""
        with sqlite3.connect(self.original_db) as conn:
            cursor = conn.cursor()
            # Check table existence
            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND LOWER(name) = LOWER(?)
            """, (self.target_table,))
            if not cursor.fetchone():
                raise ValueError(f"Table '{self.target_table}' does not exist")
            
            # Check row count
            cursor.execute(f"SELECT COUNT(*) FROM {self.target_table}")
            count = cursor.fetchone()[0]
            if count == 0:
                raise ValueError(f"Table '{self.target_table}' is empty")

    def get_table_columns(self) -> List[str]:
        """Get list of column names for the target table"""
        with sqlite3.connect(self.original_db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({self.target_table})")
            columns = [col[1] for col in cursor.fetchall() if col[1].lower() != 'rowid']
            if not columns:
                raise ValueError(f"No columns found in table '{self.target_table}'")
            return columns

    def calculate_sizes(self) -> Tuple[int, float]:
        """Calculate base size and average row size with null checks"""
        temp_db = os.path.join(self.temp_dir, "size_check.db")
        self.safe_delete(temp_db)
        
        try:
            # Create temp DB copy
            with sqlite3.connect(self.original_db) as src_conn:
                with sqlite3.connect(temp_db) as dest_conn:
                    src_conn.backup(dest_conn)
            
            # Remove target table from temp DB
            with sqlite3.connect(temp_db) as conn:
                conn.execute(f"DROP TABLE IF EXISTS {self.target_table}")
                conn.commit()
                conn.execute("VACUUM")
                base_size = os.path.getsize(temp_db)

            # Calculate row size using actual columns
            columns = self.get_table_columns()
            size_query = f"""
                SELECT COUNT(*),
                SUM({" + ".join([f"LENGTH(CAST({col} AS BLOB))" for col in columns])})
                FROM {self.target_table}
            """
            
            with sqlite3.connect(self.original_db) as conn:
                cursor = conn.cursor()
                cursor.execute(size_query)
                result = cursor.fetchone()
                
                if not result or result[0] is None or result[1] is None:
                    raise ValueError("Could not calculate row sizes")
                    
                count, total_bytes = result
                avg_size = total_bytes / count if count > 0 else 0

            return base_size, avg_size

        finally:
            self.safe_delete(temp_db)

    def execute_split(self):
        """Main splitting workflow with validation"""
        try:
            # Validate inputs
            if not os.path.exists(self.original_db):
                raise FileNotFoundError(f"Database not found: {self.original_db}")
            
            # Validate table
            self.validate_table_exists()
            
            # Calculate sizes
            base_size, avg_size = self.calculate_sizes()
            logging.info(f"Base size: {base_size/1e6:.1f}MB | Avg row: {avg_size:.1f} bytes")
            
            # Rest of the code remains the same...

        except Exception as e:
            logging.error(f"Splitting failed: {str(e)}")
            logging.error("Common solutions:")
            logging.error("- Verify the table name is spelled correctly")
            logging.error("- Check the table contains data")
            logging.error("- Ensure proper database permissions")
            raise

# Rest of the class remains unchanged...

if __name__ == "__main__":
    try:
        splitter = DatabaseSplitter(
            original_db="gowitness3.sqlite3",
            target_table="urls",
            max_size_mb=100
        )
        splitter.execute_split()
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")