str_1 =input("Enter string 1: ")
str_2 =input("Enter string 2: ")

def get_common_letters(str1,str2):
    for i in str1:
        for j in str2:
            if i==j:
                print(i)

print("Commom Letters:")
get_common_letters(str_1,str_2)