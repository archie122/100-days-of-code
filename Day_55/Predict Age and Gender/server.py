from flask import Flask, render_template
import requests


def get_name_age(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    data = response.json()["age"]
    return data


def get_gender(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    data = response.json()["gender"]
    return data


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gender/<name>")
def gender(name):
    return render_template("gender.html", gender=get_gender(name), name=name)


@app.route("/age/<name>")
def age(name):
    return render_template("age.html", age=get_name_age(name), name=name)


if __name__ == "__main__":
    app.run(debug=True)
