from flask import Flask
import random

RANDOM_NUMBER = random.randint(0, 9)
TOO_LOW = ("<body style='background-color: #FFF5E0'>"
           "<h1 style='text-align:center; color:#FF6969; font-size:80px; font-weight:bold; font-family:sans-serif;"
           "padding:50px; margin:50px;'>"
           "Too low!"
           "</h1>"
           "<img src='https://media3.giphy.com/media/tOwkgfESVDua4/giphy.gif?cid"
           "=ecf05e47vjnxmx9p9swu83td2gqevk1io733s0nw0l258vve&ep=v1_gifs_search&rid=giphy.gif&ct=g' style='display: "
           "block; margin: 0 auto; height: 600px; border: 15px solid #141E46'>"
           "</body>")

TOO_HIGH = ("<body style='background-color: #FFF5E0'>"
            "<h1 style='text-align:center; color:#FF6969; font-size:80px; font-weight:bold; font-family:sans-serif;"
            "padding:50px; margin:50px;'>"
            "Too high!"
            "</h1>"
            "<img src='https://media.giphy.com/media/Qs1nBXifGHnOI9HBYi/giphy.gif' style='display: block; margin: 0 "
            "auto; height: 600px; border: 15px solid #141E46'>"
            "</body>")

GOT_IT = ("<body style='background-color: #FFF5E0'>"
          "<h1 style='text-align:center; color:#FF6969; font-size:80px; font-weight:bold; font-family:sans-serif;"
          "padding:50px; margin:50px;'>"
          "You got it!"
          "</h1>"
          "<img src='https://media1.giphy.com/media/26u4cqiYI30juCOGY/giphy.gif?cid"
          "=ecf05e47s11lcwxcxq8dn47e1assjy67sjdbwbbemnoc2n7v&ep=v1_gifs_related&rid=giphy.gif&ct=g' "
          "style='display: block; margin: 0 auto; height: 600px; border: 15px solid #141E46'>"
          "</body>")

app = Flask(__name__)


@app.route("/")
def hello():
    return ("<body style='background-color: #FFF5E0'>"
            "<h1 style='text-align:center; color:#FF6969; font-size:80px; font-weight:bold; font-family:sans-serif; "
            "padding:50px'>"
            "Guess a number between 0 and 9, then type it in the URL!"
            "</h1> "
            "<img src='https://media2.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif?cid"
            "=ecf05e47h4gyyda565xj0urjzr75lpjat54aiefnx2j1lk64&ep=v1_gifs_related&rid=giphy.gif&ct=g'"
            "style='display: block; margin: 0 auto; height: 600px; border-radius: 100%; border: 15px solid #141E46'>"
            "</body>")


@app.route("/<number>")
def guess_number(number):
    x = int(float(number))
    if x == RANDOM_NUMBER:
        return GOT_IT
    elif x > RANDOM_NUMBER:
        return TOO_HIGH
    elif x < RANDOM_NUMBER:
        return TOO_LOW


if __name__ == "__main__":
    app.run(debug=True)
