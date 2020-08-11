num1 =float(input("Enter first number: "))
num2=float(input("Enter second number: "))

def Is_65(numb1,numb2):
    if numb1 ==65 or numb2==65 or (numb1+numb2)==65:
     return True
    else:
     return False
is_65=Is_65(num1,num2)
print("Is either of the numbers 65, OR is the sum of the numbers 65? "+str(is_65))

