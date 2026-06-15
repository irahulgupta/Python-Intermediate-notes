#---------------------------------------------
#Functions
#----------------------------------------------
print("MODULE 3: FUNCTIONS DEMO")
print("-" * 50)


# --------------------------------------------------
# 1. HIGHER-ORDER FUNCTIONS
# --------------------------------------------------
print("\n1. HIGHER-ORDER FUNCTIONS")


def apply_function(func, value):
    return func(value)


def square(x):
    return x * x


result = apply_function(square, 5)
print("Square using higher-order function:", result)

# --------------------------------------------------
# 2. CLOSURES
# --------------------------------------------------
print("\n2. CLOSURES")


def outer_function(multiplier):
    def inner_function(number):
        return number * multiplier
    return inner_function


double = outer_function(2)
triple = outer_function(3)


print("Double of 5:", double(5))
print("Triple of 5:", triple(5))




# --------------------------------------------------
# 3. LAMBDA FUNCTIONS
# --------------------------------------------------
print("\n3. LAMBDA FUNCTIONS")


add = lambda a, b: a + b
print("Lambda addition:", add(10, 20))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))


print("Squared list using lambda:", squared)




# --------------------------------------------------
# 4. FUNCTION ARGUMENT TYPES
# --------------------------------------------------
print("\n4. FUNCTION ARGUMENTS")


def student_info(name, course="Python", *skills, **details):
    print("Name:", name)
    print("Course:", course)
    print("Skills:", skills)
    print("Details:", details)


student_info(
    "Rahul",
    "Data Science",
    "Python", "SQL",
    city="Bangalore",
    experience=2
)




# --------------------------------------------------
# 5. RECURSION
# --------------------------------------------------
print("\n5. RECURSION")


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))




print("\nDemo completed successfully.")
