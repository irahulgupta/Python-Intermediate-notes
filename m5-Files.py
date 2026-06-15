#---------------------------------------------
#File Handling 
#----------------------------------------------
name = "Marina"
age = 20
#stored in Ram => stored in a File "Permenantly"
# Text Files(.txt , .csv , .json , .xml) and Binary Files (.jpg , . png , .mp3 , mp4) "Pixel => 010101010"
# Handle Files , csv , json , xml 
#1- open ("The file " , "mode")
#2- mode => r , w , a , r+

# Open -> Read/Write -> Close 
# file = open ("data.txt" ,"w")
#1 - read => read()"Entire File" , readline()"reads one line" , readlines() "reads the entire lines put into a list "
# file = open ("data.txt" ,"r")
# content = file.read()
# print(content)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# lines = file.readlines()
# print(lines)

# 2 - writing => write() , writelines()
# file = open("data.txt" , "a")
# file.write("Hello World !!")
# file.write("it is Python!")
# file.write("it is Java!")
# file.close()
# lines =[
#   "Python \n"
#   "Java \n"
#   "C++ \n"
# ]
# file.writelines(lines)
# file.close()
with open("data.txt" , "a") as file:
  file.write("This a new line")

# Hidden Cursor => File Pointer 
# tell()
# file = open("data.txt")
# print(file.tell())

# file.read(5)
# print(file.tell())
#seek() => moves the pointer
# file.seek(0)
# print(file.tell())

#- Csv (Comma-Separated Values)
# used for table 

# with open ("students.csv" , "r") as file:
#   reader = csv.read(file)

# for row in reader:
#   print(row)

# import csv 
# with open("students.csv" , "w", newline="") as file:
#   writer = csv.writer(file)
#   writer.writerows([
#     ["Name","Age"],
#     ["Marina","27"],
#     ["John","20"],
#     ["Maria","45"],

#   ])

# with open ("students.csv" , "r") as file:
#   reader = csv.reader(file)
#   for row in reader:
#     print(row)

#======================================================
#JSON => Javascript object Notation APIS AND WEB DEVELOPMENT

# {
#   "name" : "Marina",
#   "age" : 25,
#   "city" : "Egypt" 
# }
# import json 
# data = {
#   "name" :"Marina",
#   "age" :25
# }

# with open ("user.json" ,"w") as file:
#   json.dump(data,file,indent=4)

# with open ("user.json" ,"r") as file:
#   data = json.load(file)
# print(data)

#json.dump => it converts a python object into jon and writes it directly tol a file 
#Dictionary -> JSON-> Save it in a file 

#XML => Extensible Markup Language 
#used tags like html 
# <html>
#   <student>
#     <name>Marina</name>
#     <age>25</age>
#   </student>
# </html>


# file = open("data.txt")
# file.close()
#Context Managers 
# with open ("data.txt") as file:
#   x=10/0
# close the file safely  , automatic cleanup

# import zipfile 
#Extract a zip file 
# with zipfile.ZipFile("archive.zip" , "r") as zip:
#   zip.extractall()

#open zip => extract files => restore original data 

#creating a zip file
# with zipfile.ZipFile("archive.zip" , "w" , zip.ZIP.DEFLATED) as zip:
#   zip.write("data.txt")

#create zip => add files => compress 

