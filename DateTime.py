from datetime import *
import  time

def getToday():
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return today
    #print(date.today())

def getYesterday():
    yesterday = datetime.now() - timedelta(days=4)
    return  yesterday

def strTodatetime(datastr,format):
    return datetime.strptime(datastr,format)

def datediff_1(begin,end):
    format = '%Y-%m-%d'
    begindate = strTodatetime(begin,format)
    enddate = strTodatetime(end,format)
    diff = enddate - begindate
    return diff

def datediff_2(begin,end):
    beginday = time.strptime('2016-7-29', '%Y-%m-%d')
    endday = time.strptime('2016-8-15', '%Y-%m-%d')
    d1 = datetime(*beginday[:3])
    d2 = datetime(*endday[:3])
    return (d2 - d1).days

def getDays_1(begin,end):
    format = '%Y-%m-%d'
    begindate = strTodatetime(begin, format)
    enddate = strTodatetime(end, format)

    days = []
    while begindate<=enddate:
        days.append(enddate.strftime(format))
        enddate = enddate - timedelta(days=1)

    return days

def getDays_2(begin,end):
    format = '%Y-%m-%d'
    interval = datediff_2(begin,end)
    endday = strTodatetime(end,format)

    days = []
    for d in range(0,interval+1):
        day = endday-timedelta(days=d)
        days.append(day.strftime(format))

    return days

'''if __name__ == '__main__':
    print(getToday())
    print(getYesterday())
    print(strTodatetime('1992/12/31','%Y/%m/%d'))
    print(datediff_1('2016-7-29','2016-8-15'))
    print(datediff_2('2016-7-29','2016-8-15'))
    print(getDays_1('2016-7-29','2016-8-15'))
    print(getDays_2('2016-7-29','2016-8-15'))'''

    '''a='1992/12/31'
    print(time.strptime('1992/12/31','%Y/%m/%d'))
    print(datetime.strptime('1992/12/31','%Y/%m/%d'))'''
