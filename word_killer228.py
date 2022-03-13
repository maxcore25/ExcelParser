import os


def do_word_nahui(path):
    for file in os.scandir(path):
        filename, file_extension = os.path.splitext(file.name)
        if file_extension == '.docx':
            os.remove(os.path.join(path, file.name))
            print('Removed:', file.name)
