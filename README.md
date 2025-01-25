
# Gowitness Database Collection for Immunefi Bug Bounty Programs

## Overview

This repository provides an **extensive collection of Gowitness SQLite database files** to assist bug bounty hunters working with Immunefi programs. Each database contains:
- **Screenshots** of target websites.
- **Metadata** such as HTTP response codes and error logs.
- A **structured SQLite format** for efficient querying and analysis.

These databases streamline reconnaissance and help you focus on identifying vulnerabilities.

---

## Downloadable Files

Below is the list of Gowitness database files available for download:

| **Filename**           | **Size**      | **Last Modified**          | **Description**                           | **Download**                |
|-------------------------|---------------|----------------------------|-------------------------------------------|-----------------------------|
| `gowitness1.sqlite3`    | 150 MB        | September 24, 2024         | Recon data for Program 1.                 | [Download Link](#)          |
| `gowitness2.sqlite3`    | 404 MB        | September 16, 2024         | Recon data for Program 2.                 | [Download Link](#)          |
| `gowitness3.sqlite3`    | 1.2 GB        | September 19, 2024         | Recon data for Program 3.                 | [Download Link](#)          |
| `gowitness4.sqlite3`    | 80 MB         | July 28, 2024              | Recon data for Program 4.                 | [Download Link](#)          |
| `gowitness5.sqlite3`    | 505 MB        | October 12, 2024           | Recon data for Program 5.                 | [Download Link](#)          |
| `gowitness6.sqlite3`    | 120 MB        | September 12, 2024         | Recon data for Program 6.                 | [Download Link](#)          |
| `gowitness7.sqlite3`    | 28 MB         | October 17, 2024           | Recon data for Program 7.                 | [Download Link](#)          |
| `gowitness8.sqlite3`    | 1.2 MB        | September 25, 2024         | Recon data for Program 8.                 | [Download Link](#)          |
| `gowitness9.sqlite3`    | 1.8 MB        | October 11, 2024           | Recon data for Program 9.                 | [Download Link](#)          |
| `gowitness10.sqlite3`   | 238 MB        | September 12, 2024         | Recon data for Program 10.                | [Download Link](#)          |
| `gowitness11.sqlite3`   | 52 MB         | September 19, 2024         | Recon data for Program 11.                | [Download Link](#)          |

---

## How to Use

1. **Download the Database File:**
   Click the download link for the desired database file from the table above.

2. **Inspect with SQLite Tools:**
   Open the `.sqlite3` file using any SQLite-compatible viewer, such as:
   - [DB Browser for SQLite](https://sqlitebrowser.org/)
   - Command-line tool (`sqlite3`).

3. **Query Data:**
   Example query to extract URLs and metadata:
   ```sql
   SELECT url, status_code, timestamp, screenshot_path FROM results;
   ```

4. **Access Screenshots:**
   Screenshots are stored in the database and can be exported for further analysis.

---

## Requirements

- **SQLite 3.x**: To query the `.sqlite3` database files.
- **Disk Space**: Ensure sufficient storage for large database files.
## Contributing



We welcome contributions from the community! If you'd like to contribute to this repository, please follow these guidelines:



### How to Contribute



1. **Fork the Repository**: Click the "Fork" button on the top right of this repository page to create your own copy.

2. **Clone Your Fork**: Clone your fork to your local machine.

   ```bash

   git clone https://github.com/maxamin/Gowitness_IMM.git
   Create a Branch: Before making any changes, create a new branch.
   git checkout -b feature-name
   Make Your Changes: Make the necessary changes to the database files or documentation.
   Commit Your Changes: After making your changes, commit them with a descriptive message.
   git commit -m "Description of changes"
   Push Changes: Push the changes to your fork.
   git push origin feature-name
       Submit a Pull Request: Go to the original repository and submit a pull request with your changes. Provide a clear description of what you’ve changed.

Code of Conduct

Please adhere to the following code of conduct when interacting with this project:

    Be respectful and considerate of others.
    Stay focused on the project and avoid off-topic discussions.
    Refrain from making any derogatory or harmful comments.

## Disclaimer

This repository is intended **for educational purposes only**. It is designed to provide examples and demonstrate how tools like **Gowitness** can be used in the context of bug bounty programs and web security research.

By accessing or using this repository, you agree to the following:

- **Use on your own behalf**: All content, scripts, and resources in this repository are for educational, informational, or research purposes only. It is your responsibility to ensure that you are using the content legally and ethically.
- **Compliance with Laws**: You should follow all applicable laws and regulations when using the tools and methods provided in this repository. Unauthorized access to computer systems, websites, or networks is illegal and unethical.
- **No Liability**: The repository owner and contributors are not responsible for any misuse, damage, or legal consequences resulting from the use of this repository or its content.

Please ensure that you have permission to perform security testing on any systems and that your actions are ethical and lawful.
