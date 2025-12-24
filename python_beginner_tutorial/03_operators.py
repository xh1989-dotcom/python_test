print("=" * 50)
print("Python运算符")
print("=" * 50)

a, b = 10, 3

print("算术运算符:")
print(f"  {a} + {b} = {a + b}")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} / {b} = {a / b:.2f}")
print(f"  {a} // {b} = {a // b}")
print(f"  {a} % {b} = {a % b}")
print(f"  {a} ** {b} = {a ** b}")

print("\n比较运算符:")
print(f"  {a} == {b}: {a == b}")
print(f"  {a} != {b}: {a != b}")
print(f"  {a} > {b}: {a > b}")
print(f"  {a} < {b}: {a < b}")

print("\n逻辑运算符:")
print(f"  True and False = {True and False}")
print(f"  True or False = {True or False}")
print(f"  not True = {not True}")

print("\n赋值运算符:")
x = 5
x += 3
print(f"  x += 3: {x}")
x -= 2
print(f"  x -= 2: {x}")
