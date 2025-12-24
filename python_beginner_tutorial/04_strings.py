print("=" * 50)
print("Python字符串操作")
print("=" * 50)

str1 = "Hello"
str2 = "Python"

print("字符串拼接:")
full = str1 + " " + str2
print(f"  {str1} + ' ' + {str2} = '{full}'")

print("\n字符串重复:")
print(f"  '{str1}' * 3 = '{str1 * 3}'")

print("\n字符串长度:")
print(f"  len('{full}') = {len(full)}")

print("\n字符串方法:")
text = "  Python is fun!  "
print(f"  原字符串: '{text}'")
print(f"  .upper(): '{text.upper()}'")
print(f"  .lower(): '{text.lower()}'")
print(f"  .strip(): '{text.strip()}'")
print(f"  .replace(' ', '-'): '{text.strip().replace(' ', '-')}'")

print("\n字符串切片:")
word = "Python"
print(f"  '{word}'[0:3] = '{word[0:3]}'")
print(f"  '{word}'[::2] = '{word[::2]}'")
print(f"  '{word}'[::-1] = '{word[::-1]}'")

print("\n字符串格式化:")
name = "Alice"
age = 25
print(f"  f-string: {name} is {age} years old")
print(f"  format: {} is {} years old".format(name, age))
