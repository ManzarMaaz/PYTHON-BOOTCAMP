import os
from smtplib import SMTP

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

MY_EMAIL = os.getenv("EMAIL_ADDRESS")
TO_EMAIL = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/ae536bfb886e5c0377e1").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        mail = request.form["email"]
        message = request.form["message"]
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {mail}")
        print(f"Message: {message}")
        subject = "Contact Form Message !!!"
        message_body = (
            f"Name: {name}\nPhone: {phone}\nEmail: {mail}\nMessage: {message}"
        )
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"subject:{subject}\n\n{message_body}",
            )

        return render_template("contact.html", sent=True)

    return render_template("contact.html", sent=False)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in all_posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=True)
