def shipping(*args,**kwargs):
    print(type(args))      # This is of type tuple
    print(type(kwargs))    # This is of type dict

    for arg in args:
        print(arg)
    print()


    for key, value in kwargs.items():    
      print(f"{key} : {value}")

    for key in kwargs.keys():
       print(f"{key}")    

    for value in kwargs.values():
       print(f"{value}")   

    if kwargs.get("fname") == "John":
       print("Key is Present")


shipping("abr", "adb", "dce", fname="John",lname="Brad")    

def func_key(*args,**kwargs):
   print(f"{kwargs['hello']} {kwargs['title']}{kwargs['fname']} {kwargs['lname']}")

func_key(hello="Hello",title="Ms.",fname="Sukanya",lname="Ganguwar") 


# Notes on functions:
# *args --> allows you to pass multiple on-key arguments.
# **Kwargs --> allows you to pass multiple keyword-arguments.

#  * --> here astriek is considered as unpacking operator
# Types of function parameters  1. positional 2. default 3.Keyword 4.Arbitrary 
