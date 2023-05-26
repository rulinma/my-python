# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/26 21:01
@Auth ： rulinma@gmail.com
@File ：Human.py
@IDE ：PyCharm
"""
from animal.Animal import Animal


class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self):
        print(self.name + " Human is running")

    def __str__(self):
        return "Human name is " + self.name

    def __repr__(self):
        return "Human name is " + self.name

    def __add__(self, other):
        return self.name + other.name
