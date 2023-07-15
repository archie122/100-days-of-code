#Calculator
from art import logo


#Adding two numbers together
def add(n1, n2):
    return n1 + n2


#Subtracting two numbers
def subtract(n1, n2):
    return n1 - n2


#Multiplying two numbers
def multiply(n1, n2):
    return n1 * n2


#Dividing two numbers
def divide(n1, n2):
    return n1 / n2


math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number? : "))
  for key in math_operations:
      print(key)
  should_continue = True

  while should_continue:
      user_choice = input("Pick another operation : ")
      calc_function = math_operations[user_choice]
      num2 = float(input("What is the second number? : "))
      result = calc_function(num1, num2)

      print(f"{num1} {user_choice} {num2} = {result}")

      if input(
              f"Type 'y' to continue calculating with {result} or type 'n' start a new calculation : "
      ) == "y":
          num1 = result
      else:
          should_continue = False
          calculator()


calculator()
