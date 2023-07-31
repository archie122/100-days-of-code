# List Comprehension : it is the process of creating a new list from an existing list

# numbers = [1, 2, 3, 4, 5]
# new_list = [n * 2 for n in numbers]
# for num in numbers:
#     numbers = num * 2
#     new_list.append(num * 2)
# print(new_list)

# Example new_list = [new_item for item in list]

# new_list = [n * 2 for n in range(1,5)]
# print(new_list)

names = ['John', 'Paul', 'George', 'Ringo', 'Andy', 'Joe', 'Mike', 'Toby']
new_list = [name for name in names if len(name) < 5]
print(new_list)

upper_names = [name.upper() for name in names]
print(upper_names)