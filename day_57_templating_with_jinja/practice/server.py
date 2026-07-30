from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year, name='Muhammad Farhan')

@app.route('/guess/<name>')
def guess_gender_age(name):

    gender = requests.get(f"https://api.genderize.io/?name={'farhan'}").json()['gender']
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    # gender, age = 20, 15
    
    return render_template('guess.html', name=name, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)