import os
import shutil

# Define the directory where all your folders are located
root_directory = "Y:\Шушарин И.А\ЗК\РТЗК54"

# Walk through all subdirectories and files in the root directory
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Construct the full file path
        file_path = os.path.join(root, file)

        # Move the file to the parent folder (root)
        parent_folder = os.path.dirname(root)
        shutil.move(file_path, root_directory)  # Moves the file to the root directory

# Remove any empty folders
for root, dirs, files in os.walk(root_directory, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if not os.listdir(dir_path):  # If the directory is empty
            os.rmdir(dir_path)

print("Files have been moved to their parent directory and subfolders have been removed.")
