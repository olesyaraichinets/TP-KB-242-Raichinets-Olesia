import functions
import operations

print("CALCULATOR ")
print("Enter 'q' at any time to quit\n")

while True:
    a = operations.getNumber("Enter the first number or 'q' to quit: \n")
    if a == 'Q' or a == 'q':
        operations.log('q')
        print("You have left the program")
        break
    
    b = operations.getNumber("Enter the second number or 'q' to quit: \n")
    if b == 'Q' or b == 'q':
        operations.log('q')
        print("You have left the program")
        break
    
    op = operations.getOperations("Choose an operation (+, -, *, /) or 'q' to quit: \n")
    if op == 'Q' or op == 'q':
        operations.log('q')
        print("You have left the program")
        break
    
    if op == '+':
        result = functions.plus(a, b)
        operations.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '-':
        result = functions.minus(a, b)
        operations.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '*':
        result = functions.multiply(a, b)
        operations.log(a, b, op, result)
        print(f"Answer: {result}")
    elif op == '/':
        result = functions.divide(a, b)
        operations.log(a, b, op, result)
        print(f"Answer: {result}")
    
    print("-" * 30)