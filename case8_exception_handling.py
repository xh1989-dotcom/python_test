#!/usr/bin/env python3
"""
案例8：异常处理
功能：捕获和处理各种异常
"""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：输入必须是数字")
        return None
    else:
        print(f"计算成功，结果是: {result}")
        return result
    finally:
        print("除法运算完成")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 {filename}")
        return None
    else:
        return content

if __name__ == "__main__":
    divide(10, 2)
    divide(10, 0)
    divide("10", 2)
    
    read_file("nonexistent.txt")