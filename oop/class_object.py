# Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class

#Example
#Create a class named MyClass, with a property named x and a method named print x 

class MyClass:
    x = 5

p1 = MyClass()   # Create an object of MyClass
print(p1.x)   # Print the value of x

# __init_() Function
# The __init__() function is a special method that is automatically called when an object is created.
# It is used to initialize the attributes of the object.    
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:



class Car:
    def __init__(self, brand, model, dyear, for_sale):
        self.brand = brand
        self.model = model
        self.year = dyear   # Assigning 'dyear' to an attribute named 'year'
        self.for_sale = for_sale
        self.color = "red"
        # self is a reference to the current instance of the class, and is used to access variables that belong to the class.
        # It must be the first parameter of any function in the class
        # The __init__() function is called automatically every time the class is being used to create a new object.

c1 = Car("Ford","Mustang", 1964, True)

print("Brand:", c1.brand)
print("Model: {} , Color : {}".format(c1.model, c1.color))
print("Year: {} , For Sale : {}".format(c1.year, c1.for_sale))
print("Car object:", c1) # Print the object itself
print("Car object:", c1.__dict__)  # Print all attributes of the object
print("Car object:", c1.__class__)  # Print the class of the object
print("Car object:", c1.__class__.__name__)  # Print the name of the class
print("Car object:", c1.__class__.__module__)  # Print the module of the class

#output
# Brand: Ford
# Model: Mustang , Color : red
# Year: 1964 , For Sale : True
# Car object: <__main__.Car object at 0x7f8c8c2d3b50>       # Print the object itself
# Car object: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'for_sale': True, 'color': 'red'}  # Print all attributes of the object
# Car object: <class '__main__.Car'>  # Print the class of the object
# Car object: Car  # Print the name of the class
# Car object: __main__  # Print the module of the class
# Car object: __main__.Car  # Print the qualified name of the class   

