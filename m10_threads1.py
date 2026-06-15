#--------------------------------------------------
# Threads
# --------------------------------------------------
#Downloaded => read from database => send email -> open chrome  => Solution "MultiThreading"
#Process => Program 
# chrome browsing => process
# vs code => process 
# python code => process 
# Thread => is a smallest unit of execution inside a program 
# Company (Process)
# - Employer 1 (Thread)
# - Employer 2 (Thread)
# - Employer 3 (Thread)

#Single Thread , MultiThread 
# by default Python program runs on one thread => one after another 
# print("Task1")
# print("Task2")
# print("Task3")
#====================================================
#downloading 10 files => Multithreading 
# concurrency vs parallelism 
# Concurrency => Multiple tasks make progress during the same period 
#Task A
#Task B
#Task C
#A=>B=>C=>A=>B=>C=>A=>C "Schedueling" => Context Switching 

#Parallelism => tasks literaaly executes at the same time 
#============================================================
# import threading 
# counter = 0
# def task():
#   global counter
#   counter += 1


# thread = threading.Thread(target=task)
# thread.start()
# #join()=> waits untill thread finishes 
# thread.join()
# print(counter)

#Shared Memory => threads shae the same memory 
#counter = 0 => main thread (Thread1) , (Thread2)
#Race Condition 
# Solution => lock 
# import threading 
# counter = 0
# lock = threading.Lock()
# def increment():
#   global counter

#   lock.acquire()
#   counter += 1
#   lock.release()

# increment()
# thread = threading.Thread(target=increment)
# thread.start()
# #join()=> waits untill thread finishes 
# thread.join()
# print(counter)

# import threading
# counter = 0

# def task():
#   global counter
#   counter +=1

# threads = []
# for i in range(100000):
#   t=threading.Thread(target=task)
#   threads.append(t)
#   t.start()

# for t in threads:
#   t.join()

# print(counter)  

#Deadlock => Threads 2 Thread 1  Thread2 => threads are waiting for each others 
# import threading 
# lock1= threading.Lock()
# lock2= threading.Lock()

# def task1():
#   lock1.acquire()
#   print("Thread 1 got Lock1")

#   lock2.acquire()
#   print("Thraed 1 got lock2")

#   lock2.release()
#   lock1.release()


# def task2():
#   lock2.acquire()
#   print("Thread 2 got Lock2")

#   lock1.acquire()
#   print("Thraed 1 got lock2")

#   lock1.release()
#   lock2.release()

# t1 = threading.Thread(target=task1) #t1 => l1 =>l2
# t2= threading.Thread(target=task2) #t2 => l2 =>l1
#thread 1 owns lock 1 , waiting for lock 2
#thread 2 owns lock2 , waiting for lock 1 

# t1.start()
# t2.start()

#Thread 1 => lock 1 => lock 2
#Thread2 => lock 1 =>lock2 

#Timeout 
# lock.aquire(timeout = 3)

# import time 
# def task1():
#   print("Task1 Started")
#   time.sleep(3)
#   print("Task1 Finished")

# def task2():
#   print("Task2 Started")
#   print("Task 2 Finished")

# task1()
# task2()

#Asynchronization  => if there is a task / code that will takes time , it will not wait it will make another code or task 
#async , await 

import time  
import asyncio
async def task1():
  print("Task1 Started")
  await asyncio.sleep(3)
  print("Task1 Finished")

async def task2():
  print("Task2 Started")
  print("Task 2 Finished")

#await => Event loop  => responsible for run another code 
async def main():
  await asyncio.gather(
    task1(),
    task2()
  )

asyncio.run(main()) 
#Api Calls
# Web Scrapping 
#Chatting Application 


