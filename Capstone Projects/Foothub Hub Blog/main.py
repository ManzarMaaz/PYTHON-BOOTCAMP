import select
from datetime import date

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text, select  # noqa: F811
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField, URLField


class PostForm(FlaskForm):
    title = StringField("Blog Post Title")
    subtitle = StringField("Subtitle")
    author_name = StringField("Your Name")
    img_url = URLField("Blog Image URL")
    body = CKEditorField("Blog Content")
    submit = SubmitField("Post Submit")


app = Flask(__name__)

# CKEditor secure LTS version
app.config["CKEDITOR_SERVE_LOCAL"] = False
# app.config["CKEDITOR_PKG_TYPE"] = "full"
app.config["CKEDITOR_CDN_URL"] = "https://cdn.ckeditor.com/4.25.1-lts/full/ckeditor.js"

app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    with app.app_context():
        all_post = (
            db.session.execute(select(BlogPost).order_by(BlogPost.id)).scalars().all()
        )
    posts = [post for post in all_post]
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author_name.data,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit_post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    current_post = db.get_or_404(BlogPost, post_id)

    edit_form = PostForm(
        title=current_post.title,
        subtitle=current_post.subtitle,
        img_url=current_post.img_url,
        author=current_post.author,
        body=current_post.body,
    )

    if edit_form.validate_on_submit():
        current_post.title = edit_form.title.data
        current_post.subtitle = edit_form.subtitle.data
        current_post.body = edit_form.body.data
        current_post.img_url = edit_form.img_url.data
        current_post.author = edit_form.author_name.data
        current_post.date = date.today().strftime("%B %d, %Y")

        db.session.commit()

        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=edit_form, editing=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=["POST", "GET"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
