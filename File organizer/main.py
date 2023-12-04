from utils.file_organizer import FileOrganizer

if __name__ == "__main__":
                  
    source_directory = input("Enter Your source Directory file location")
    organize_file = FileOrganizer(source_directory)
    organize_file.organize_files()
#    organize_file(source_directory) 