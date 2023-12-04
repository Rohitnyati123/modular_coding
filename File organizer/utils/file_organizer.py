import os, sys
import shutil
from utils.common import get_file_extension, create_directory

class FileOrganizer:
    def __init__(self, source_directory):
        self.source_directory = source_directory


    def organize_files(self):
        if not os.path.exists(self.source_directory):
            print("Source directory does not exist.")
            return
        for filename in os.listdir(self.source_directory):
            file_path = os.path.join(self.source_directory, filename)

            if os.path.isfile(file_path):
                extension = get_file_extension(filename)
                if extension:
                    destination_directory = os.path.join(self.source_directory, extension[1:])
                    create_directory(destination_directory)

                    try:
                        shutil.move(file_path, os.path.join(destination_directory, filename))
                        print(f"Moved '{filename}' to '{destination_directory}'")
                    except Exception as e:
                        print(f"Error moving '{filename}' to '{destination_directory}': {e}")
                else:
                    print(f"Skipped '{filename}' as it doesn't have an extension.")
            else:
                print(f"Skipped '{filename}' as it is not a file.")

        print("File organization completed.")