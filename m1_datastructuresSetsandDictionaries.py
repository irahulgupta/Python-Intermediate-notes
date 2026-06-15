#---------------------------------------------
#Data Structures =>  is a way of organizing and storing data in my 
#computer / system so it can be accessed and modified efficiently
#----------------------------------------------
#---------------------------------------------
#Dictionary , Set {}
#Dictionary => key "Unique , duplicates are not allowed", value 
# user = {
#   "name" : "John",
#   "age" : 25,
#   "grades" : [90,95,100],
#   "friends":{
#     "name1" : "Marina",
#     "name2" : "Maria"
#   }
# }
# print(user)

#creating a dictionary : 
# user = {}
# user = dict()

# user = {
#   "name" : "John",
#   "age" : 25,
#   "grades" : [90,95,100],
# }
# print(user["name"])

#get 
# print(user.get("name"))

#Operations:
# add new element
# user["Attendence"]=True
# print(user)

#remove => pop , del 
# age = user.pop("age")
# print(age)
# print(user)

# del user["age"]
# print(user)

#Iterate through the dictions 
#keys
#values
#keys, value
# user = {
#   "name" : "John",
#   "age" : 25,
#   "grades" : [90,95,100],
# }
# for key in user:
#   print(key)

# for value in user.values():
#   print(value)

# for key,value in user.items():
#   print(key,value)
#-----------------------------------------------
#Set {}
#unordered collection => has no indexed , no slicing , has no duplicates
set = {"Marina" , 23 , True , 500.263 }
# print(set)

#clear 
#union | , union
# b ={"one" , "two" , "three"}
# c= {"1" , "2" , "3"}
# print(b|c)
# print(b.union(c))

#intersection => common elements
# a={1,2,3,4}
# b ={3,4,5,6}
# print(a & b)

#difference => elements in one set not in the other set 
# #print(a-b)
# print(b-a)

# add => add new element 
# a={1,2,3,4}
# a.add(5)
# print(a)

#pop 
# print(a.pop())
# print(a)
