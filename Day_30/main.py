# File Error
# with open("file.txt") as file:
#     lines = file.readlines()

# Key Error
# a_dict = {"a": 1, "b": 2}
# print(a_dict["c"])

# Index Error
# a_list = [1, 2, 3]
# print(a_list[5])

# Type Error
# a_list = [1, 2, 3]
# print(a_list + 2)

# Error handling
# try:      This code will be executed and the error will be handled
# except:   If there was an error, this code will be executed
# else:     If there was no error, this code will be executed
# finally:  This code will be executed no matter what

# try:
#     file = open("file.txt")
#     a_dict = {"a": 1, "b": 2}
#     print(a_dict["c"])
# except FileNotFoundError: # This line of code is important for error handling, because then it allows for the program
#     # to know what error to handle
#     file = open("file.txt", "w")
# except KeyError as error:
#     print(f"KeyError : {error}")
# else: # If no errors were found, this code will be executed.
#     content = file.read()
#     print(content)
# finally: # This code will be executed no matter what
#     # file.close()
#     # print("File closed")
#     raise Exception("Something went wrong") # This line of code creates an exception, that the user can handle

height = int(input("Height: "))
weight = int(input("Width: "))

if height > 3 :
    raise Exception("Height must be less than 3")

bmi = weight / height ** 2