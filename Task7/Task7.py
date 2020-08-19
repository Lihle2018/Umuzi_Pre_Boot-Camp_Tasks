import dis
DEGREE_SIGN =u"\u00b0"
temperature =float(input("Enter temperature: "))

def convert_to_celcius(fereignheit_temperature):
    return fereignheit_temperature*(9/5)+32

def convert_to_fereignheit(celcius_temperature):
     return (celcius_temperature -32)/(1.8)

print("Celcius to Fereignheit\n")
print(str(temperature)+DEGREE_SIGN+"C = "+str(convert_to_celcius(temperature))+DEGREE_SIGN+"F\n")

print("Fereignheit to Celcius\n")
print(str(temperature)+DEGREE_SIGN+"F = "+str(convert_to_fereignheit(temperature))+DEGREE_SIGN+"C\n")

