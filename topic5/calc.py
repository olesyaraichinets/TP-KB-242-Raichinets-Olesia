import functions
import operations


def main():
    a, b = operations.get_numbers()
    oper = operations.get_operation()

    match oper:
        case '+':
            print(f'Resulf: {functions.plus(a, b)}') 
        case '-':
            print(f'Result: {functions.minus(a, b)}')
        case '*':
            print(f'Result: {functions.mult(a, b)}')
        case '/':
            if b != 0:
                print(f'Result: {functions.minus(a, b)}')
            else:
                print('Zero division error!')
        case '_':
            print('Unknown operation!')


main()
