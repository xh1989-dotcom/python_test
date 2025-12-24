print("=" * 50)
print("Python字典")
print("=" * 50)

print("创建字典:")
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
print(f"  person: {person}")

print("\n访问字典:")
print(f"  person['name']: {person['name']}")
print(f"  person.get('age'): {person.get('age')}")
print(f"  person.get('job', '未知'): {person.get('job', '未知')}")

print("\n修改字典:")
person['age'] = 26
person['job'] = "工程师"
print(f"  修改后: {person}")

print("\n删除元素:")
del person['city']
print(f"  删除city后: {person}")
age = person.pop('age')
print(f"  pop('age'): {age}, 剩余: {person}")

print("\n字典方法:")
print(f"  keys(): {list(person.keys())}")
print(f"  values(): {list(person.values())}")
print(f"  items(): {list(person.items())}")

print("\n遍历字典:")
for key, value in person.items():
    print(f"    {key}: {value}")

print("\n字典合并:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"  合并后: {merged}")

print("\n字典推导式:")
squares = {x: x**2 for x in range(3)}
print(f"  {{x: x**2 for x in range(3)}}: {squares}")
