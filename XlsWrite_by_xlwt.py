import datetime

from xlwt import *


def set_style(name, height, bold=False, fmt='yy/mm/dd'):
    style = XFStyle()
    font = Font()

    # 字体类型
    font.name = name
    # 加粗
    font.bold = bold
    # 字体大小
    font.height = height
    # 字体颜色，0是黑色，2是红色
    font.colour_index = 0
    # 设置字符串格式
    style.num_format_str = fmt

    font.underline = Font.UNDERLINE_DOUBLE

    style.font = font

    return style


def write_excel_by_workbook():
    w = Workbook()
    sheet1 = w.add_sheet('stu')
    
    row = ['姓名', '年龄', '出生日期', '爱好', '关系']
    column = ['小杰', '小胖', '小明', '大神', '大仙', '小敏', '无名']

    for i in range(0, len(row)):
        sheet1.write(
            0, i, row[i], set_style(
                'Times New Roman', 220, bold=True))

    for j in range(0, len(column)):
        sheet1.write(j + 1, 0, column[j], set_style('Times New Roman', 220))

    sheet1.write_merge(1, 2, 4, 4, '好朋友')
    sheet1.write_merge(3, 5, 4, 4, '同学')
    sheet1.write_merge(7, 7, 2, 4, '暂无')

    # 加入日期时间，通过指定style
    sheet1.write(1, 2, datetime.datetime.now(),
                 set_style('Times New Roman',
                           220,
                           fmt='yyyy-mm-dd'))

    # 加入超链接
    sheet1.write(8, 0, Formula(
        'HYPERLINK' +
        '("http://www.cnblogs.com/zhoujie","jzhou\'s blog")'))

    w.save(r'C:\Program Files\Python35\test\demo1.xls')

# 各种日期格式


def test_format():
    w = Workbook()
    sheet = w.add_sheet('date')

    fmts = [

        'M/D/YY',

        'D-MMM-YY',

        'D-MMM',

        'MMM-YY',

        'h:mm AM/PM',

        'h:mm:ss AM/PM',

        'h:mm',

        'h:mm:ss',

        'M/D/YY h:mm',

        'mm:ss',

        '[h]:mm:ss',

        'mm:ss.0',

    ]

    i = 0
    style = XFStyle()
    for fmt in fmts:
        sheet.write(i, 0, fmt)
        style.num_format_str = fmt
        sheet.write(i, 3, datetime.datetime.now(), style)
        i += 1

    w.save(r'C:\Program Files\Python35\test\demo2.xls')


if __name__ == '__main__':
    test_format()
