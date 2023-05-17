# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# import functools
# v='1 2 3 4'



# result=list(map(int,v.split()))
# print(result)
# map=======================>


# def hello(x):
#     return x+x
# list1=[1,2,3,4]
# output=list(map(hello,list1))
# print(output)


# output=list(map(lambda x:x>2,result))

# print(output,"----------->")

# filter------------------------->



# output=list(filter(lambda x:x>1,result))
# print(output)

# reduce----------------------->

# output2=functools.reduce(lambda x,y:x+y,result)
# print(output2)


# Decorator------------------------------>


# def called_to(func):
#     def inner():
#         print("inside inner")
#         func()
#     return inner


# def ordinary():
#     print("inside ordinary")
    
    
# result=called_to(ordinary)
# print(result())


# def smart(func):
#     def inner():
#         print("inside inner")
#         return func()
#     return(inner)
    
# @smart       
# def divide():
#     print("hi i'm ordinary")

# divide()


# generator---------------------------->

# def simple():
#     yield "this"
#     yield "that"
    
# for i in simple():
#     print(i)
# or 
# x=simple()
# print(x.__next__())
# print(x.__next__())

# iter()-------------------------------->

# x=[1,2,4]
# v=iter(x)
# print(next(v))
# print(next(v))
# print(next(v))

# inheritance---------------------------------->

# class person:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
    
#     def print(self):
#         return self.first_name + " " + self.last_name

# class employee(person):
#     def __init__(self,first_name,last_name):
#         person.__init__(self,first_name,last_name)
    
    # def print(self):
    #     return "it's from employee"
        
# obj=person('vishal','yadav')
# print(obj.print())
        
# obj=employee('vishal','yadav')
# print(obj.print())


# polymorphism----------------------------------->

# class India():
# 	def capital(self):
# 		print("New Delhi is the capital of India.")

# 	def language(self):
# 		print("Hindi is the most widely spoken language of India.")

# 	def type(self):
# 		print("India is a developing country.")

# class USA():
# 	def capital(self):
# 		print("Washington, D.C. is the capital of USA.")

# 	def language(self):
# 		print("English is the primary language of USA.")

# 	def type(self):
# 		print("USA is a developed country.")

# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
# 	country.capital()
# 	country.language()
# 	country.type()



# encapsulation


# class Base:
#     class_var=10
#     def __init__(self):
        # self._var=2   #this is protected var
#     def print_class_var(self):
#         return Base.class_var
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#     def print(self):
#         return self._var 
        
# # obj2=Base()
# # print(obj2._Base.__var)
# obj=Derived()
# print(obj.print())
# # print(obj.print_class_var())
# print(Base.class_var)

# private var

# class Base:
#     def __private_func(self):
#         return 'hi'
        
# obj=Base()
# print(obj._Base__private_func())
# print(obj._Base__var)



    
