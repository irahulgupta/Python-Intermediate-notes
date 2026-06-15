# Performance Optimization => Making our program :
#run faster 
#reducing memory consumption 
#using cpu resources efficiently 
#improving overall performance 

#i think this function is slow 
# Measure first 
# find the bottleneck 
# optimize the bottleneck 
# Profiling => measure how your program behaves while runnning 

#1 - time module 
# import time 
# start = time.time()
# for i in range(10000):
#   pass
# end = time.time()
# print(end-start)

#2- timeit => more accurate in time 
# import timeit
# execution_time = timeit.timeit(
#   "sum(range(1000))",
#   number=1000
# )
# print(execution_time)

#3 - cprofile => professional tool 
# import cProfile 
# cProfile.run("sum(range(100000))")

#======================================================
#LOOP => biggest issue
# numbers =[]
# for i in range(10000):
#   numbers.append(i)

# total = 0
# for num in numbers:
#   total += num

# print(total)

# sum1 = sum(range(10000))
# print(sum1)

#=====================================
#List Comprehension vs Tradition Listg 
# square = []
# for i in range(10):
#   square.append(i*i)

# print(square)

# square = [i*i for i in range(10)]

#Memory optimization 

# numbers =[i for i in range(100000)]

#Generator () => generates the values one at at time
# square = sum(i for i in range(10)) 
# print(square)

#Built in function 
# avoid nesting 
# minize object creation 
# efficient data structure 

#GIL => Global Interpreter Lock 
# Protects python's internal memory structure => threads 
#Thread a -------------
#thread b -------------
#thread c -------------

#With Gil => only one executes at a time  
#Thread a ---
#thread b     ----
#thread c          ----

#Async Programmer 
#Numpy , pandas 

import time
import cProfile

print("MODULE 12 HANDS-ON: CODE OPTIMISATION EXERCISE")
print("-" * 60)


# --------------------------------------------------
# 1. INEFFICIENT LOOP
# --------------------------------------------------
def inefficient_sum():
    total = 0
    numbers = []

    for i in range(100000):
        numbers.append(i)

    for num in numbers:
        total += num

    return total


# --------------------------------------------------
# 2. OPTIMISED LOOP
# --------------------------------------------------
def optimised_sum():
    return sum(range(100000))


# --------------------------------------------------
# 3. MEMORY-FRIENDLY GENERATOR STYLE
# --------------------------------------------------
def generator_sum():
    return sum(i for i in range(100000))


# --------------------------------------------------
# 4. TIMING FUNCTION
# --------------------------------------------------
def measure_execution_time(function_name, function_reference):
    start_time = time.time()
    result = function_reference()
    end_time = time.time()

    print(f"{function_name} result: {result}")
    print(f"{function_name} execution time: {end_time - start_time:.6f} seconds\n")


# --------------------------------------------------
# 5. GIL CONCEPT DEMO (CPU-BOUND STYLE)
# --------------------------------------------------
def cpu_task():
    total = 0
    for i in range(500000):
        total += i * i
    return total


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------
print("\n1. EXECUTION TIME COMPARISON\n")

measure_execution_time("Inefficient Sum", inefficient_sum)
measure_execution_time("Optimised Sum", optimised_sum)
measure_execution_time("Generator Sum", generator_sum)


print("2. PROFILING INEFFICIENT FUNCTION\n")
cProfile.run("inefficient_sum()")


print("\n3. BEST PRACTICES DISCUSSION")
print("- Use built-in functions where possible")
print("- Avoid unnecessary intermediate lists")
print("- Prefer generators for memory efficiency")
print("- Keep code readable while optimising")
print("- Profile before optimising")


print("\n4. GIL CONCEPT NOTE")
print("CPU-bound tasks in Python threads may not always speed up due to the GIL.")
print("For heavy CPU work, multiprocessing is often a better choice than threading.")


print("\nLab completed successfully.")

