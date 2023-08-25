from flask import Flask

app = Flask(__name__)


# Paths (this means ending part of the url with a slash)
@app.route("/")
def hello():
    return ("<h1 style='text-align:center; color:blue; font-size:100px'>Hello!</h1>"
            "<p style='text-align:center; color:red; font-size:50px'>This is the home page</p>"
            "<img src='https://picsum.photos/400/600' style='display: block; margin: 0 auto;'>")



@app.route("/hello")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/hello/<name>")
def hello_name(name):
    return f"<h1>Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
