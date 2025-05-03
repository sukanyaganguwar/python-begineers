

name = input("Enter your name : ")

while name == "":
    name = input("Enter you name please: ")

age = int(input("Enter your Age:"))

while age < 0:
    print("Your Age Can't be less than 0")
    age = int(input("Enter your Age:"))

print(f"Your Name is : {name}.")
print(f"Your Age is {age} yrs old.")    
