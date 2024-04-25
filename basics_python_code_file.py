#traditional way of starting any language intro==================>

# print("Hello World")

#user input 

#simple
# num = input("Enter a int number\n")

#complex but simple===================>

# num:int = int(input("Enter a int number\n"))
# print(type(num),end='\n')
# print(num,end='\n')

# var define==================>

# x = 10   #yes it dynamic

# print(type(x))

# name = "Python3"

# print(type(name))

##Topic#1 Control flow===========================================>

# Conditional Statements:=========================================>

# x = 10

# if x > 0:
#     print("x is positive")
# elif x == 0:
#     print("x is zero")
# else:
#     print("x is negative")

# to make it interesting

# x=10

# print("x is positive" if x>0 else ("x is zero" if x ==0 else "x is negative"))

#Loops==============================================>

# For Loop:=======================================================>

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# iterate using index

# for i in range(0, len(fruits)):
#     print(fruits[i])


#while loop=======================================================>

# while condition:
    # opertion
    # increment so that loop further

# i = 1

# while i <= 5:
#     print(i)
#     i += 1

#Break statement==================================================>

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)
#     break

#output : #break after apple

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)

#Continue statement:=============================================>

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)


# Topic#2 Data types :===========================================>


#Numbers--->1. Integer 2.Floating-point (float) 3. Complex

# 1. integer

# x=10
# print(x)

# 2. floating-point

# x=121321.342
# print(x)

#3. complex

# j=2

# this complex number

# z1 = 3 + 2j
# z2 = -1.5 - 0.5j


#this is int and float
# z1 = 3 + 2*j
# z2 = -1.5 - 0.5*j

# print(type(z1),type(z2),sep='\t')


# another way to write it complex(real num, imaginary num)
# z1 = 3 + 4j
# z2 = complex(2, -5)  # Using the complex() function

# Print the complex numbers
# print("z1:", z1)
# print("z2:", z2)

# print(z1.real)
# print(z1.imag)
# print(z2.real)
# print(z2.imag)

# print(z1.conjugate()) # change the sign + to - or vice
# print(abs(z2))

#Python Dictionary :============================================>

#Creating a Dictionary:====================================>

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# print(my_dict)

#empty dict

# can_say_obj = dict()
# print(can_say_obj)


# Accessing Values:========================================>

# print(my_dict['name'])

# or 

# print(my_dict.get('name'))
# print(my_dict.get('key_ni_h','default_wala_value'))

# Modifying Values:

# my_dict['age'] = 35
# print(my_dict)

# Adding New Key-Value Pairs:

# my_dict['gender'] = 'Male'
# print(my_dict)

# Removing Key-Value Pairs:

# del my_dict['city']
# print(my_dict)

# Dictionary Methods:

# keys(), values(), items(), get(), update(), clear()

# print(my_dict.keys())     # Output: dict_keys(['name', 'age', 'gender'])
# print(my_dict.values())   # Output: dict_values(['John', 35, 'Male'])


#Dictionary Comprehension:

# squares = {x: x*x for x in range(1, 6)}

# print(squares)

# Nested Dictionaries: #Not included in baiscs topic

# employee = {'name': 'John', 'details': {'age': 30, 'position': 'Manager'}}



# Boolean Values: =================================================>

# x = True
# x = False
# y = False

#Usage in Conditional Statements :

# if x:
#     print("x is true")
# else:
#     print("x is false")

# Logical Operators:   #can relate with logic gate and or not

# a = True
# b = False

# # Logical AND
# result_and = a and b  # Result: False

# # Logical OR
# result_or = a or b  # Result: True

# # Logical NOT
# result_not = not a  # Result: False


# print(result_and, result_or, result_not, sep="\t")


# Comparison Operators:


# ==, !=, <, >, <=, >=


# what_say = 1>2
# what_say = 1<2
# what_say = 1==2
# what_say = 1!=2
# what_say = 1<=2
# what_say = 1>=2

# print(what_say)

# Python Set:======================================================>

# Creating a Set:


# my_set = {1, 2, 3, 4, 5}

# print(my_set)

# Creating an Empty Set:

# empty_set = set()

# print(empty_set)


# Adding Elements to a Set:

# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)

# Removing Elements from a Set:

# my_set = {1, 2, 4, 5}
# my_set.remove(3)  #raise error when element not present 
# my_set.discard(3) #ignores and no error raise
# print(my_set)

# Set Operations:================================================>

# union (|), intersection (&), difference (-), and symmetric difference (^).

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# union_set = set1 | set2             # Union
# intersection_set = set1 & set2      # Intersection
# difference_set = set1 - set2        # Difference
# symmetric_difference_set = set1 ^ set2  # Symmetric Difference


# print("::::: printing Union :::::")
# print(union_set)

# print("::::: printing Intersection :::::")
# print(intersection_set)


# print("::::: printing Difference :::::")
# print(difference_set)

# print("::::: printing Symmetric Differenec :::::")
# print(symmetric_difference_set)

# Set Methods:

# union(), intersection(), difference(), symmetric_difference(), add(), remove(), discard(), pop(), clear()

# Type Casting:======================================================>


# Integer to Float Conversion:

# integer_number = 10
# float_number = float(integer_number)
# print(type(float_number))
# print(float_number)  # Output: 10.0

# Float to Integer Conversion:

# float_number = 10.5
# integer_number = int(float_number)
# print(type(integer_number))
# print(integer_number)  # Output: 10

# String to Integer/Float Conversion:

# str_integer = "123"
# int_number = int(str_integer)
# print(type(int_number))
# print(int_number)  # Output: 123

# str_float = "3.14"
# float_number = float(str_float)
# print(type(float_number))  # Output: 3.14
# print(float_number)  # Output: 3.14

# Integer/Float to String Conversion:

# integer_number = 123
# str_integer = str(integer_number)
# print(type(str_integer))
# print(str_integer)  # Output: "123"

# float_number = 3.14
# str_float = str(float_number)
# print(type(str_float)) 
# print(str_float)  # Output: "3.14"

# String to List Conversion:

# my_string = "hello"
# char_list = list(my_string)
# print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# List to String Conversion:

# char_list = ['h', 'e', 'l', 'l', 'o']
# my_string = ''.join(char_list)
# print(my_string)  # Output: "hello"

# String===================================================>

# Immutable

# my_string = 'Hello'
# # This will raise an error
# my_string[0] = 'h'

# Indexing and Slicing:

# my_string = 'Python'
# print(my_string[0])  # Output: 'P'
# print(my_string[2:5])  # Output: 'tho'

# Concatenation:

# first_name = 'John'
# last_name = 'Doe'
# full_name = first_name + ' ' + last_name
# print(full_name)  # Output: 'John Doe'

# String Methods:

# my_string = '  Hello, world!  '
# print(my_string.strip())  # Output: 'Hello, world!'
# print(my_string.upper())  # Output: '  HELLO, WORLD!  '

# Formatted Strings:

# name = 'Alice'
# age = 30
# print(f'My name is {name} and I am {age} years old.')  # Output: 'My name is Alice and I am 30 years old.'


# and way to do this is 

# # Basic usage
# template = "Hello, {}!"
# formatted_string = template.format("world")
# print(formatted_string)  # Output: Hello, world!

# # Using multiple placeholders
# template = "Hello, {}! Today is {}."
# formatted_string = template.format("John", "Monday")
# print(formatted_string)  # Output: Hello, John! Today is Monday.

# # Using named placeholders
# template = "Hello, {name}! Your age is {age}."
# formatted_string = template.format(name="Alice", age=30)
# print(formatted_string)  # Output: Hello, Alice! Your age is 30.


# String Operations:

# my_string = 'Python'
# print(len(my_string))  # Output: 6
# print('Py' in my_string)  # Output: True


# Python List:===============================================>

#empty list

# empty_list = []

# Accessing Elements:

# my_list = [1, 2, 3, 4, 5]

# print(my_list[0])  # Output: 1


# Slicing:

# my_list = [1, 2, 3, 4, 5]

# print(my_list[1:4])  # Output: [2, 3, 4]


# Modifying Elements:

# my_list = [1, 2, 3, 4, 5]

# my_list[2] = 10

# Adding Elements:

# my_list = [1, 2, 3, 4, 5]

# my_list.append(6)

# Removing Elements:

# my_list = [1, 2, 3, 4, 5]

# my_list.remove(3)

# List Methods:

# my_list = [1, 2, 3, 4, 5]

# my_list.sort()

# List Comprehension:

# squares = [x**2 for x in range(1, 6)]

# # Nested Lists:

# matrix = [[i + j for j in range(3)] for i in range(3)]

# print(matrix)

# Output:

# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]


##Important ============================================>

# lambda===============================================>

# syntax

# lambda arguments: expression

# def double(x):
#     return x * 2

# double = lambda x: x * 2


# print(double(2))

# map() Function:==============================================>

# Syntax: map(function, iterable)

# def double(x):
#     return x * 2

# numbers = [1, 2, 3, 4, 5]

# doubled_numbers = map(double, numbers)

# print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# filter() Function:=============================================>

# Syntax: filter(function, iterable)

# # Define a function to filter even numbers
# def is_even(x):
#     return x % 2 == 0

# # Filter even numbers from the list using filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]


# reduce() Function:============================>


# # Syntax: functools.reduce(function, iterable[, initializer])

# # Example (with functools.reduce()):

# from functools import reduce

# # Define a function to sum numbers
# def add(x, y):
#     return x + y

# # Reduce the list to find the sum of all elements
# numbers = [1, 2, 3, 4, 5]
# sum_of_numbers = reduce(add, numbers)
# print(sum_of_numbers)  # Output: 15


# Now usage of lambda with map and filter:


# # With map() function:

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = map(lambda x: x * 2, numbers)
# print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# # With filter() function:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Python Tuples:===============================================>

# Creating a Tuple:

# my_tuple = (1, 2, 3, 4, 5)

# empty tuple 

# empty = tuple()
# print(empty)

# Accessing Elements:

# my_tuple = (1, 2, 3, 4, 5)

# print(my_tuple[0])  # Output: 1


# Slicing:
# [start:stop:step]

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1:4])  # Output: (2, 3, 4)

# Immutable Nature:

# my_tuple = (1, 2, 3, 4, 5)

# my_tuple[0] = 10  # This will raise an error

# Tuple Packing and Unpacking:

# my_packed_tuple = 1, 2, 3
# a, b, c = my_packed_tuple
# print(a, b, c)  # Output: 1 2 3

# Single-element Tuple:

# # single_element_tuple = (1) #type returns int
# single_element_tuple = (1,) #add comma after element return tuple type
# print(type(single_element_tuple))
# print(single_element_tuple)

# Tuple Methods:

# count() and index().

# my_tuple = (1, 2, 2, 3, 4, 4, 4)
# print(my_tuple.count(2))  # Output: 2


# Topic#3 Function=========================================>

# # Example: Defining a Function
# def greet():
#     print("Hello, World!")

# # Calling the function
# greet()


# # Function Parameters:

# # Example: Function with Parameters
# def greet(name):
#     print("Hello,", name)

# # Calling the function with an argument
# greet("Alice")


# # Return Statement:

# # Example: Function with Return Statement
# def add(x, y):
#     return x + y

# # Calling the function and storing the result
# result = add(3, 5)
# print("Result:", result)

# # Default Parameters:

# # Example: Function with Default Parameters
# def greet(name="World"):
#     print("Hello,", name)

# # Calling the function with and without an argument
# greet()  # Output: Hello, World
# greet("Alice")  # Output: Hello, Alice


# Define a global variable
# global_var = 10

# def my_function():
#     # Access the global variable
#     print("Inside my_function:", global_var)

# # # Access the global variable outside the function
# # print("Outside my_function:", global_var)

# # # Modify the global variable
# global_var = 20
# print("Modified global_var:", global_var)

# # Call the function
# my_function()



# Topic#4 File Handling:==============================================>


# # Opening and Closing Files:

# file = open("example.txt", "r")  # Open file for reading
# # Perform operations on the file
# file.close()  # Close the file when done


# Reading from Files:
# You can read data from a file using various methods like read(), readline(), or readlines().

# # Example: Reading from Files
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Writing to Files:
# You can write data to a file using the write() method.

# # Example: Writing to Files  ### this write rewrite the content this new content
# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a test file.")



# Appending to Files

# with open("example.txt", "a") as file:
#     file.write("\nThis text is appended to the file.")


# # Iterating Over Lines in a File:

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Strip newline characters from each line



# Topic#5 Exception Handling:=========================================>


# Basic Exception Handling:

# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

# # Handling Multiple Exceptions:

# try:
#     result = int("hello")  # This will raise a ValueError
# except ValueError:
#     print("Error: Invalid conversion to integer")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")




#Handling Any Exception
# try:
#     result = 10 / 0
# except:
#     print("An error occurred")


# else Block

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# else:
#     print("Result:", result)

# The finally Block:

# try:
#     file = open("example.txt", "r")
#     # Perform file operations
# except FileNotFoundError:
#     print("Error: File not found")
# finally:
#     file.close()  # Close the file regardless of whether an exception occurred


# Topic#6 Class ==================================================>


# # Example: Defining a Class

# class MyClass:  #first letter of class name should be capital according to python
#     # Class attribute
#     class_variable = "Hello, World!"

#     # Constructor method (initialization)
#     def __init__(self, name):
#         self.name = name  # Instance attribute

#     # Instance method
#     def greet(self):
#         print("Hello,", self.name)

# # Example: Creating Objects (Instances)

# obj1 = MyClass("Alice")
# obj2 = MyClass("Bob")

# # Example: Accessing Attributes and Calling Methods

# print(obj1.name)  # Accessing instance attribute
# obj1.greet()      # Calling instance method

# print(obj2.class_variable)  # Accessing class attribute
# obj2.greet()                # Calling instance method




# Topic#7 OOPS:=====================================================>

# Note :
# # always remember constructor inside the class are called before any other method inside the class

# class Car:
#     # Class variable
#     num_cars = 0
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         # Increment the class variable when a new instance is created
#         Car.num_cars += 1
#         print("Hi first come to me...")
        
#     def get_car_brand(self,):
#         return f'{self.model} is of brand {self.brand}'

# # Create instances of the Car class
# car1 = Car("Toyota", "Corolla")
# car2 = Car("Honda", "Civic")

# # Access the class variable
# # print("Number of cars:", Car.num_cars)  # Output: 2


# let that constructor get called first....
# print(car1.get_car_brand())
# print(car1.brand)




# class Person:
#     # name, age, and occupation are attributes or instance variables of the Person class.
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#         # self.name, self.age, and self.occupation are specific instances of these attributes associated with each individual instance of the Person class.

#     def describe(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Occupation: {self.occupation}")

#     def update_age(self, new_age):
#         if new_age >= 0:
#             self.age = new_age
#         else:
#             print("Age cannot be negative.")

#     def is_eligible_to_vote(self):
#         return self.age >= 18


# class Student(Person):
#     def __init__(self, name, age, occupation, student_id):
#         super().__init__(name, age, occupation)
#         self.student_id = student_id

#     def describe(self):  # Method overriding
#         super().describe()
#         print(f"Student ID: {self.student_id}")


# # Create instances of the Person and Student classes
# person1 = Person("Alice", 25, "Engineer")
# student1 = Student("Bob", 20, "Student", "S12345")

# # Describe the persons and student
# print("Person 1:")
# person1.describe()
# print("\nStudent 1:")
# student1.describe()

# # Check if objects are instances of their respective classes
# print("\nIs person1 an instance of Person?", isinstance(person1, Person))
# print("Is student1 an instance of Student?", isinstance(student1, Student))

# # Check if objects are instances of the superclass
# print("\nIs student1 an instance of Person?", isinstance(student1, Person))

# # Check polymorphism - both objects have describe method
# print("\nCalling describe method on person1:")
# person1.describe()
# print("\nCalling describe method on student1:")
# student1.describe()


#Class variable ==============================================>

# class Car:
#     # Class variable
#     num_cars = 0
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         # Increment the class variable when a new instance is created
#         Car.num_cars += 1

# # Create instances of the Car class
# car1 = Car("Toyota", "Corolla")
# car2 = Car("Honda", "Civic")

# # Access the class variable
# print("Number of cars:", Car.num_cars)  # Output: 2



#Private variable and Private function================================>

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # Private variable
#         self.__age = age    # Private variable
    
#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     #private method 
#     def __check_person(self):
#         return f'name : {self.__name} and age : {self.__age}'
    
#     #let use private method inside class
#     def person_info(self):
#         return self.__check_person()

# # Creating an instance of the Person class
# person = Person("Alice", 30)

# Attempting to access private variables directly
# This will raise an AttributeError
# print(person.__name)
# print(person.__age)

# Accessing private variables through getter methods
# print("Name:", person.get_name())  # Output: Name: Alice
# print("Age:", person.get_age())    # Output: Age: 30


# Private variables are kind of myth here

# Accessing private variables using the class name
# name = person._Person__name
# age = person._Person__age

# print("Name:", name)  # Output: Name: Alice
# print("Age:", age)    # Output: Age: 30


#using private function output in public function
# print(person.person_info())  #using public method
# print(person.__check_person()) # AttributeError

#instead use

# print(Person._Person__check_person(person)) 
# print(person._Person__check_person())

