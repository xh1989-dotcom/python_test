#!/usr/bin/env python3
"""
案例7：面向对象编程
功能：定义类和对象，实现继承和多态
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现speak方法")

class Dog(Animal):
    def speak(self):
        return f"{self.name} 汪汪叫"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁"

if __name__ == "__main__":
    animals = [Dog("旺财"), Cat("咪咪")]
    for animal in animals:
        print(animal.speak())
    
    person = Person("张三", 25)
    print(person.introduce())