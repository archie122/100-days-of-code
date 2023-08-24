from flask import Flask

app = Flask(__name__)  # The __name__ variable allows flask to know the name of the file


# When the user visits the home page
@app.route("/")  # This is a python decorator
# A decorator is a function that takes another function as an argument
# and returns another function with additional functionality

# The @ symbol is used to mark the decorator function and is called syntactic sugar
def hello_world():  # This is what will happen when the user visits the home page
    return "<p>Hello, World!</p>"
