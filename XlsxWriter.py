import xlsxwriter

def write():
    workbook = xlsxwriter.Workbook(r'C:\Program Files\Python35\test\demo3.xlsx')
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold':True})

    worksheet.write('A1','hello',bold)
    worksheet.write(1,0,'world')

    worksheet.insert_image('B5',r'C:\Program Files\Python35\test\字段长度类型.png')
    workbook.close()

if __name__ == '__main__':
    write()