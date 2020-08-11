num1 =float(input("Enter first number: "))
num2 =float(input("Enter second number: "))

def Contains3(num1,num2):
    if (num1==3 or num2==3) and str(num1+num2).find("3"):
        return True
    else:
        return False

print("Is either of the number 3 and the sum of the number contains 3 ? "+str(Contains3(num1,num2)))
