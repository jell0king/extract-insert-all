import os
import shutil

directory = "directory\path\folder"

for filename in os.listdir(directory):
    # Create the full file path
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        # Create a new folder with the same name as the file (without the extension)
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(directory, folder_name)
        
        os.makedirs(folder_path, exist_ok=True)

        shutil.move(file_path, os.path.join(folder_path, filename))

print("Files have been moved to their respective folders.")
