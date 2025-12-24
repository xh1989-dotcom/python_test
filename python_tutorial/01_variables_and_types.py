"""
Python变量和数据类型
===================

本教程介绍Python中的变量、数据类型和基本操作
"""

print("=" * 60)
print("Python变量和数据类型教程")
print("=" * 60)

# 1. 变量定义
print("\n1. 变量定义")
print("-" * 60)

name = "张三"
age = 25
height = 1.75
is_student = True

print(f"姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"是学生: {is_student}, 类型: {type(is_student)}")

# 2. 数值类型
print("\n2. 数值类型")
print("-" * 60)

# 整数
a = 10
b = -5
c = 0x1A  # 十六进制
d = 0o12  # 八进制
e = 0b1010  # 二进制

print(f"整数: {a}, {b}, {c}, {d}, {e}")

# 浮点数
f = 3.14
g = 2.5e3  # 科学计数法
h = 1.23e-4

print(f"浮点数: {f}, {g}, {h}")

# 复数
i = 3 + 4j
print(f"复数: {i}, 实部: {i.real}, 虚部: {i.imag}")

# 数值运算
print("\n数值运算:")
x, y = 10, 3
print(f"  {x} + {y} = {x + y}")  # 加法
print(f"  {x} - {y} = {x - y}")  # 减法
print(f"  {x} * {y} = {x * y}")  # 乘法
print(f"  {x} / {y} = {x / y}")  # 除法
print(f"  {x} // {y} = {x // y}")  # 整除
print(f"  {x} % {y} = {x % y}")  # 取余
print(f"  {x} ** {y} = {x ** y}")  # 幂运算

# 3. 字符串类型
print("\n3. 字符串类型")
print("-" * 60)

# 字符串定义
str1 = "Hello"
str2 = 'World'
str3 = """多行字符串
可以跨越多行"""
str4 = "I'm happy"  # 使用双引号包含单引号

print(f"字符串1: {str1}")
print(f"字符串2: {str2}")
print(f"字符串3: {str3}")
print(f"字符串4: {str4}")

# 字符串操作
full_name = str1 + " " + str2
print(f"字符串拼接: {full_name}")

# 字符串格式化
name = "李四"
age = 30
print(f"格式化1: {name}今年{age}岁")
print("格式化2: {}今年{}岁".format(name, age))
print("格式化3: %s今年%d岁" % (name, age))

# 字符串方法
text = "Hello Python World"
print(f"原字符串: {text}")
print(f"  小写: {text.lower()}")
print(f"  大写: {text.upper()}")
print(f"  首字母大写: {text.capitalize()}")
print(f"  每个单词首字母大写: {text.title()}")
print(f"  长度: {len(text)}")
print(f"  是否包含'Python': {'Python' in text}")
print(f"  替换: {text.replace('Python', 'Java')}")

# 字符串切片
text = "Python编程"
print(f"  原字符串: {text}")
print(f"  切片[0:3]: {text[0:3]}")
print(f"  切片[3:]: {text[3:]}")
print(f"  切片[:2]: {text[:2]}")
print(f"  切片[-2:]: {text[-2:]}")

# 4. 布尔类型
print("\n4. 布尔类型")
print("-" * 60)

bool1 = True
bool2 = False
print(f"布尔值: {bool1}, {bool2}")

# 布尔运算
print(f"  True and False = {True and False}")
print(f"  True or False = {True or False}")
print(f"  not True = {not True}")

# 数值的布尔值
print(f"  bool(0) = {bool(0)}")
print(f"  bool(1) = {bool(1)}")
print(f"  bool('') = {bool('')}")
print(f"  bool('hello') = {bool('hello')}")

# 5. 类型转换
print("\n5. 类型转换")
print("-" * 60)

# 转换为整数
print(f"int('123') = {int('123')}")
print(f"int(3.14) = {int(3.14)}")
print(f"int(True) = {int(True)}")

# 转换为浮点数
print(f"float('3.14') = {float('3.14')}")
print(f"float(10) = {float(10)}")

# 转换为字符串
print(f"str(123) = {str(123)}")
print(f"str(3.14) = {str(3.14)}")

# 转换为布尔值
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")

# 6. 列表类型
print("\n6. 列表类型")
print("-" * 60)

# 列表定义
fruits = ["苹果", "香蕉", "橙子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"水果列表: {fruits}")
print(f"数字列表: {numbers}")
print(f"混合列表: {mixed}")

# 列表操作
print(f"  长度: {len(fruits)}")
print(f"  第一个元素: {fruits[0]}")
print(f"  最后一个元素: {fruits[-1]}")
print(f"  切片[1:3]: {fruits[1:3]}")

# 列表方法
fruits.append("葡萄")
print(f"  添加后: {fruits}")

fruits.remove("香蕉")
print(f"  删除后: {fruits}")

fruits.sort()
print(f"  排序后: {fruits}")

# 7. 元组类型
print("\n7. 元组类型")
print("-" * 60)

# 元组定义（不可变）
point = (10, 20)
colors = ("红", "绿", "蓝")

print(f"坐标: {point}")
print(f"颜色: {colors}")

# 元组解包
x, y = point
print(f"  解包: x={x}, y={y}")

# 8. 字典类型
print("\n8. 字典类型")
print("-" * 60)

# 字典定义
person = {
    "name": "王五",
    "age": 28,
    "city": "北京"
}

print(f"字典: {person}")
print(f"  姓名: {person['name']}")
print(f"  年龄: {person['age']}")

# 字典操作
person["email"] = "wang@example.com"
print(f"  添加邮箱后: {person}")

person["age"] = 29
print(f"  修改年龄后: {person}")

del person["city"]
print(f"  删除城市后: {person}")

# 9. 集合类型
print("\n9. 集合类型")
print("-" * 60)

# 集合定义（无序、不重复）
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"集合1: {set1}")
print(f"集合2: {set2}")

# 集合运算
print(f"  并集: {set1 | set2}")
print(f"  交集: {set1 & set2}")
print(f"  差集: {set1 - set2}")

# 10. None类型
print("\n10. None类型")
print("-" * 60)

result = None
print(f"None值: {result}")
print(f"  类型: {type(result)}")
print(f"  bool(None) = {bool(None)}")

# 判断是否为None
if result is None:
    print("  结果为None")

# 11. 变量赋值技巧
print("\n11. 变量赋值技巧")
print("-" * 60)

# 多重赋值
a = b = c = 10
print(f"多重赋值: a={a}, b={b}, c={c}")

# 多元赋值
x, y, z = 1, 2, 3
print(f"多元赋值: x={x}, y={y}, z={z}")

# 交换变量值
x, y = y, x
print(f"交换后: x={x}, y={y}")

# 12. 类型检查
print("\n12. 类型检查")
print("-" * 60)

value = 42
print(f"值: {value}")
print(f"  type(value): {type(value)}")
print(f"  isinstance(value, int): {isinstance(value, int)}")
print(f"  isinstance(value, str): {isinstance(value, str)}")

# 多类型检查
print(f"  isinstance(value, (int, float)): {isinstance(value, (int, float))}")

# 13. 常量约定
print("\n13. 常量约定")
print("-" * 60)

# Python没有真正的常量，但约定使用大写字母表示常量
PI = 3.14159
MAX_SIZE = 100
DEFAULT_NAME = "匿名"

print(f"PI = {PI}")
print(f"MAX_SIZE = {MAX_SIZE}")
print(f"DEFAULT_NAME = {DEFAULT_NAME}")

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)

# 练习
print("\n练习:")
print("1. 创建一个包含姓名、年龄、身高的字典")
print("2. 将字符串'123'转换为整数并计算其平方")
print("3. 创建一个列表，添加5个数字，计算它们的和")
print("4. 使用三元表达式判断一个数是奇数还是偶数")
print("5. 创建一个集合，去除列表中的重复元素")

# 练习答案示例
print("\n练习答案示例:")
print("-" * 60)

# 练习1
student = {"姓名": "小明", "年龄": 20, "身高": 1.75}
print(f"练习1: {student}")

# 练习2
num = int("123")
print(f"练习2: {num}的平方 = {num ** 2}")

# 练习3
nums = [1, 2, 3, 4, 5]
print(f"练习3: 列表{nums}的和 = {sum(nums)}")

# 练习4
n = 7
parity = "奇数" if n % 2 == 1 else "偶数"
print(f"练习4: {n}是{parity}")

# 练习5
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(duplicates))
print(f"练习5: {duplicates}去重后 = {unique}")
