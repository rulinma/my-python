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
    def __init__(self):
        print("init Calculate")
        pass

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
