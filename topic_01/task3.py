import math

def discr(a, b, c):
    return b*b - 4*a*c   

a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))

D = discr(a, b, c)
print("Discriminant =", D)

if D < 0:
    print("No result")
elif D == 0:
    x = -b / (2*a)
    print("One:", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Two:", x1, "и", x2)