#---------------------------------------------
#Data Structures =>  is a way of organizing and storing data in my 
#computer / system so it can be accessed and modified efficiently
#----------------------------------------------
#---------------------------------------------
# m1_datastructuresStackandQueue.py
#Stack => A way of sorting the data LIFO (Last in First Out)
#list , tuple 
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print("Stack after pushing operation" , stack)
# print("Current top element" , stack[-1])
# stack.pop()
# print("Stack after Pop operation" , stack)
# print("Current top element" , stack[-1])
# stack.pop()
# print("Stack after Second Pop operation" , stack)
# print("Current top element" , stack[-1])

#--------------------------------------------------------------
#Queue : FIFO("fIRST IN , FIRST OUT")
 
# WE are calling the deque code from the collections that is made by prgrammers 
# from collections import deque
# queue = deque() #i made an empty queue 
# print(queue)

# #Enqueue : add elemengt from the rear 
# queue.append("Ali")
# queue.append("Marina")
# queue.append("John")
# print(queue)
# print(queue[0])
# #Dequeue : Remove element from front 
# print(queue.popleft())
# print(queue)

# #how to get the front elemnent (index)
# print(queue[0])
# queue.append("Mark")
# print(queue)
# print(queue[-1])

# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next = None

# node1 = Node(10)
# node2 = Node (20)
# node3 = Node (30)


# node1.next = node2 
# node2.next = node3
# current = node1

# while current is not None:
#   print(current.data)
#   current = current.next

#=====================================================
# Collection : container that have a lot of codes and data 
# built in variables, built in functions

# why ? less code , better in performance 
# more readable 

# 1- deque 
# 2-Counter 
# 3=defaultdict
# from collections import Counter , deque , defaultdict
# data = [1,1,2,3]
# print(Counter(data))

# student_marks={
#   "Science" : 30
# }
# student_marks["Math"]+=10
# # defaultdict
# from collections import Counter , deque , defaultdict
# student_marks= defaultdict(int)
# student_marks["Maths"]+=10;
# print(student_marks)