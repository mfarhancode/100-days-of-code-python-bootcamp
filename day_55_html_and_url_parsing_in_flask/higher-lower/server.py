from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(0,9)
print(rand_num)

@app.route("/")
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='width:200px'>"


@app.route("/<int:guess_number>")
def check(guess_number):
    if guess_number > rand_num:
        return "<h1 style='color:red'>Too high, try again!</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style='width:200px'>"
    elif guess_number < rand_num:
        return "<h1 style='color:yellow'>Too low, try again!</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' style='width:200px'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style='width:200px'>"

if __name__ == '__main__':
    app.run(debug=True)