import os
from PyPDF2 import PdfFileMerger


def do_merge_epta(path):
    counter = 0

    for pdf_letter in os.scandir(path):
        counter += 1
        merger = PdfFileMerger()

        merger.append(path + pdf_letter.name)
        merger.append('Приложение к письму оспаривание КС.pdf')

        merger.write(os.path.join(path, f'letter_700_PP_{counter + 1}.pdf'))
        merger.close()
        print('Merged:', pdf_letter.name)
