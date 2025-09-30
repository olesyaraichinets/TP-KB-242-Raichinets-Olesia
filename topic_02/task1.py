def calculate_discriminant(a, b, c):
    """Calculate discriminant of quadratic equation"""
    return b**2 - 4*a*c

def solve_quadratic_equation(a, b, c):
    """Find roots of quadratic equation using discriminant"""
    d = calculate_discriminant(a, b, c)
    
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return "Two real roots: x1 = " + str(round(x1, 2)) + ", x2 = " + str(round(x2, 2))
    elif d == 0:
        x = -b / (2*a)
        return "One real root: x = " + str(round(x, 2))
    else:
        return "No real roots"

# Main execution
print("Quadratic Equation Solver")
print("=" * 30)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve_quadratic_equation(a, b, c)
print("Result: " + result)