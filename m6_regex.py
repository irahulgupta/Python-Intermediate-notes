#---------------------------------------------
#Regex
#----------------------------------------------
#regex => marina#gmail.com => @
#password 
# regex => a special language used to search for "patterns" inside a text 
# text ="My phone number 9876543210"
# for char in text :
#   if char.isdigit():
#     print(char)

# import re
# regex =re.findall(r"\d",text)
# print(regex)

import re

#1- Literal Charcater =>  a normal character matches itself 
# text = "Python is powerful . Python is easy"
# result = re.findall("Python" , text)
# print(result)

#2- Meta Characters => has a special meaning 
# . => any character 
# \d => the digits 
# \w => letter , digit , _
# \s => space
# ^ => Start of the string 
#$ => end of a string 
# * => zero or more  a* => "" a aa aaa aaaaa 
# + => one or more a+ => a aa aaa
# ? =>optional 

#3- Character Classes => allow matching a group of characters 
# [a-z] [A-Z] [0-9] [A-Za-z0-9] 

# result = re.findall(r"\d" , "Age 25")
# print(result)
# result = re.findall(r"\w" , "HI 2235")
# print(result)

# result = re.findall(r"\d+" , "Age 25 and 30 ")
# print(result)

#finadall
# match => match at start 
#search() => first match 
#sub() => replace
#split()=> split a text 

# email_text = "Contact as at support@test.com or admin@company.org or marina977@gmail.com" 
# r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+"   

import re 
# text = "Python is good"
# new_Text = re.sub("good","awesome",text)
# print(new_Text)

# credit = re.sub(r"\d", "#","Marina 1234 47363 47823")
# print(credit)

# phone = "987622296644"
# if re.fullmatch(r"\d{10}" ,phone):
#   print("valid number")
# else:
#   print("Invalid number , phone must be 10 digits only" )





