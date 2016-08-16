import re

# 常规方式驼峰转小写下划线
def convert_Camel_to_low_underline(str):
    str_camel = ''
    x = 0
    for s in str:
        if (x != 0 and s.islower() == False):
            s = '_' + s
        str_camel += s
        x += 1

    return str_camel.lower()

# 正则方式驼峰转小写下划线
def convert_Camel_to_low_underline_by_regular(str):
    captial = re.findall('[A-Z]', str)

    for c in captial:
        if str.index(c) != 0:
            str = re.sub(c, '_' + c, str)

    return str.lower()

if __name__ == '__main__':
    print(convert_Camel_to_low_underline('MyNameIs'))
    print(convert_Camel_to_low_underline_by_regular('MyNameIs'))
    a=2
