# -- coding: utf-8 --
# Introduction to Object Oriented Programming (OOP)
# 面向对象基础介绍
# class 是 用来build object的 模板template
class Person:
    # 构造函数
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def hello(self):
        print(self.name + " say hello")


p1 = Person("alex", 29)
p2 = Person("mio", 29)

p1.hello()
p2.hello()

print(isinstance(p1, Person))