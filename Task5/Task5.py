import math
a_1=float(input("Enter side length 1: "))
b_1=float(input("Enter side length 2: ")) 
c_1=float(input("Enter side length 3: "))

def area(a,b,c):
    s=0.5*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
print("\nArea = "+str(area(a_1,b_1,c_1)))
print()

