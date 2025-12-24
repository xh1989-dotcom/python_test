print("=" * 50)
print("Python文件操作")
print("=" * 50)

print("创建测试文件...")
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")

print("\n读取文件 - 一次性读取:")
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"  {content}")

print("\n读取文件 - 逐行读取:")
with open("test.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"  第{i}行: {line.strip()}")

print("\n写入文件 - 追加模式:")
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的行\n")

print("\n验证追加结果:")
with open("test.txt", "r", encoding="utf-8") as f:
    print(f"  {f.read()}")

print("\n文件操作模式:")
print("  'r' - 读取（默认）")
print("  'w' - 写入（会覆盖）")
print("  'a' - 追加")
print("  'r+' - 读写")
print("  'b' - 二进制模式")

print("\n使用with语句:")
print("  with语句会自动关闭文件")
print("  不需要手动调用close()")

print("\n文件操作函数:")
print("  read() - 读取全部")
print("  readline() - 读取一行")
print("  readlines() - 读取所有行到列表")
print("  write() - 写入")
print("  writelines() - 写入多行")

print("\n清理测试文件...")
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("  test.txt 已删除")
