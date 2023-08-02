# Keyword Aruguments
def my_function_1(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}. You are {age} years old.")


# my_function(first_name="John", last_name="Doe", age=30)

# Default Arguments
def my_function_2(country="Norway"):
    print(f"I am from {country}")


# Unlimited Arguments
def my_function_3(*kids):  # *args is ually used to accept a variable number of arguments
    for kid in kids:
        print(kid)


# Challenge
def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


# print(add(1, 2, 3, 4, 5))


# Unlimited Positional Arguments
def my_function_4(*args):
    print(args[3])


my_function_4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Keyword Arguments
def my_function_5(**kid):
    print(kid)


my_function_5(fname="John", lname="Doe")


# Example

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")

my_car = Car(make="Ford", model="Mustang", year=1969)