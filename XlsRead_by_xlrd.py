import xlrd
from datetime import datetime


def xls_read():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xlsx')
    # 获取所有sheet名称
    sheet_name = workbook.sheet_names()
    print(sheet_name)
    sheet2_name = sheet_name[1]

    # 根据sheet索引或名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)
    sheet2 = workbook.sheet_by_name('Sheet2')

    # 打印sheet的名称、行数和列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # 获取正行和整列的值
    rows = sheet2.row_values(3)
    cols = sheet2.col_values(2)
    print(rows, cols)

    # 获取单元格内容
    print(sheet2.cell(1, 0).value)
    print(sheet2.cell_value(1, 0))
    print(sheet2.row(1)[0].value)

    # 获取单元格数据类型
    print(sheet2.cell(1, 0).ctype)
    print(sheet2.cell(1, 1).ctype)
    print(sheet2.cell(1, 2).ctype)
    print(sheet2.cell(2, 4).ctype)


if __name__ == '__main__':
    xls_read()
