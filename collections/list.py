# LIST : 
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets []
# List items are ordered, changeable, and allow duplicate values.

#Examples of List

fruits = ["apple", "banana","coconut", "grapes"]

print(fruits)

print(fruits[0])

print(fruits[0:2])

print(fruits[0:3])

print(fruits[::3])    # it means same like 0 to 3 [0:3]

fruits[0]="guava"

for fruit in fruits:
    print(fruit , end=" ")

print()

#List Length
#To determine how many items a list has, use the len() function:
print(len(fruits))

# List APPEND METHOD
fruits.append("Strawberry")

for fruit in fruits:
    print(fruit , end=" ")

print()

# List REMOVE METHOD
fruits.remove("Strawberry")

for fruit in fruits:
    print(fruit , end=" ")

print()    

# List POP METHOD
fruits.pop(0)
fruits.append("Strawberry")

for fruit in fruits:
    print(fruit , end=" ")

print() 

# List CLEAR METHOD
#fruits.clear()

fruits.sort()
fruits.append("Strawberry")

for fruit in fruits:
    print(fruit , end=" ")

print()     

# List SORT METHOD
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)    

print()    

# List SORT REVERSE METHOD
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print()    

# List COPY METHOD
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print()

#JOIN TWO LIST EXAMPLES BELOW:

# 1st way to join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print()

# 2nd way to join list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print()

# OTHER METHODS USED IN GENERAL IN PYTHON FOR ASSISTANCE
print(dir(fruits))
print(help(fruits))
print(len(fruits))
