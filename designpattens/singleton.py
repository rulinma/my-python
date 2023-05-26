# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 21:45
@Auth ： rulinma@gmail.com
@File ：singleton.py
@IDE ：PyCharm
"""


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Singleton:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Singleton name is " + self.name

    def __repr__(self):
        return "Singleton name is " + self.name


if __name__ == '__main__':
    s1 = Singleton("Tom")
    s2 = Singleton("Jerry")
    print(s1 == s2)
