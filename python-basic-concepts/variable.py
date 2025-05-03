#VARIABLE

# Python is a dynamically-typed language. This means that we do not declare the types of variables.
# There are also no const or var qualifiers; it is not possible to declare a variable as “constant”.

a=1 
b=2 

#In Python, an assignment doesn’t create a copy of the value being assigned, but instead creates a reference to the value.

a=b 

# what does this means. In Python, when you assign a value to a variable, you are not creating a copy of the value.
#  Instead, you are creating a reference to the value in memory. 
# This means that the variable points to the location in memory where the actual value is stored. 

#1. Assignment Example:

a = [1, 2, 3]
b = a
# In this example:

# a is a variable that references a list [1, 2, 3].
# When you assign a to b, b now references the same list that a references. No new list is created; both a and b point to the same list in memory.

# 2. Implications of Reference Assignment:

# Since a and b reference the same list, any changes made to the list via one variable will be reflected when accessed through the other variable.

b.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]

# Here, appending 4 to b also affects a because they both reference the same list.

# 3. Creating Copies:

# If you want to create a separate copy of the list (so changes to one don’t affect the other), you need to explicitly create a copy:

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3, 4]

# Now a and b reference different lists, so changes to b do not affect a.

# Understanding this concept is crucial for managing mutable data types (like lists and dictionaries) in Python, as it affects how changes to one variable can impact others.

# also how to check reference of variable

print(a is b)

# also you can use id function for that.

print(id(a))
