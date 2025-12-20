#!/usr/bin/env python3
"""
案例4：文件读写
功能：创建、读取、写入文件
"""

def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"文件 {filename} 写入成功")
    except Exception as e:
        print(f"写入文件时出错: {e}")

def read_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"文件 {filename} 内容:")
        print(content)
        return content
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except Exception as e:
        print(f"读取文件时出错: {e}")

if __name__ == "__main__":
    filename = "example.txt"
    content = "这是一个文件读写示例\n第二行内容\n第三行内容"
    
    write_to_file(filename, content)
    read_from_file(filename)
    
    # 追加内容
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write("\n追加的内容")
        print("\n追加内容后:")
        read_from_file(filename)
    except Exception as e:
        print(f"追加内容时出错: {e}")