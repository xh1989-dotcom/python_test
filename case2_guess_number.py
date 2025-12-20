#!/usr/bin/env python3
"""
案例2：猜数字游戏
功能：随机生成一个数字，玩家猜测并获得提示
"""

import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("猜数字游戏")
    print("我已经想好了一个1到100之间的数字")
    
    while True:
        try:
            guess = int(input("请猜一个数字: "))
            attempts += 1
            
            if guess < secret_number:
                print("太小了！再试试")
            elif guess > secret_number:
                print("太大了！再试试")
            else:
                print(f"恭喜你，猜对了！你用了{attempts}次尝试")
                break
        except ValueError:
            print("请输入有效的数字")

if __name__ == "__main__":
    guess_number()