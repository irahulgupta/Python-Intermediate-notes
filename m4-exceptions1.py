#---------------------------------------------
#Exceptions
#----------------------------------------------
print("MODULE 4 HANDS-ON: INPUT VALIDATION SYSTEM")
print("-" * 55)


# --------------------------------------------------
# CUSTOM EXCEPTION
# --------------------------------------------------
class InvalidAgeError(Exception):
    pass


def validate_user():
    try:
        print("\nEnter user details")

        name = input("Enter name: ")

        if not name.isalpha():
            raise ValueError("Name must contain only letters")

        age = int(input("Enter age: "))

        if age < 0:
            raise InvalidAgeError("Age cannot be negative")

        if age < 18:
            raise InvalidAgeError("User must be at least 18 years old")

    # MULTIPLE EXCEPTIONS
    except ValueError as ve:
        print("Value Error:", ve)

    except InvalidAgeError as iae:
        print("Custom Error:", iae)

    except Exception as e:
        print("Unexpected Error:", e)

    # ELSE BLOCK
    else:
        print("\nValidation Successful")
        print(f"Welcome {name}, Age: {age}")

    # FINALLY BLOCK
    finally:
        print("Execution completed.\n")


# --------------------------------------------------
# RUN MULTIPLE TIMES
# --------------------------------------------------
for i in range(3):
    validate_user()

