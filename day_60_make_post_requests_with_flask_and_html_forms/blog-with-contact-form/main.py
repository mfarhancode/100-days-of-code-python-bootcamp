from flask import Flask, render_template, request
import requests
import smtplib
from pathlib import Path
import os
from dotenv import load_dotenv

env_file_path = Path(__file__).parent.joinpath('.env')
load_dotenv(dotenv_path=env_file_path)

MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def send_mail(name, email, phone, message):
    
    content_email = f'Name: {name} \nEmail: {email} \nPhone number: {phone} \nMessage: {message} '
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = RECIPIENT_EMAIL,
                            msg=f"Subject:New Message\n\n{content_email}")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        is_form_sent = True
        data = request.form
        name, email, phone, message = data['name'], data['email'], data['phone'], data['message']
        send_mail(name, email, phone, message)
        return render_template("contact.html", is_form_sent=is_form_sent)
    else: 
        is_form_sent = False
        return render_template("contact.html", is_form_sent=is_form_sent)
    # is_form_sent = (request.method == 'POST')
    # return render_template("contact.html", is_form_sent=is_form_sent)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route('/form-entry', methods=['POST'])
# def receive_data():
#     if request.method == 'POST':
#         return render_template('form-entry.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
