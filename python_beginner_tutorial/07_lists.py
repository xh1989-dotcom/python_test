print("=" * 50)
print("Python列表")
print("=" * 50)

print("创建列表:")
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "hello", True, 3.14]
empty = []

print(f"  numbers: {numbers}")
print(f"  fruits: {fruits}")
print(f"  mixed: {mixed}")
print(f"  empty: {empty}")

print("\n访问元素:")
print(f"  fruits[0] = {fruits[0]}")
print(f"  fruits[-1] = {fruits[-1]}")
print(f"  fruits[1:3] = {fruits[1:3]}")

print("\n修改元素:")
fruits[0] = "草莓"
print(f"  修改后: {fruits}")

print("\n列表操作:")
print(f"  添加元素 - append(): {fruits.append('西瓜')}; 结果: {fruits}")
print(f"  插入元素 - insert(): {fruits.insert(1, '葡萄')}; 结果: {fruits}")
print(f"  删除元素 - remove(): {fruits.remove('香蕉')}; 结果: {fruits}")
print(f"  弹出元素 - pop(): {fruits.pop()}; 结果: {fruits}")
print(f"  列表长度 - len(): {len(fruits)}")
print(f"  元素是否存在 - in: {'苹果' in fruits}")

print("\n列表排序:")
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"  排序前: {nums}")
print(f"  排序后: {sorted(nums)}")
nums.sort()
print(f"  sort()后: {nums}")

print("\n列表推导式:")
squares = [x**2 for x in range(5)]
print(f"  [x**2 for x in range(5)]: {squares}")
evens = [x for x in range(10) if x % 2 == 0]
print(f"  偶数: {evens}")
