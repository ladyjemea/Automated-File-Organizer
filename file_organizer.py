import os
import shutil

def organize_files(directory):
    # Define categories and their corresponding file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Others': []  # Default category for files with unknown extensions
    }

    # Create folders for each category
    for category in categories:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Determine the category of the file based on its extension
            category = 'Others'  # Default category
            for cat, extensions in categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    category = cat
                    break

            # Move the file to the corresponding category folder
            destination = os.path.join(directory, category, filename)
            shutil.move(filepath, destination)
            print(f"Moved '{filename}' to '{category}' folder.")

if __name__ == "__main__":
    # Example usage: python organize_files.py <directory_path>
    import sys
    if len(sys.argv) != 2:
        print("Usage: python organize_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: Invalid directory path.")
        sys.exit(1)

    organize_files(directory_path)





"""
Save the code to a file named organize_files.py.
Open a command-line interface.
Navigate to the directory containing the organize_files.py file.
Run the script by providing the directory path you want to organize as an argument, like this:
python organize_files.py /path/to/your/directory
Replace /path/to/your/directory with the path to the directory containing the files you want to organize.
Press Enter, and the script will organize the files within the specified directory based on their file extensions into separate folders.
"""