from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from pathlib import Path

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

path_db = Path(__file__).parent.joinpath("new-books-collection.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path_db}"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

def add_book(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        title =  request.form["title"]
        author = request.form["author"]        
        rating = request.form["rating"]
        add_book(title, author, rating)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    
    return render_template("edit_rating.html", book=book_selected)
    

if __name__ == "__main__":
    app.run(debug=True)

