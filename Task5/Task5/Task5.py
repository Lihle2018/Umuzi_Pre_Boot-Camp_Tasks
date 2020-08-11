import math
a1=float(input("Enter side length 1: "))
b1=float(input("Enter side length 2: ")) 
c1=float(input("Enter side length 3: "))

def Area(a,b,c):
    s=0.5*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
print("\nArea = "+str(Area(a1,b1,c1)))
print()

