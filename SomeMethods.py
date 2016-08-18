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

#2队比赛，分别有队员a,b,c和x,y,z，已知a和x不比赛，c和x、z不比赛，求对阵情况
def team():
    team1 = ['a', 'b', 'c']
    team2 = ['x', 'y', 'z']

    team3 = []
    team4 = []
    for t1 in team1:
        if t1=='c':
            for t2 in team2:
                if(t2!='x' and t2!='z'):print(t1,t2)
                else:team4.append(t2)
        else:team3.append(t1)

    for t3 in team3:
        if t3=='a':
            for t4 in team4:
                if t4!='x':print(t3,t4)
                else:t5 = t4
        else:print(t3,t5)

if __name__ == '__main__':
    #print(convert_Camel_to_low_underline('MyNameIs'))
    #print(convert_Camel_to_low_underline_by_regular('MyNameIs'))
    team()