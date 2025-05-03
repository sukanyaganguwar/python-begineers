# class variables = Shared among all instances of a class
#                    Defined within the class but outside any methods
#                    Allow you to share data among all objects created from the class
#                    Can be accessed using the class name or the instance name
#                    Can be modified using the class name or the instance name
#                    Should be used for constants or shared data

# instance variables = Unique to each instance of a class


class Student:
    # Class variable
    class_year = 2025  # Shared among all instances of the class

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Year: {Student.class_year}")


student1 = Student("Alice", 20)

print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20  
print(student1.class_year)  # Output: 2025 (class variable)
student1.display_info()  # Output: Name: Alice, Age: 20, School: None


# Note : we can access class variable using instance name or class name
# print(Student.class_year)  # Output: 2025 ( accessing class variable using class name)
# print(student1.class_year)  # Output: 2025 ( accessing class variable using instance name)
# but the best practice is to use class name to access class variable 
