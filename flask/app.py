import os,sys
import shutil
from utils.common import get_file_extension,create_directory
from flask import Flask,render_template,request

app=Flask(__name__)

def organize_files(source_directory):
    if not os.path.exists(source_directory):
        print("source directory not exists")
        return

    for filename in os.listdir(source_directory):
        file_path=os.path.join(source_directory,filename)
        if os.path.isfile(file_path):
            extension = get_file_extension(filename)
            if extension:
                destination_directory=os.path.join(source_directory,extension[1:])
                create_directory(destination_directory)

            try:
                shutil.move(file_path,os.path.join(destination_directory, filename))
                print(f"moved'{filename}' to'{destination_directory}'")
            except Exception as e:
                print(f"Error during moving '{filename}' to '{destination_directory}':{e}")
            else:
                print(f"skipped '{filename}' as it doesn't have any extension")
        else:
            print(f"skipped '{filename}' as it doesnot have a file")
    
    print("our files are organized")

@app.route('/',methods=['GET','POST'])
def login():
    message=""
    if request.method=='POST':
        source_directory=request.form['source_directory']
        message= organize_files(source_directory)

    return render_template('index1.html',message=message)


if __name__=='__main__':
    app.run(debug=True)
