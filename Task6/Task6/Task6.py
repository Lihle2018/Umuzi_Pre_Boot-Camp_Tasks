num1 =int(input("Enter number: "))
num2 =int(input("Enter number: "))
num3 =int(input("enter number: "))

def GetMax(num1,num2,num3):
    max =-999
    list =[num1,num2,num3]
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
        return max
print("Max number : "+str(GetMax(num1,num2,num3)))
