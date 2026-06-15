#---------------------------------------------
#Functions
#----------------------------------------------
# Higher - Order Function (HOF)
# 1- Accepts another function as a parameter 
# 2- Returns a function as a result
# 3- or both 

# def square(num):
#   return num * num

# def cube(num):
#   return num * num * num 

# def fourth(num):
#   return num * num * num * num

# #operation is a function (square , cube)
# def operate (nums , operation):
#   for i in nums:
#     result = operation(i)
#     print(result) 

# values = [5,6,7]
# result = operate(values,square)
# def outer():
#   def inner():
#     print("Inner Function")

#   return inner

# x = outer()
# x()
#-----------------------------------------------------------

#Closures : inner function that remembers the variable of an outer function 
#1- outer , inner function 
#2- the inner function uses a variable from the outer function 
#3- return inner function 

# def outer():
#   message = "Hello"
#   def inner ():
#     print(message)

#   return inner 

# x = outer()
# x()


# numbers = []
# def enter_numer(x):
#   numbers.append(x)
#   print(numbers)

# enter_numer(3)
# enter_numer(5)
# enter_numer(7)
# enter_numer(9)
#==========================================
# def enter_number_outer():
#   numbers = []
#   def enter_number_inner(x):
#     numbers.append(x)
#     print(numbers)

#   return enter_number_inner

# enter_num = enter_number_outer()
# enter_num(3)
# enter_num(7)
# enter_num(5)
#=================================================
# def greet(name):
#   def say_hello():
#     print(f"Hello {name}")

#   return say_hello

# person1 = greet("Marina")
# person2= greet("John")

# person1()
# person2()
# =================================================
#Lambda Function :  => Anonymous Function , 1 time function 
#is a function without the (def) , there is no function name  
# lambda parameters  : implementation 
# def square (x):
#   return x*x

# sqauree = lambda x : x*x
# print(sqauree(5))

# def add(a,b):
#   return a+b

# addition = lambda a,b : a+b
# print(addition(5,5))
#=========================================================
#Recursion : ia a function it calls itself during excecution 
# def count(n):
#   print (n)
#   count(n-1)


# count(5) => 5
#count(4) => 4
# count(3)=> 3

#why recursion ?
# 1- Base Case => stopping condition without the recursion will never stop
#2- Rcursive Cae => the part when function calls itself 

#Factorial 
#5! = 5 * 4 * 3 * 2 * 1
#4! = 4 * 3 * 2 * 1

#5! = 5 * 4!
#4! = 4 *3!
#3! = 3 *2!
#2! = 2 *1!
#1! = 1 

# def factorial (n):
#   #Base Case :
#   if n == 1:
#     return 
  
#   #Recursion Case 
#   return n * factorial (n-1)








