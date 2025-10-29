
def get_numbers():
    while True:
        try:
            a = int(input('Number 1: '))
            b = int(input('Number 2: '))
        except ValueError:
            print('Введіть числа!!!')
        else:
            return a, b
        
def plus(a, b):
    return a + b 

def minus(a, b):
    return a - b 

def mult(a, b):
    return a * b 

def divide(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        print('Ділити на нуль не можна!')
    else:
        return result

def main():
    a, b = get_numbers()

    oper = input('+, -, *, /: ')

    match oper:
        case '+':
            print(f'Результат: {plus(a, b)}')
        case '-':
            print(f'Результат: {minus(a, b)}')
        case '*':
            print(f'Результат: {mult(a, b)}')
        case '/':
            result = divide(a, b)

            if result:
                print(f'Результат: {result}')


main()
