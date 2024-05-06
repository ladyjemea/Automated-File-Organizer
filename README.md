# Automated-File-Organizer
This command-line tool automatically organizes files within a specified directory based on their file type or other criteria. It scans the directory, categorizes files, and moves them into separate folders according to their attributes.


# Installation
Clone the repository:
git clone https://github.com/yourusername/file-organizer.git

Navigate to the project directory:
cd file-organizer

Install dependencies:
pip install -r requirements.txt


# Usage
Command-Line Interface
To use the File Organizer tool, run the following command:
python file_organizer.py [options] <directory_path>

Replace [options] with any additional arguments and <directory_path> with the path to the directory you want to organize.


# Options
-h, --help: Show the help message and exit.
-c, --criteria <criteria>: Specify the organization criteria (e.g., file extension, creation date, size).
-l, --log <log_file>: Enable logging and specify the log file path.
-v, --verbose: Enable verbose mode to display detailed information during execution.

Examples
Organize files in the directory ~/Documents based on their file extensions:
python file_organizer.py -c extension ~/Documents

Organize files in the directory ~/Downloads based on their creation date and enable logging:
python file_organizer.py -c creation_date -l ~/file_organizer.log ~/Downloads
