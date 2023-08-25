# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        result = function(args[0], args[1], args[2])
        print(f'You called the {function.__name__} ({args[0]}, {args[1]}, {args[2]})')
        print('It returned: ' , result)
    return wrapper


# Use the decorator 👇


@logging_decorator
def a_function(x, y, z):
    return x * y * z

a_function(1, 2, 3)