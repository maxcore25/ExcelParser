import os
from borb.pdf.pdf import PDF
from borb.pdf.document.document import Document


def do_merge_epta(path):
    counter = 0

    # for pdf_letter in os.scandir(path):
    #     counter += 1
    #     merger = PdfFileMerger()
    #
    #     merger.append(os.path.join(path, pdf_letter.name))
    #     merger.append('Приложение к письму оспаривание КС.pdf')
    #
    #     merger.write(os.path.join(path, f'letter_700_PP_{counter + 1}.pdf'))
    #     merger.close()
    #     print('Merged:', pdf_letter.name)
    for pdf_letter in os.scandir(path):
        counter += 1

        # Прочитайте первый PDF-файл
        with open(pdf_letter, "r") as pdf_file_handle:
            input_pdf_001 = PDF.loads(pdf_file_handle)

        # Прочитайте второй PDF-файл
        with open("Приложение к письму оспаривание КС.pdf", "r") as pdf_file_handle:
            input_pdf_002 = PDF.loads(pdf_file_handle)

        # Создайте новый PDF-файл, объединив два входных файла
        output_document = Document()
        output_document.append_document(input_pdf_001)
        output_document.append_document(input_pdf_002)

        # Написать PDF
        with open(os.path.join(path, f'letter_700_PP_{counter + 1}.pdf'), "w") as pdf_out_handle:
            PDF.dumps(pdf_out_handle, output_document)
