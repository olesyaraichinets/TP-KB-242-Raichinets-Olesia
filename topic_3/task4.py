print(">>> Пошук позиції вставки <<<")

sorted_list = [2, 4, 6, 8, 9]
print("Список:", sorted_list)

x = int(input("Введіть число для вставки: "))

pos = 0
for i in range(len(sorted_list)):
    if x < sorted_list[i]:
        pos = i
        break
else:
    pos = len(sorted_list)

print(f"Позиція для вставки: {pos}")
sorted_list.insert(pos, x)
print("Новий список:", sorted_list)

print(">>> Кінець програми <<<")
