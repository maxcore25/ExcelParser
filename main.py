from docxtpl import DocxTemplate
import openpyxl
from docx2pdf import convert

# Define variable to load the workbook
workbook = openpyxl.load_workbook("120519060Марьина Роща.xlsx")
# Define variable to read the active sheet:
worksheet = workbook.active
# Iterate the loop to read the cell values
for i in range(1, worksheet.max_row):
    vals = []
    for col in worksheet.iter_cols(0, 30):
        vals.append(col[i].value)
    doc = DocxTemplate("Mail_for_700_PP.docx")
    print(vals)
    if 'ИНН' in str(vals[29]):
        spl_vals_29 = vals[29].split(',')
        fio, inn = spl_vals_29[0], spl_vals_29[1].split(':')[1]
        context = {'fio': fio, 'square': vals[11], 'inn': inn, 'address': vals[13]}
    else:
        context = {'fio': vals[5], 'square': vals[2], 'inn': '-', 'address': vals[3]}
    doc.render(context)
    doc.save(f"./final_docs/letter_700_PP_{i+1}.docx")

convert('./final_docs')
