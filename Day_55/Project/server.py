from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_url)
data = response.json()

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html", data=data)

@app.route('/post/<num>')
def get_post(num):
    num = int(num) - 1
    post = data[num]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)


