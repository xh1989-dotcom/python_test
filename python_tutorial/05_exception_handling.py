"""
Python异常处理
==============

本教程介绍Python中的异常处理机制
"""

print("=" * 60)
print("Python异常处理教程")
print("=" * 60)

# 1. 基本异常处理
print("\n1. 基本异常处理")
print("-" * 60)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")
    print("除数不能为零")

try:
    num = int("abc")
except ValueError as e:
    print(f"捕获到异常: {e}")
    print("无法将字符串转换为整数")

# 2. 多个异常处理
print("\n2. 多个异常处理")
print("-" * 60)

def divide_numbers(a, b):
    """除法运算"""
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("错误：除数不能为零")
    except TypeError:
        print("错误：参数类型不正确")
    except Exception as e:
        print(f"未知错误: {e}")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 2)

# 3. else和finally
print("\n3. else和finally")
print("-" * 60)

def safe_divide(a, b):
    """安全的除法运算"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为零")
        return None
    else:
        print("运算成功")
        return result
    finally:
        print("无论是否异常，都会执行")

print("safe_divide(10, 2):")
result = safe_divide(10, 2)
print(f"结果: {result}\n")

print("safe_divide(10, 0):")
result = safe_divide(10, 0)
print(f"结果: {result}")

# 4. 抛出异常
print("\n4. 抛出异常")
print("-" * 60)

def check_age(age):
    """检查年龄"""
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150岁")
    print(f"年龄{age}是有效的")

try:
    check_age(25)
    check_age(-5)
except ValueError as e:
    print(f"捕获到异常: {e}")

# 5. 自定义异常
print("\n5. 自定义异常")
print("-" * 60)

class InsufficientFundsError(Exception):
    """余额不足异常"""
    pass

class BankAccount:
    """银行账户"""
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        """取款"""
        if amount > self.balance:
            raise InsufficientFundsError(f"余额不足，当前余额{self.balance}，尝试取款{amount}")
        self.balance -= amount
        print(f"取款{amount}成功，余额{self.balance}")

account = BankAccount(1000)
try:
    account.withdraw(500)
    account.withdraw(800)
except InsufficientFundsError as e:
    print(f"捕获到异常: {e}")

# 6. 异常链
print("\n6. 异常链")
print("-" * 60)

def read_config():
    """读取配置文件"""
    try:
        with open("config.txt", "r") as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError("配置文件不存在") from e

try:
    config = read_config()
except RuntimeError as e:
    print(f"捕获到异常: {e}")
    if e.__cause__:
        print(f"原始异常: {e.__cause__}")

# 7. 常见异常类型
print("\n7. 常见异常类型")
print("-" * 60)

exceptions = [
    ("IndexError", lambda: [1, 2, 3][10]),
    ("KeyError", lambda: {"a": 1}["b"]),
    ("AttributeError", lambda: 123.append(4)),
    ("TypeError", lambda: "1" + 1),
    ("NameError", lambda: undefined_var),
]

for name, func in exceptions:
    try:
        func()
    except Exception as e:
        print(f"{name}: {e}")

# 8. 上下文管理器
print("\n8. 上下文管理器")
print("-" * 60)

class FileManager:
    """文件管理器"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"关闭文件: {self.filename}")
        if exc_type:
            print(f"发生异常: {exc_val}")
        return True

# 使用自定义上下文管理器
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")

# 9. 警告
print("\n9. 警告")
print("-" * 60)

import warnings

def deprecated_function():
    """已弃用的函数"""
    warnings.warn("这个函数已弃用，请使用新函数", DeprecationWarning)
    print("函数执行")

deprecated_function()

# 10. 实战练习
print("\n10. 实战练习")
print("-" * 60)

# 练习1：数据验证
print("练习1：数据验证")
def validate_user_data(data):
    """验证用户数据"""
    errors = []
    
    if not isinstance(data, dict):
        raise TypeError("数据必须是字典类型")
    
    if "name" not in data:
        errors.append("缺少name字段")
    elif not isinstance(data["name"], str) or len(data["name"]) < 2:
        errors.append("name必须是至少2个字符的字符串")
    
    if "age" not in data:
        errors.append("缺少age字段")
    elif not isinstance(data["age"], int) or data["age"] < 0 or data["age"] > 150:
        errors.append("age必须是0-150之间的整数")
    
    if "email" in data and "@" not in data["email"]:
        errors.append("email格式不正确")
    
    if errors:
        raise ValueError("数据验证失败: " + ", ".join(errors))
    
    return True

try:
    validate_user_data({"name": "张", "age": 200})
except ValueError as e:
    print(f"验证失败: {e}")

try:
    validate_user_data({"name": "张三", "age": 25, "email": "test@example.com"})
    print("验证成功")
except ValueError as e:
    print(f"验证失败: {e}")

# 练习2：安全的输入处理
print("\n练习2：安全的输入处理")
def get_positive_integer(prompt):
    """获取正整数输入"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入正整数")
                continue
            return value
        except ValueError:
            print("请输入有效的整数")

# 练习3：文件处理
print("\n练习3：安全的文件处理")
def process_file(filename):
    """处理文件"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.splitlines()
            print(f"文件有{len(lines)}行")
            return lines
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 {filename}")
        return None
    except UnicodeDecodeError:
        print(f"错误：文件 {filename} 编码不正确")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 练习4：网络请求处理
print("\n练习4：网络请求处理模拟")
class NetworkError(Exception):
    """网络错误"""
    pass

class TimeoutError(Exception):
    """超时错误"""
    pass

def fetch_data(url, timeout=5):
    """模拟网络请求"""
    import random
    
    if random.random() < 0.3:
        raise NetworkError("网络连接失败")
    
    if random.random() < 0.2:
        raise TimeoutError("请求超时")
    
    return {"status": "success", "data": "示例数据"}

def safe_fetch(url, max_retries=3):
    """安全的网络请求"""
    for attempt in range(max_retries):
        try:
            return fetch_data(url)
        except NetworkError as e:
            print(f"网络错误 (尝试 {attempt + 1}/{max_retries}): {e}")
        except TimeoutError as e:
            print(f"超时错误 (尝试 {attempt + 1}/{max_retries}): {e}")
        except Exception as e:
            print(f"未知错误: {e}")
            break
    
    print(f"在{max_retries}次尝试后失败")
    return None

# 练习5：数据库操作模拟
print("\n练习5：数据库操作模拟")
class DatabaseError(Exception):
    """数据库错误"""
    pass

class Database:
    """模拟数据库"""
    def __init__(self):
        self.data = {}
        self.connected = False
    
    def connect(self):
        """连接数据库"""
        if self.connected:
            raise DatabaseError("已经连接到数据库")
        self.connected = True
        print("数据库连接成功")
    
    def disconnect(self):
        """断开连接"""
        if not self.connected:
            raise DatabaseError("数据库未连接")
        self.connected = False
        print("数据库断开连接")
    
    def insert(self, key, value):
        """插入数据"""
        if not self.connected:
            raise DatabaseError("数据库未连接")
        if key in self.data:
            raise DatabaseError(f"键 {key} 已存在")
        self.data[key] = value
        print(f"插入数据: {key} = {value}")
    
    def get(self, key):
        """获取数据"""
        if not self.connected:
            raise DatabaseError("数据库未连接")
        if key not in self.data:
            raise DatabaseError(f"键 {key} 不存在")
        return self.data[key]

db = Database()
try:
    db.connect()
    db.insert("user1", {"name": "张三", "age": 25})
    db.insert("user2", {"name": "李四", "age": 30})
    print(f"获取user1: {db.get('user1')}")
    db.disconnect()
except DatabaseError as e:
    print(f"数据库错误: {e}")

print("\n" + "=" * 60)
print("教程完成！")
print("=" * 60)
