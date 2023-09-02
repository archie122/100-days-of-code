import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

all_books = []
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    book = get_book(id)
    if request.method == "POST":
        rating = request.form["rating"]
        book.rating = rating
        db.session.commit()
    return render_template("edit.html", book=book)


@app.route("/delete/<id>")
def delete(id):
    book = get_book(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


def get_book(id):
    return db.session.execute(db.select(Book).where(Book.id == id)).scalar()

if __name__ == "__main__":
    app.run(debug=True)

