num =int(input("Enter a number: "))

def convert(number):
    hours=number//60
    min=number%60

    print(f"{hours} hour(s):{min} min\n")
print()
convert(num)

    
