# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


def msg():
    print("Hello, Good Morning!")

msg()  

# Return Function

def add (a,b):
    z=a+b
    return z;

print(add(1,3))

def name(fname, lname):
    first_name = fname.capitalize()
    last_name = lname.capitalize()
    return first_name + " " + lname

full_name = name("Sukanya", "Ganguwar")

print(full_name)

#Default Args(Default Parameter Value)

# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value

def net_price(list_price,  discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500,0.01))

# Note for default arguments

# def count_time(start_time=0,  end_time):   #if you write like this you will get error Non-default argument follows default argument,
#                                            # so you default arguments should be at last
#     return start_time + end_time


# print(count_time(500))



# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:

def mypositional_function(x, /):
  print(x)

mypositional_function(3)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments

def keyword_function(*, x):
  print(x)

keyword_function(x = 3)
