def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def exponentiation(a, b):
    return a ** b

# Main calculator function
def calculator_match_case():
    print("Calculator using match-case")
    print("=" * 30)
    print("Available operations: +, -, *, /, **")
    
    try:
        first_num = float(input("Enter first number: "))
        operation = input("Enter operation: ")
        second_num = float(input("Enter second number: "))
        
        match operation:
            case '+':
                result = addition(first_num, second_num)
            case '-':
                result = subtraction(first_num, second_num)
            case '*':
                result = multiplication(first_num, second_num)
            case '/':
                result = division(first_num, second_num)
            case '**':
                result = exponentiation(first_num, second_num)
            case _:
                result = "Unknown operation!"
        
        print("Result: " + str(first_num) + " " + operation + " " + str(second_num) + " = " + str(result))
        
    except ValueError:
        print("Please enter valid numbers!")

calculator_match_case()