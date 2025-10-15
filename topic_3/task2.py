print(">>> Тестування списків <<<")

nums = [1, 2, 3]
print("Початковий список:", nums)

nums.append(8)
print("append(8):", nums)

nums.extend([5, 6])
print("extend([5,6]):", nums)

nums.insert(1, 9)
print("insert(1,9):", nums)

nums.remove(5)
print("remove(5):", nums)

nums.sort()
print("sort():", nums)

nums.reverse()
print("reverse():", nums)

copy_nums = nums.copy()
print("copy():", copy_nums)

nums.clear()
print("clear():", nums)

print(">>> Кінець тесту списку <<<")
