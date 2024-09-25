import os
import shutil

# Define the directory where your files are located
directory = "Y:\Шушарин И.А\РТЗК10"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Create the full file path
    file_path = os.path.join(directory, filename)
    
    # Ensure it's a file and not a directory
    if os.path.isfile(file_path):
        # Create a new folder with the same name as the file (without the extension)
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(directory, folder_name)
        
        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Move the file into the new folder
        shutil.move(file_path, os.path.join(folder_path, filename))

print("Files have been moved to their respective folders.")
