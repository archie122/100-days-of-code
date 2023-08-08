# age : int
# name : str
# height : float
# is_male : bool

# These are called Type Hints. It is a way to tell the Python interpreter what type of data you are assigning to a variable.
def check_age(age : int) -> bool:
    if age >= 18:
        return True
    else:
        return False
















if check_age(12):
    print("You are 12 years old")
else:
    print("You are not 12 years old")