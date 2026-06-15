#====================================
#Web Scraping => is the process of automatically extracting information from website 
# HTML"TAGS" , CSS , JS 
# <h1> Python course </hh1>
# <p> Price :4000 </p>
#Step 1 => Send an http request 
# Step2 => recerive a response => html code (response.text)
# Step 3 => Parse html => BeautifulSoup (library)=> converts it into a structured python that can be understood  
# Step 4 => Extract data 
#====================================
# #Python => Get Request => Server => html response =>python
# import requests 
# from bs4 import BeautifulSoup
# response = requests.get("https://info.cern.ch/")
# soup = BeautifulSoup(response.text , "html.parser")

# title = soup.find("p")
# print(title.text)

#------------------------------
#Http Methods
#1-Get => Receiving data requests.get()
#2-Post =>Sending data (registeration form , login form)
#3- Put => Updating existing data 
#4- delte => delete post 


#Status Code :
#checked if your request is okay or not
# 200 => Success
# 201 => Created 
# 400 => Bad Request
# 404 => Not Found
# 500 => Server error 
# if response.status_code == 200:
#   print("Success")
# import requests 
# from bs4 import BeautifulSoup
# html = """
# <ul>
# <li class="course">Python</li>
# <li class="course">Java</li>
# <li class="course">C++</li>
# </ul>
# """
# soup = BeautifulSoup(html, "html.parser")
# courses = soup.find_all("li" , class_ ="course")

# for course in courses:
#   print(course.text)

#=========================================================
#API =>"Application Programming Interface" it allows program to communicate directly 
# Application => Api => JSON Data 
#.json() => convert from json to python dictionary 
# data = response.json()
# some api still return xml => ElementTree 

#==============================================================
#Synchronization  = > program runs the instructions one after another  (code => waits untill finishes)
#_
#_
#_
#_ => takes long time (finishes)
#_
#_
#_

