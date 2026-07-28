from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
    "<p>this is a paragraph</p>" \
    "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDFxOXRvMjhvNG91c3BzdXF2YjEzMGh1eTgxc2E3N2NjOGl2dzRibyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BF0RAxJxSGdKTU3SQn/giphy.gif' style='width:200px'>"


def make_bold(function: function):
    def wrapper():
        return "<b>" + function() +"</b>"
    return wrapper

def make_emphasis(function: function):
    def wrapper():
        return "<em>" + function() +"</em>"
    return wrapper

def make_underlind(function: function):
    def wrapper():
        return "<u>" + function() +"</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlind
def bye():
    return "Bye, World!"

# @app.route("/username/<name>")
# def greet(name):
#     return f"<h1>Hello {name}</h1>"

@app.route("/<name>")
def greet(name):
    return f"<h1>Hello there {name} !</h1>"

if __name__ == '__main__':
    app.run(debug=True)

