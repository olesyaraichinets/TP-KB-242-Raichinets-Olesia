import functions
import operations
import logger


def main():
    a, b = operations.get_numbers()
    oper = operations.get_operation()

    match oper:
        case '+':
            result = functions.plus(a, b)
        case '-':
            result = functions.minus(a, b)
        case '*':
            result = functions.mult(a, b)
        case '/':
            if b != 0:
                result = functions.divide(a, b)
            else:
                print("Zero division error!")
                result = "ERROR"
        case _:
            print("Unknown operation!")
            result = "ERROR"

    print(f"Result: {result}")

    logger.write_log(a, b, oper, result)


main()
