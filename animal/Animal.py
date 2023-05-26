# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 21:01
@Auth ： rulinma@gmail.com
@File ：Animal.py
@IDE ：PyCharm
"""
from abc import abstractmethod


class Animal:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return "Animal name is " + self.name + " age is " + str(self.age)

    def __repr__(self):
        return "Animal name is " + self.name + " age is " + str(self.age)
