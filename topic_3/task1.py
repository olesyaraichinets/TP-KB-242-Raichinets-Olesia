print(">>> Привіт! Це калькулятор. <<<")

while True:
    op = input("Введіть операцію (+, -, *, /) або 'вихід' для завершення: ")

    if op.lower() == "вихід":
        print(">>> До побачення! <<<")
        break

    a = float(input("Перше число: "))
    b = float(input("Друге число: "))

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Невідома операція.")
