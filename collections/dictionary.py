# Python Dictionaries

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets {}, and have keys and values (:)

#Example

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)

# way to access items in dictionary

brand = mydict.get("brand")

model = mydict["model"]

print(brand)

print(model)


# ways to access all values in dict

values = mydict.values()

print(values)


# way to get all keys

keys = mydict.keys()

print(keys)

# Add Items

mydict["color"] = "red"
print(mydict)

mydict.update({"tree": "mango"})
print(mydict)

# Way to change/update items or even add using update method:

mydict["year"] = 2018
print(mydict)

mydict.update({"year": 2020})
print(mydict)


# way to loop key and values

for x in keys:
    print(x)

# You can also use the values() method to return values of a dictionary:

for x in mydict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in mydict.keys():
  print(x)    

# The items() method will return each item in a dictionary, as tuples in a list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2018

print(x) #after the change

# way to use items()

car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

for key,value in car2.items():
   print(f" {key} : {value}")





# to remove the element by using pop, popitems, del , clear

mydict.pop("brand")

print(mydict)

mydict.popitem()

print(mydict)

del mydict["model"]
print(mydict)
 
mydict.clear()
print(mydict)   # will get you an empty dictionary

# del mydict
# print(mydict) #this will cause an error because "thisdict" no longer exists.






