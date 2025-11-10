from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
boostrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}"


with app.app_context():
    db.create_all()


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        author_name = request.form.get("author")
        rating = request.form.get("rating")
        # new_dictionary = {"title": book_name, "author": author_name, "rating": rating}
        # all_books.append(new_dictionary)
        with app.app_context():
            new_book = Book(
                title=book_name,
                author=author_name,
                rating=rating,
            )
            db.session.add(new_book)
            db.session.commit()
            print(f"✅ New Book Added: {new_book.title}")
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/", methods=["GET", "POST"])
def home():
    with app.app_context():
        all_books = db.session.execute(select(Book)).scalars().all()
    return render_template("index.html", data=all_books)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    if request.method == "POST":
        with app.app_context():
            book_to_update = db.session.execute(
                select(Book).where(Book.id == book_id)
            ).scalar()
            if book_to_update:
                book_to_update.rating = request.form.get("new_rating")
                db.session.commit()
                print(f"✅ Updated Book: {book_to_update.title}")
        return redirect(url_for("home"))
    with app.app_context():
        book_to_edit = db.session.execute(
            select(Book).where(Book.id == book_id)
        ).scalar()

    return render_template("edit.html", book_data=book_to_edit)


@app.route("/Delete")
def delete():
    book_id = request.args.get("id")
    with app.app_context():
        book_to_be_deleted = db.session.execute(
            select(Book).where(Book.id == book_id)
        ).scalar()
        if book_to_be_deleted:
            db.session.delete(book_to_be_deleted)
            db.session.commit()
            print(f"🚫 Book Deleted: {book_to_be_deleted.title}")
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=True)
