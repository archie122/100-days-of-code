from flask import Flask, render_template, request
import requests
import smtplib

BLOG_URL = 'https://api.npoint.io/0d50c89524a4659d48d6'
RESPONSE = requests.get(BLOG_URL)
DATA = RESPONSE.json()
EMAIL = "t72189519@gmail.com"
PASSWORD = "tdqwngwakikmzexk"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=DATA)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/post/<num>')
def get_post(num):
    num = int(num) - 1
    post = DATA[num]
    return render_template("post.html", post=post)

@app.route('/from-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    if name != "" and email != "" and phone != "" and message != "":
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Encrypting the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="archie.c122133@gmail.com",
                msg=f"Subject:Message from {name}!!\n\n"
                    f"Here is the message for today : {message}\n\n"
                    f"Email: {email}\n\n"
                    f"Phone: {phone}\n\n")

        return render_template("from-entry.html", name=name, email=email, phone=phone, message=message)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


