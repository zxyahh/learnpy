# -*- coding:utf-8 -*-
weight=float(input('请输入你的体重：'))
hight = float(input('请输入你的身高：'))
r = weight/(hight*hight)
if r > 32:
    print('严重肥胖')
elif r >28:
    print('肥胖')
elif r > 25:
    print('过重')
elif r > 18.5:
    print('正常')
else:
    print('过轻')
