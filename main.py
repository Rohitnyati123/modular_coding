from utils.file_organizer import FileOrganizer

if __name__=="__main__":
    source_directory=input("Enter your source directory path")
    organize_file=FileOrganizer(source_directory)
    organize_file.organize_files()