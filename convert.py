import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('supdata3.xlsx')
    sh = wb.sheet_by_name('Taxonomic abundances')
    supdata3 = open('supdata3.csv', 'w')
    wr = csv.writer(supdata3, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    supdata3.close()

# runs the csv_from_excel function:
csv_from_excel()