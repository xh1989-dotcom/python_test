#!/usr/bin/env python3
"""
案例1：简单计算器
功能：实现加减乘除四则运算
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

if __name__ == "__main__":
    print("简单计算器")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    
    choice = input("请选择操作(1-4): ")
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("无效的选择")