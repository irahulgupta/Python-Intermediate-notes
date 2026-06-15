#---------------------------------------------
#Exceptions
#----------------------------------------------
# Error => Syntax Error (Compile error), Logical(Runtime Error)
#1- Syntax Error
# print("") 

#Runtime Errors => Exception 
#input age => Marina
# number =int(input("Please enter your age : ")) 

# print(number)
# x = 5
# print(x)

#Exception try , expect , else , finally , raise 
# try :
#   # code that might through an error 
# except :
#   # a code , a message from the uer 
# try:
#   age = int(input("Please enter your age : "))
# except :
#   print ("Please enter a valid number")

# try:
#     # age = int(input("Please enter your age : "))
#     # file = open("data.txt") 
#     number = int(input("Enter a number"))
#     result = 10 / number

# except ZeroDivisionError:
#     print("We cant not divide y zero ")

# except FileNotFoundError:
#     print("This File does not exist ")
# except ValueError :
#    print ("Please enter a valid number")

#Custom Exception 
# class InvalidAgeError(Exception):
#   pass

# age = 7
# if age<18:
#   raise InvalidAgeError("Age Can not be smaller than 18")
#raise => immediately stops the current excecution and throws an exception 
# try:
#    age = int(input("Please enter your age : "))
# except InvalidAgeError:
#    print ("Please enter a valid number")

#raise keyword 

#Else :
# used only when no exception occurs 

# try:
#   x = int("10") 
# except ValueError:
#   print("Error")
# else:
#   print("Success" , x)

#Finally block => will run whenever happens 
# try:
#   x = int("10") 
# except ValueError:
#   print("Error")
# else:
#   print("Success" , x)
# finally:
#   print("Goodbye")
  
# result = "10" + "5"
# print(result)
