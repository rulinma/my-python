# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 19:48
@Auth ： rulinma@gmail.com
@File ：calculate.py
@IDE ：PyCharm
"""


def plus(a, b):
    print("plus")
    return a + b


class Calculate:

    def __init__(self, name=None):
        if name is None:
            print("init Calculate")
            self.name = "None"
        else:
            print("init Calculate with name", name)
            self.name = name

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    def __str__(self, *args, **kwargs):
        # return "Calculate: " + self.name is None and "" or self.name
        return "Calculate: " + self.name


if __name__ == '__main__':
    print("run calculate.py")