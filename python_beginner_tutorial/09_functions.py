print("=" * 50)
print("Python函数")
print("=" * 50)

print("定义函数:")
def greet():
    print("  Hello!")

print("调用函数:")
greet()

print("\n带参数的函数:")
def greet_person(name):
    print(f"  你好, {name}!")

greet_person("张三")

print("\n带返回值的函数:")
def add(a, b):
    return a + b

result = add(3, 5)
print(f"  add(3, 5) = {result}")

print("\n默认参数:")
def greet_with_default(name, greeting="Hello"):
    print(f"  {greeting}, {name}!")

greet_with_default("李四")
greet_with_default("王五", "Hi")

print("\n关键字参数:")
def describe_pet(name, animal_type="dog"):
    print(f"  {name} 是一只 {animal_type}")

describe_pet(animal_type="cat", name="咪咪")
describe_pet("旺财")

print("\n可变参数:")
def sum_numbers(*numbers):
    total = sum(numbers)
    return total

print(f"  sum_numbers(1, 2, 3, 4) = {sum_numbers(1, 2, 3, 4)}")

def print_info(**info):
    for key, value in info.items():
        print(f"    {key}: {value}")

print("\n关键字可变参数:")
print_info(name="张三", age=25, city="北京")

print("\n变量作用域:")
x = "全局变量"
def test_scope():
    x = "局部变量"
    print(f"  函数内: {x}")

test_scope()
print(f"  函数外: {x}")
