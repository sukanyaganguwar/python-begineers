#This is a comment
print("Hello World")

#you can print multiple objects seperated by comma
print("Hello","Sunshine",999)

#variables are containers that can store data or values

#Identifier is the name given to entities like class functions, variables etc
# Identifiers in Python can be of any length. there is no specific length.
# Spaces are not allowed in variable names Ex: a b c = 100 200 300
# valid once example:
a,b,c = 100,200,300
print(a)
print(b)

d_h_g = 1,200,300
print(type(d_h_g)) # this is a tuple,  used to store multiple items in a single variable
print(d_h_g)
print(d_h_g[0])

abc = 1,00,000

#rules for writing identifiers
# 1. Can be combination of letters in lowercases or uppercases or digits.
#  2. cannot start with digit ex: 1abc , but abc1 is valid indentifier
#    if use assign a variable name as 1abc the you will get Syntaxerror: invalid syntax
#  3. inbuilt keywords cannot be used as identifiers.

i=99
print(i)

# type(var) : is used to check the datatype of a variable.

print(type(i))

# id() is the function which tells the location of a variable.
print(id(i))

#python is dynamic typed language means if there is a variable called "i" having have 99 then same variable can take values of different datatypes.

# now to check is it a dynamic typed i have changed the value of i from 99 to "my notes"

i = "my notes"

print(i)

# now as i is pointing to a string object it will refer to another location where the string value is stored.

print(id(i))

# now check

