print("=" * 50)
print("Python变量和数据类型")
print("=" * 50)

name = "张三"      # 字符串
age = 25           # 整数
height = 1.75      # 浮点数
is_student = True  # 布尔值

print(f"姓名: {name}, 类型: {type(name).__name__}")
print(f"年龄: {age}, 类型: {type(age).__name__}")
print(f"身高: {height}, 类型: {type(height).__name__}")
print(f"是学生: {is_student}, 类型: {type(is_student).__name__}")

print("\n练习题：")
print("1. 创建变量存储你的姓名和年龄")
print("2. 尝试修改上面的变量值")
print("3. 使用type()函数检查变量类型")
