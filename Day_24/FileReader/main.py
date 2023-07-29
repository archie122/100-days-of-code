# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# Because it is a bit annoying to constantly have to close the file. Python developer is usually use the segment of
# code below to automatically close it.

# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# Writing to a file (always change the mode)
with open('my_file.txt', mode='w') as file:
    file.write('Hello, My name is Archie. :D')

# Adding to a file
with open('my_file.txt', mode='a') as file:
    file.write('Hello, My name is Robert.')

# Reading from a file
with open('my_file.txt', mode='r') as file:
    contents = file.read()
    print(contents)

# Creating a file
with open('my_new_file.txt', mode='w') as file:
    file.write('Hello, My name is Archie')