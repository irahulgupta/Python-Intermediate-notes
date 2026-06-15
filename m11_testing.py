#===================================
# Unit Testing => unit " the smallest testable piece of code"
#==================================
#A function 
#A class Component

# def add(a,b):
#   return a+b
# def divide(a,b):
#   if b == 0:
#     return 
#   return a / b

#Unittest Framework => a built in testing library unittest 
# import unittest 
# def add(a,b):
#   return a+b

# class TestAdd(unittest.TestCase):
#   def test_addition(self):
#     self.assertEqual(add(2,3),5)

# unittest.main()

#Structure of Test Case :
# import unittest

# class MyTest(unittest.TestCase):

# #seup =>runs before every test ,  preparing data 
#   def setUp(self):
#     pass


#   def test_something(self):
#     pass

# # runs after every test , used for cleanup
#   def tearDown(self):
#     pass

#Assertion =>  Compares the expected result and the actual result 
#assertEqual (actual , expected)
#self.assertEqual(add(2,3),5)
#assestTrue => checks if the expression is true 
# self.assertTrue(5>2)
#assertFalse =>checks if the expression is False 
# self.assertTrue(5<2)
#assertRaises()=> checks whether an exception occurs 
# def divide(a,b):
#   return a/b

# with self.assertRaise(ZeroDivisionError):
#   divide(10,0)

#Debugging => Finding and fixing errors in code 
#Synatx Error
#Runtime Error => 10/0
#Logical Error => area(l,w): l+w 

#prints
#Reading error message 
# print(10/0)
#Using a debugger 
#TTD (Test-Driven Development):
#write code => test code 
#write test => write the code 
#Red , green , blue 
#1- RED =>ERROR
# def test_add(self):
#   self.assertEqual(add(2,3),5)

# #2- Green => write a simplest code of a function 
# def add(a,b):
#   return a+b

# #3- Refactor => modifying on your code 
# def add(a,b):
#   result =  a+b
#   return result 

#Loging Levels => print (very detailed information of what i am making)
# - Trace => (very detailed information 
# - DEBUG => developer information 
# - INFO => Normal application events (User LoGGED In successfully)
# - WARN => omething unusual happened , program still working 
# - Error => a series problem (Database connection failed)
# - Fatal => Critical problem => system shutdown due to critical failure 



