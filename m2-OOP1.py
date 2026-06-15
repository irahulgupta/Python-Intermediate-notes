#---------------------------------------------
#OOP
#----------------------------------------------
#object => attributes (data) , functions (method)"can make"
#general form , bluebrint "class" 
# class Student:
#   #method => constructor , initializer 
#   #self => refers to the current object 
#   def __init__(self , name , age = 18):
#     self.name = name 
#     self.age=age

# student1 = Student("Marina" , 23)
# print(student1.name)
# print(student1.age)

# student2 = Student("John")
# print(student2.name)
# print(student2.age)

#oop Inheritance  , polymorphism , Encapsulation , Abstraction 
#==================================================================
#Inheritance :
# class Animal :
#   def eat(self):
#     print("Animal is eating")

 
# #is a relations is dog an animal ? => yes "Inheritance"
# class Dog (Animal):
   
#    def bark(self):
#     print("Dog is barking")


# dog1 = Dog()
# dog1.eat()
# dog1.bark()


# Inheritance => allows one child to acquire the properties and methods of his parent 
# My Dad => black hair , blue eyes
# child =>black hair , blue eyes , small nose 
# Parent => attributes , methods 
# Child => attributes , methods , its own methods or attributes 
#everything from the parent class can be inherits to the child class except the constructor 
#super => help me call the constructor of parent class , because i cant inherrited
# class Person :
#   def __init__(self , name):
#     self.name=name

# class Student (Person):
#   def __init__(self,name , age):
#     super().__init__(name)
#     self.age=age

# s= Student("Marina" , 22)
# print(s.name)
# print(s.age)

#Plymorphism => Many Forms 
#overrriding , overloading functions that have the same name 
# class Animal :
#   def speak(self):
#     print("Animal is speaking")

# class Dog (Animal):
   
#   def speak(self):
#     print("Dog is barking")


# animal=Animal();
# animal.speak()
# dog = Dog()
# dog.speak()
# def add(num1 , num2){
#   return num1 +num2
# }
# def add(num1 , num2 , num3){
#   return num1+num2+num3
# }

#Encapsulation => protecting data 
# bank system 
# balance 
#Public , protected , private 
#public => can shown at any place 
# name = "Marina"
# class Student :
#   def __init__(self):
#     self.name="Marina"

# s = Student()
# print(s.name)

#protected => it can be accessed in my file but cant be accessed an any other files 
# class Student :
#   def __init__(self):
#     self._name="Marina"

# s = Student()
# print(s.name)

# private => it can't be accessed anywhere other than its class 
# class BankAccount :
#   def __init__(self):
#     self.__balance=0
  
#   def get_balance(self):
#     return self.__balance;

#   def set_balance(self , amount):
#     if amount > 0 :
#       self.__balance = amount

# #setters and getters => function made only for private members 

# myaccount = BankAccount()
# myaccount.set_balance(500);
# print(myaccount.get_balance())

#Abstraction :hide implementation details and show essential functionality 
#ATM => Insert Card , Enter pin , Withdraw 
#Abstract class => can't be instanitated => Can't make an object from it 
#99% has inheritance 
#abstract method => must be implemented in the child class 
# from abc import ABC , abstractmethod
# class Shape(ABC):
#   @abstractmethod
#   def area(self):
#     pass

# class Circle (Shape):
#   def area(self):
#     return 3.14 *5*5
# c=Circle()
# print(c.area())

#overloading in python :
# def add (num1 , num2 ):
#   print(num1+num2)


# def add (num1,num2,num3=0):
#   print(num1+num2+num3)

# add(5,6,4)

#variable length argument 
# def add (*args):
#   return sum(args)

# add1= add(1,2)
# add2 = add(1,2,4,5)
# add3 = add(4,4,9,2,4,5,3)
# print(add1)
# print(add2)
# print(add3)







