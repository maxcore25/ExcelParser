import xlrd
import csv
import os
from multiprocessing import Pool
from datetime import datetime


def convert_xls_csv(filename):
    wb = xlrd.open_workbook(f'./xls_tables/{filename}')
    count_sheets = wb.nsheets
    csv_f = open(f'./csv_tables/{filename[:-4]}.csv', 'w')
    csv_writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)

    for i in range(count_sheets):
        sheet = wb.sheet_by_index(i)
        skip_rows = 8 if i == 0 else 2

        for rownum in range(skip_rows, sheet.nrows):
            vals = sheet.row_values(rownum)[2:]
            csv_writer.writerow(vals)

    csv_f.close()


if __name__ == '__main__':
    start_time = datetime.now()

    xls_list = os.listdir('./xls_tables')
    n = len(xls_list)

    # время работы 0:00:32.195499
    with Pool(n) as p:
        p.map(convert_xls_csv, xls_list)

    # время работы 0:01:53.973485
    # for filename in xls_list:
    #     convert_xls_csv(filename)

    print(datetime.now() - start_time)


