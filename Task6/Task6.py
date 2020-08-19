num_1 =int(input("Enter number: "))
num_2 =int(input("Enter number: "))
num_3 =int(input("enter number: "))

def get_max(num_1,num_2,num_3):
    max =num_1
    list =[num_1,num_2,num_3]
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
        return max
print("Max number : "+str(get_max(num_1,num_2,num_3)))
