print("=" * 50)
print("Python条件语句")
print("=" * 50)

print("if-elif-else语句:")
age = 18

if age < 18:
    print("  未成年人")
elif age < 65:
    print("  成年人")
else:
    print("  老年人")

print("\n比较运算符:")
x, y = 5, 10
if x < y:
    print(f"  {x} < {y} 成立")

print("\n逻辑运算符:")
a, b = True, False
if a and b:
    print("  both True")
elif a or b:
    print("  at least one is True")

print("\n三元表达式:")
status = "成年" if age >= 18 else "未成年"
print(f"  age >= 18 ? '{status}'")

print("\n练习：编写一个成绩评级程序")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"  成绩 {score} 分，等级: {grade}")
