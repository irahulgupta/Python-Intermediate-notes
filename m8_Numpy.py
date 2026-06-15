# --------------------------------------------------
# Numpy(Numerical Python) => is a python library used for :
# Mathematical Calculations
# Works with large datasets 
# Multi Dimenesional arrays 
# supercharged calculator for python
# --------------------------------------------------
#Without Numpy 
# numbers =[1,2,3,4,5]
# result = []
# for n in numbers :
#   result.append(n ** 2)

# print(result)

#With Numpy 
# import numpy as np
# numbers = np.array([1,2,3,4,5])
# print(numbers ** 2) 

#Numpy is Faster than Python Lists  
#Memory Efficient => better performance 
# Vectorized Operations 
# for n in numbers :
#   result.append(n * 2)
#arr *=2

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr) 
# arr = np.zeros(5)
# print(arr)
# arr1 = np.ones(5)
# print(arr1)
# arr1 = np.arange(1,11)
# print(arr1)

#1D array :
# arr = np.array([1 , 2 , 3])
# print(arr)


# #2D array :
# arr2 = np.array([
#   [1,2],
#   [3,4]
#   ])
# print(arr2)

#3D array :
# arr3 = np.array([
#  [[1,2],[3,4]]
#  ,[[5,6],[7,8]]
#   ])
# print(arr3)

# arr = np.array([
#   [1,2,3],
#   [4,5,6]
#   ])
# print(arr)
# #shape (rows,columns)
# print(arr.shape) 
# #size => total number of elements
# print(arr.size)
#ndim=> number of dimension
# print(arr.ndim)
# print(arr.dtype)

#Mathematical 
# print(arr + 5)

# Statistical Functions
#  
#MEAN => Avarage Value
# mean =np.mean(arr)
# print(mean)

#Sum 
# np.sum(arr)

# #Max
# max=np.max(arr)
# print(max)

# #Min
# min=np.min(arr)
# print(min)

#Standard Deviation => measures the spreed of data
# sd = np.std(arr)
# print(sd)

#Array => indexed , slicing 
# arr = np.array([10,20,30,40,50,60])
# print(arr[0])
# print(arr[1:4])
# print(arr[arr > 25])
# arr2 = arr.reshape(2,3)
# print(arr2)
# a= np.array([1,2])
# b=np.array([3,4])
# #hstack 
# c=np.hstack((a,b))
# print(c)
# d = np.vstack((a,b))
# print(d)

#====================================================================
#Pandas => python library => for handling structured data 
# Series , dataFrame 

# pip install pandas

import pandas as pd 
#series => 1D array labeled (start from 0)
# s= pd.Series([10,20,30])
# print(s)

#Data Frame => 2D table => excel worksheet 

# df = pd.DataFrame({
#   "Name" : ["Marina" , "John"],
#   "Age" : [20,25]
# })
# print(df)
# data = {
#   "Name" : ["Marina" , "John"],
#   "Age" : [20,25]
# }
# df = pd.DataFrame(data)
# print(df)

#Read csv , load data from csv 
df = pd.read_csv("employees.csv")
# print(df)

# View First Rows head() => print the first 5 rows 
# print(df.head()) 

#tail() => shows last rows =>5
# print(df.tail())

#info => columns, data type , missin values
# print(df.info())

#descripe => mean , min , max , standard deviation "Statistics"
# print(df.describe())

#Accrssing Rows => loc[] "location"
# print(df.loc[0])


# print(df[df["Age"]>20])

#Delete a Column  drop
# df.drop("Age")

#Renam a column 
# df = df.rename(columns={"Salary" : "Revenue"})
# print(df)

# Missing Data 
#Find missing values:
# print(df.isnull().sum())

# #1- Remove the whole row (missing values)  
# df.dropna(inplace=True)

# #2-Fill this Missing Values:
# df.fillna(0)

#-------------------------------------
#Datacleaning 
#Duplicates 
# df = df.drop_duplicates()
# print(df)
#Change Column type
# df["Age"] = df["Age"].astype(int)

#Sort => default ascending
# df.sort_values("Salary") 
#descending
# df.sort_values("Salary" , ascending=False)

#Group By 
#Categories    Sales
#Tech          100
#Tech          200
#Office        300 

# df.groupby("Category")["Sales"].sum() 
#office 300
#Tech   300

#pip install matplotlib
# import matplotlib.pyplot as plt

#Age Distribution 
# plt.figure(figsize=(8,5))
# plt.hist(df["Age"] , bins=8)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Employees")
# plt.show()

#Average Salary be Department 
# avg_salary = df.groupby("Department")["Salary"].mean()
# plt.figure(figsize=(8,5))
# avg_salary.sort_values().plot(kind="bar")
# plt.title("Salary Distribution")
# plt.xlabel("Department")
# plt.ylabel("Average Salary")
# plt.show()

# dept_counts = df["Department"].value_counts()
# plt.figure(figsize=(8,8))
# plt.pie(
#   dept_counts,
#   labels=dept_counts.index,
#   autopct="%1.1f%%"
# )
# plt.title("Employees distribution by departments")
# plt.show()








