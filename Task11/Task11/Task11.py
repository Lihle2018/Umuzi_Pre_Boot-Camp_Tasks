str1 =input("Enter string 1: ")
str2 =input("Enter string 2: ")

def GetCommonLetters(str1,str2):
    for i in str1:
        for j in str2:
            if i==j:
                print(i)

print("Commom Letters:")
GetCommonLetters(str1,str2)