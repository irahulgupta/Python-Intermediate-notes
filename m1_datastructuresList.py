#---------------------------------------------
#Data Structures =>  is a way of organizing and storing data in my 
#computer / system so it can be accessed and modified efficiently
#----------------------------------------------
#---------------------------------------------
#1-List => Many data 
#List is ordered , indexed "position" zero based
#Mutable => Add , delete , edit 
#list is not unique 
#different data types
#variable => box =>1 value name = "Marina"
#----------------------------------------------
# myList = ["Marina" ,26, True]
#1- append => add new one element at the end
# myList.append("John")
# myList.append("Egypt")
# myList.append(500.5)
# print(myList)

#2- extend => add multiple elemenets at end
# myList1 = ["Marina" ,26, True]
# myList2 = ["Mark", 24 , False ]
# myList1.extend(myList2)
# print(myList1)

#3-remove : more than 1 occurence , it will remove the first one only 
# myList = ["Marina" ,26, True ,"Marina"]
# myList.remove("Marina")
# print(myList)

#4-Sort => it will sort the array => only by numbers or string , reverse = true => begin with largest number 
# y = [1,2,100,4248,0,3,9]
# y.sort(reverse = True)
# print(y)

#5- clear => will not delete , no elements 
# myList = ["Marina" ,26, True ,"Marina"]
# myList.clear()
# print(myList)

#6- count : will count the occurence of a specific number
# y = [1,2,100,4248,0,3,9 , 1, 1 ,1 ,1 ,1,1 ]
# print(y.count(1))

# 7- Insert : it inserts at specific position (index) , (index,"value")
# myList = ["Marina" ,26, True ,"Marina"]
# myList.insert(2,528825)
# print(myList)

#8-pop : removes at specific index and return item at this index 
# myList = ["Marina" ,26, True ,"Marina"]
# print(myList.pop(-1))

#List Comprehensions => a shorter way of creating a list listname = [value for(range) if]
# squares =[]
# for i in range(5):
#   squares.append(i**2)

# print(squares)
# 0 1 2 3 4 
# 0 1 4 9 16
# squares =[i**2 for i in range (5)]
# print(squares)

#even values if (i % 2 == 0)=> even numbers
# 0 ->10 
# even =[]
# for i in range (10):
#   if i % 2 == 0:
#     even.append(i)
# print(even)
# even =[i for i in range(11) if i%2==0]
# print(even)