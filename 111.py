def f(x):
    return x*x

def by_name(tu):
    return tu[0][0].lower()

def by_score(tu):
    return tu[1]

class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def heigth(self):
        return self._heigth

    @width.setter
    def width(self,width):
        self._width = width

    @heigth.setter
    def heigth(self,heigth):
        self._heigth = heigth

    @property
    def resolution(self):
        return self._width + self._heigth

#map函数，作用列表每一元素
'''l = map(f,[1,2,3,4])
print(list(l))'''

#soted函数
'''a = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
b = sorted(a,key=by_name)
c = sorted(a,key=by_score,reverse=True)
print(b,'\n',c)'''

#@property，函数作为属性
s = Screen()
s.width = 12
s.heigth = 25
print(s.width,s.heigth,s.resolution)


