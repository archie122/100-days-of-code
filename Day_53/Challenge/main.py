from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_italic(function):
    def wrapper():
        return f"<i>{function()}</i>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye World!"


if __name__ == '__main__':
    app.run(debug=True)
