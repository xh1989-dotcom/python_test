print("=" * 50)
print("Python循环语句")
print("=" * 50)

print("for循环:")
print("  遍历列表:")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"    {fruit}")

print("\n  遍历字符串:")
for char in "Python":
    print(f"    {char}")

print("\n  range()函数:")
for i in range(5):
    print(f"    {i}")

print("\n  range带参数:")
for i in range(2, 5):
    print(f"    {i}")

print("\nwhile循环:")
count = 0
while count < 3:
    print(f"    count = {count}")
    count += 1

print("\n循环控制:")
print("  break - 跳出循环:")
for i in range(5):
    if i == 3:
        break
    print(f"    {i}")

print("\n  continue - 跳过本次循环:")
for i in range(5):
    if i == 2:
        continue
    print(f"    {i}")

print("\n循环中的else:")
for i in range(3):
    print(f"    {i}")
else:
    print("  循环正常结束")

print("\n嵌套循环:")
for i in range(2):
    for j in range(3):
        print(f"    ({i}, {j})")
