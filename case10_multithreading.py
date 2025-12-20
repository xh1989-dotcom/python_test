#!/usr/bin/env python3
"""
案例10：多线程编程
功能：使用threading模块实现多线程
"""

import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(f"数字: {i}")
        time.sleep(0.5)

def print_letters():
    for letter in 'ABCDEFGHIJ':
        print(f"字母: {letter}")
        time.sleep(0.7)

if __name__ == "__main__":
    print("单线程执行:")
    start_time = time.time()
    print_numbers()
    print_letters()
    print(f"单线程耗时: {time.time() - start_time:.2f} 秒")
    
    print("\n多线程执行:")
    start_time = time.time()
    
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"多线程耗时: {time.time() - start_time:.2f} 秒")