from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)
Bootstrap5(app)
API_KEY = "e6d51f9475aa3942cc1dbee9fb76179c"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNmQ1MWY5NDc1YWEzOTQyY2MxZGJlZTlmYjc2MTc5YyIsInN1YiI6IjY0ZjM2ODYwOWU0NTg2MDExZGU2MmViOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c-qgPcMvOnW6H0RJ7G_EsPx9r6HDwNguj91K6LzSOs0"
}

all_movies = []

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)


class MovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.asc())).scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


def build_url(movie_title):
    movie_title = movie_title.replace(" ", "%20")
    return f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=true&language=en-US&page=1"


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(build_url(movie_title), headers=headers).json()
        return render_template("select.html", movies=response["results"])

    return render_template("add.html", form=form)


@app.route("/select/<title>", methods=["GET", "POST"])
def select(title):
    response = requests.get(build_url(title), headers=headers).json()
    new_movie = Movie(
                title=response["results"][0]["title"],
                year=response["results"][0]["release_date"],
                description=response["results"][0]["overview"],
                rating=response["results"][0]["vote_average"],
                review='Add a review',
                img_url= "https://image.tmdb.org/t/p/w500" + response["results"][0]["poster_path"]
            )

    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


def get_movie(id):
    return db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = MovieForm()
    movie = get_movie(id)
    if form.validate_on_submit() and request.method == "POST":
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<id>")
def delete(id):
    movie = get_movie(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)


