import os

path = os.getcwd() + '\\final_docs\\'
print(path)
all_count = 0
docx_count = 0

for file in os.scandir(path):
    all_count += 1
    filename, file_extension = os.path.splitext(file.name)
    if file_extension == '.docx':
        docx_count += 1
        os.remove(path + file.name)
        print('Removed:', file.name)

print(all_count, docx_count)
