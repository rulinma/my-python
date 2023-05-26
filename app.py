# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 20:28
@Auth ： rulinma@gmail.com
@File ：app.py
@IDE ：PyCharm
"""

from cal.calculate import Calculate


# __main__表示当前模块在直接执行时的名字。如果模块被导入，__main__将不会被执行。

def main():
    c = Calculate()
    print(c.add(1, 2))
    print(c.sub(1, 2))
    print(c.mul(1, 2))
    print(c.div(1, 2))
    print(c)
    d = Calculate()
    print(d)
    print(Calculate.add(1, 2))


if __name__ == '__main__':
    print("run app.py")

    main()
