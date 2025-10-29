import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/9bd5da8c48fbe6b8c398").json()
posts_objects = []


for blog in all_posts:
    post_obj = Post(
        id=blog["id"], title=blog["title"], subtitle=blog["subtitle"], body=blog["body"]
    )
    posts_objects.append(post_obj)
print(posts_objects)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
