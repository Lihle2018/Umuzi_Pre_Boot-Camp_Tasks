
num =int(input("Enter number"))

def get_multiples(number):
    i=0
    x=0
    while i<number:
        if i%3==0 or i%5==0:
            x+=i
        i+=1
    return x
print("\nSum of all mltiples of 3 or 5 below "+str(num)+" = "+str(get_multiples(num)))
print()

