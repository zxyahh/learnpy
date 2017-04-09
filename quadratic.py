# -*- coding:utf-8 -*-
import math
a = int(input('请输入a：'))
b = int(input('请输入b：'))
c = int(input('请输入c：'))
def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2
print(quadratic(a,b,c))
