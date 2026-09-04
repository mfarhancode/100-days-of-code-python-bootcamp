from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
path_db = Path(__file__).parent.joinpath("top_movies.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path_db}"
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title  : Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

# with app.app_context():
#     db.create_all()

def add_book(title, year, description, rating, ranking, review, img_url):
    with app.app_context():
        new_movie = Movie(title=title, year=year, description=description, rating=rating, ranking=ranking, review=review, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()

def add_book_object(Movie):
    with app.app_context():
        db.session.add(Movie)
        db.session.commit()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    movies_list = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars().all()
    return render_template('index.html', movies=movies_list)


@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie, form=form)

@app.route("/delete", methods=['GET', 'POST'])
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
