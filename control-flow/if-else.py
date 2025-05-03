# if else condition examples:

# example1
num = 0

if num <= 5:
    print("less that 5")
elif num == 0:
    print("zero 0")
else:
    print("greater than 5")



# example 2
age = int(input("Enter your age :"))
price = 10.00

if age > 65:
    print(" You are a Senior Citizen")
    print(f" You are a Senior citizen , you need to pay {price * 0.75}") 
elif age > 18:
    print("You are a Adult")
    print(f" You are a Adult , you need to pay {price}") 
else:
    print("You are a Child")
    print(f" You are a child , you need to pay {price * 0.5}")        
