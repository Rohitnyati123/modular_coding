import os, sys
import shutil
from flask import Flask, request, render_template
from utils.common import get_file_extension, create_directory
from utils.file_organizer import FileOrganizer

app = Flask(__name__)


# localhost:5000
@app.route('/', methods = ['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        source_directory = request.form['source_directory']
        # source_directory1= "D:\success analytics\modular_coding\File organizer\images"
        message=FileOrganizer(source_directory)
        message.organize_files()
        # message = FileOrganizer.organize_files(source_directory)

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run(debug=True)

