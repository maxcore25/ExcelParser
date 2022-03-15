import os
from PyPDF2 import PdfFileMerger

path = os.getcwd() + '\\final_docs\\'
print(path)
counter = 0

for pdf_letter in os.scandir(path):
    counter += 1
    merger = PdfFileMerger()

    merger.append(path + pdf_letter.name)
    merger.append('Приложение к письму оспаривание КС.pdf')

    merger.write(os.getcwd() + '\\merged_letters\\' + f'letter_700_PP_{counter + 1}.pdf')
    merger.close()
    print('Merged:', pdf_letter.name)
