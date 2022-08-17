import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
for i in range(15):
    worksheet.write(f'A{i}', "Hello World")
workbook.close()