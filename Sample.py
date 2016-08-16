import xlrd

# 读取所有单元格


def read_all_excel():
    workbook = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xlsx')
    sheet = workbook.sheet_by_name('Sheet2')
    [print(sheet.cell_value(i, j)) for i in range(sheet.nrows)
     for j in range(sheet.ncols)]

# 按行读取单元格


def read_excel_by_row():
    workbook = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xlsx')
    sheet = workbook.sheet_by_name('Sheet2')
    [print(sheet.row_values(i)) for i in range(sheet.nrows)]

# 按列读取单元格


def read_excel_by_col():
    workbook = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xlsx')
    sheet = workbook.sheet_by_name('Sheet2')
    [print(sheet.col_values(i)) for i in range(sheet.ncols)]

# 读取合并单元格


def read_merge_cells():
    workbook = xlrd.open_workbook(r'C:\Program Files\Python35\test\demo.xlsx')
    sheet2 = workbook.sheet_by_index(1)
    merge = []
    for (row, row_tange, col, col_range) in sheet2.merged_cells:
        merge.append([row, col])
    print(merge)

if __name__ == '__main__':
    read_merge_cells()
    read_excel_by_row()
    read_all_excel()
