from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    return render_template('index.html', random_number=random_number, year = current_year)

@app.route('/blog')
def get_blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    data = response.json()
    return render_template('blog.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)