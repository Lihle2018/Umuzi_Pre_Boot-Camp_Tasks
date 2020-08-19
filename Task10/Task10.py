
Input =input("Enter a String: ")

def print_vowels(Input):
    vowels ="aeiouAEIOU"

    i =0
    while i<len(Input):
        for vowel in vowels:
           if Input[i]==vowel:
               print(Input[i])
        i+=1
Print_vowels(Input)
           
        
