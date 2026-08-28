from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/ef1300325658f5d5f15e")
all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)

@app.route('/about-us')
def about():
    return render_template("about.html")

@app.route('/contact-us')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def get_post(id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == id:
            requested_post = blog_post
    return render_template("post.html", id=id, post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)