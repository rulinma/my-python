# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 21:01
@Auth ： rulinma@gmail.com
@File ：Animal.py
@IDE ：PyCharm
"""


class Animal:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def run(self):
        print(self.name + "Animal is running")

    def __str__(self):
        return "Animal name is " + self.name + " age is " + str(self.age)

    def __repr__(self):
        return "Animal name is " + self.name + " age is " + str(self.age)
