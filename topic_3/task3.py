print(">>> Тестування словників <<<")

person = {"name": "Олеся", "age": 18}
print("Початковий словник:", person)

person.update({"city": "Чернігів"})
print("update({'city':'Чернігів'}):", person)

print("keys():", list(person.keys()))
print("values():", list(person.values()))
print("items():", list(person.items()))

del person["age"]
print("del age:", person)

person.clear()
print("clear():", person)

print(">>> Кінець тесту словників <<<")
