import dis
degreeSign =u"\u00b0"
Temperature =float(input("Enter temperature in "+degreeSign+"C: "))

def ConvertTemperature(Temperature):
    return Temperature*(9/5)+32

print(str(Temperature)+degreeSign+"C = "+str(ConvertTemperature(Temperature))+degreeSign+"F\n")

