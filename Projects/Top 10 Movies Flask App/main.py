import os

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_TOKEN = os.getenv("API_TOKEN")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RateMovieForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Reviews", validators=[DataRequired()])
    submit = SubmitField("Submit")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top10movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    with app.app_context():
        all_movies = (
            db.session.execute(select(Movie).order_by(Movie.rating.desc()))
            .scalars()
            .all()
        )

        for i, movie in enumerate(all_movies):
            movie.ranking = i + 1

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()

    # Move headers outside so it's available for both API calls
    headers = {
        "accept": "application/json",
        "Authorization": TOKEN}

    if form.validate_on_submit():
        search_url = "https://api.themoviedb.org/3/search/movie"

        parameters1 = {
            "query": f"{form.title.data}",
            "include_adult": "false",
            "language": "en-US&page=1",
        }

        search_response = requests.get(
            search_url, headers=headers, params=parameters1
        ).json()["results"]
        return render_template("select.html", data=search_response)

    movie_id = request.args.get("id")

    if movie_id:
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"

        parameters2 = {
            "include_adult": "false",
            "language": "en-US&page=1",
        }

        movie_data = requests.get(
            details_url, headers=headers, params=parameters2
        ).json()
        image_url = f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"

        new_movie = Movie(
            title=movie_data["title"],
            year=movie_data["release_date"].split("-")[0],
            description=movie_data["overview"],
            img_url=image_url,
            rating=0.0,  # Added required field
            ranking=0,  # Added required field
            review="",  # Added required field
        )
        db.session.add(new_movie)
        db.session.commit()
        print(f"✅ Added New Movie: {new_movie.title}")  # Fixed: was Movie.title

        return redirect(url_for("edit", movie_id=new_movie.id))  # Pass movie_id to edit

    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("movie_id")
    if request.method == "POST":
        with app.app_context():
            movie_to_update = db.session.execute(
                select(Movie).where(Movie.id == movie_id)
            ).scalar()
            if movie_to_update:
                movie_to_update.rating = form.rating.data
                movie_to_update.review = form.review.data
                db.session.commit()
                print(f"✅ Movie Updated: {movie_to_update.title}")
            return redirect(url_for("home"))
    with app.app_context():
        movie_to_edit = db.session.execute(
            select(Movie).where(Movie.id == movie_id)
        ).scalar()
    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")

    with app.app_context():
        movie_to_delete = db.session.execute(
            select(Movie).where(Movie.id == movie_id)
        ).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
        print(f"🚫 Movie Deleted: {movie_to_delete.title}")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
