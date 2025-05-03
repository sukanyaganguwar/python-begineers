# list comprehension = A concise way to create lists in Python. 
# Compact and easier to read than traditional for loops.
# It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering items based on a condition. 

list1 = [1, 2, 3, 4, 5]
list2 =[x for x in list1 if x%2==0]
print("List comprehension:", list2)     
# Create a list of squares for numbers from 1 to 10

squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)

# Create a list of tuples (number, square) for numbers from 1 to 5
number_square_pairs = [(x, x**2) for x in range(1, 6)]
print("Number-Square pairs:", number_square_pairs)

# Flatten a 2D list into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatt = [row for row in matrix]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flatt)
print("Flattened list:", flattened)
