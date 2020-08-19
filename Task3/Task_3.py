num_1 =float(input("Enter first number: "))
num_2=float(input("Enter second number: "))

def is_65(numb_1,numb_2):
    if numb_1 ==65 or numb_2==65 or (numb_1+numb_2)==65:
     return True
    else:
     return False

print(f"Is either of the numbers 65, OR is the sum of the numbers 65? {str(is_65(num_1,num_2))} \n")

