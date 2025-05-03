
# Example for understanding dictionary , Concession stand Program

menu = { "pizza": 10.00,
         "chips": 5.00,
         "pasta": 15.00,
         "soda": 5.00,
         "tacos": 7.00}

cart = []
total = 0

print("-----Menu Items-----")

for key,value in menu.items():
    print(f" {key} : Rs.{value}")

print("---------------------")    

while True:
    food = input("Please Enter the item , select q to exits : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)   

print("--------------------")

for x in cart:
    total+=menu.get(x)
    print(x, end=" ")

print()    

print(f"The Total is Rs.{total:.2F}")

