
Input =input("Enter a String: ")

def PrintVowels(Input):
    vowels ="aeiouAEIOU"

    i =0
    while i<len(Input):
        for vowel in vowels:
           if Input[i]==vowel:
               print(Input[i])
        i+=1
PrintVowels(Input)
           
        
