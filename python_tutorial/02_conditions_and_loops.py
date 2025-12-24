"""
Python条件语句和循环
=====================

本教程介绍Python中的条件语句和循环结构
"""

print("=" * 60)
print("Python条件语句和循环教程")
print("=" * 60)

# 1. 条件语句
print("\n1. if-elif-else 条件语句")
print("-" * 60)

age = 20

if age < 18:
    print(f"年龄 {age}：未成年人")
elif age < 65:
    print(f"年龄 {age}：成年人")
else:
    print(f"年龄 {age}：老年人")

# 嵌套条件
score = 85
if score >= 60:
    print(f"成绩 {score}：及格")
    if score >= 90:
        print("  等级：优秀")
    elif score >= 80:
        print("  等级：良好")
    else:
        print("  等级：及格")
else:
    print(f"成绩 {score}：不及格")

# 三元表达式
grade = "及格" if score >= 60 else "不及格"
print(f"\n三元表达式：grade = {grade}")

# 逻辑运算符
print("\n逻辑运算符示例:")
x, y = 10, 20
if x > 5 and y > 15:
    print(f"  {x} > 5 且 {y} > 15：成立")

if x > 15 or y > 15:
    print(f"  {x} > 15 或 {y} > 15：成立")

if not (x > 15):
    print(f"  not ({x} > 15)：成立")

# 2. for循环
print("\n2. for 循环")
print("-" * 60)

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("遍历列表:")
for fruit in fruits:
    print(f"  {fruit}")

# 遍历字符串
print("\n遍历字符串:")
for char in "Python":
    print(f"  {char}")

# 使用range()
print("\n使用range(5):")
for i in range(5):
    print(f"  {i}")

print("\n使用range(2, 6):")
for i in range(2, 6):
    print(f"  {i}")

print("\n使用range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}")

# 遍历字典
person = {"name": "张三", "age": 25, "city": "北京"}
print("\n遍历字典:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 3. while循环
print("\n3. while 循环")
print("-" * 60)

count = 0
print("while循环示例:")
while count < 5:
    print(f"  count = {count}")
    count += 1

# 无限循环示例（带break）
print("\n带break的while循环:")
count = 0
while True:
    print(f"  count = {count}")
    count += 1
    if count >= 3:
        break

# 4. 循环控制
print("\n4. 循环控制语句")
print("-" * 60)

# break - 跳出循环
print("break示例:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

# continue - 跳过本次迭代
print("\ncontinue示例:")
for i in range(5):
    if i == 2:
        continue
    print(f"  {i}")

# else - 循环正常结束时执行
print("\nelse示例（正常结束）:")
for i in range(3):
    print(f"  {i}")
else:
    print("  循环正常结束")

print("\nelse示例（break跳出）:")
for i in range(5):
    if i == 3:
        break
    print(f"  {i}")
else:
    print("  循环正常结束")
print("  循环被break打断，else不执行")

# 5. 嵌套循环
print("\n5. 嵌套循环")
print("-" * 60)

print("打印乘法表（3x3）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} × {j} = {i*j}", end="  ")
    print()

# 6. 列表推导式
print("\n6. 列表推导式")
print("-" * 60)

squares = [x**2 for x in range(6)]
print(f"平方数: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"偶数: {evens}")

# 嵌套列表推导式
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"3x3矩阵: {matrix}")

# 7. 实战练习
print("\n7. 实战练习")
print("-" * 60)

# 练习1：猜数字游戏
print("练习1：猜数字游戏")
import random
secret = random.randint(1, 10)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("  猜一个1-10的数字: "))
    attempts += 1
    if guess < secret:
        print("  太小了！")
    elif guess > secret:
        print("  太大了！")

print(f"  恭喜！你用了{attempts}次猜对了数字{secret}")

# 练习2：计算平均分
print("\n练习2：计算平均分")
scores = [85, 92, 78, 90, 88]
total = 0
count = 0

for score in scores:
    total += score
    count += 1

average = total / count
print(f"  成绩: {scores}")
print(f"  平均分: {average:.2f}")

# 练习3：查找最大值
print("\n练习3：查找最大值")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(f"  数字列表: {numbers}")
print(f"  最大值: {max_num}")

# 练习4：统计字符出现次数
print("\n练习4：统计字符出现次数")
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(f"  文本: '{text}'")
print(f"  字符统计: {char_count}")

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)
