# What are environment variables?
#   Convenience : When you deploy a large application, the process is quite complicated. This means that you need to
#   write the same code multiple times. This can be avoided by using environment variables.
#   Security : Environment variables are used to store sensitive information.
#
#
# Environment variables are variables that are stored in the operating system and can be accessed from anywhere in the code.
# They also give you the ability to modify the variables, without changing the code. They also give you the ability to
# store the keys in a secure location and the code does not need to be changed.

# To create and use environment variables:
# 1. In the terminal, type "export" followed by the name of the variable you want to create.
# 2. Have the os module installed.
# 3. To access the environment variables, use the os module in this format:
# os.environ.get("VAR_NAME")

# Learn more about environment variables


import os

API_KEY = os.environ.get("API_KEY")

print(API_KEY)
