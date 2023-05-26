# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 21:17
@Auth ： rulinma@gmail.com
@File ：cal.app.py
@IDE ：PyCharm
"""
from cal.calculate import Calculate

if __name__ == '__main__':
    print("run cal.app.py")
    c = Calculate()
    print(c.add(1, 2))