num_1 =float(input("Enter first number: "))
num_2 =float(input("Enter second number: "))

def contains_3(num_1,num_2):
    sum=num_1+num_2
    if (num_1==3) or (num_2==3) and find(f"{sum}","3"):
          return True
    else:
          return False;
          
def find(collection,value): #Checks if value is contained in a collection
    return value in collection
       
print(f"Is either of the number 3 and the sum of the number contains 3 ? "+str(contains_3(num_1,num_2)))
