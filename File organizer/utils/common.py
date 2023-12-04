import os, sys
import shutil

# abc.txt
def get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)