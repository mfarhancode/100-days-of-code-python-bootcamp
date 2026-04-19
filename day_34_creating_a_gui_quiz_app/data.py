
import requests
from tkinter import *
from tkinter import ttk

THEME_COLOR = "#375362"


trivia_categories = {
    'Any Category': 'any',
    "General Knowledge": 9,
    "Entertainment: Books": 10,
    "Entertainment: Film": 11,
    "Entertainment: Music": 12,
    "Entertainment: Musicals & Theatres": 13,
    "Entertainment: Television": 14,
    "Entertainment: Video Games": 15,
    "Entertainment: Board Games": 16,
    "Science & Nature": 17,
    "Science: Computers": 18,
    "Science: Mathematics": 19,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
    "Entertainment: Comics": 29,
    "Science: Gadgets": 30,
    "Entertainment: Japanese Anime & Manga": 31,
    "Entertainment: Cartoon & Animations": 32
}

difficulties = {
    "Any Difficulty": "any",
    "Easy": "easy",
    "Medium": "medium",
    "Hard": "hard"
}

trivia_categories_keys = tuple(trivia_categories.keys())
difficulties_keys = tuple(difficulties.keys())

def generate_questions():

    num_q = no_of_questions.get()
    categ = trivia_categories[category.get()]
    dif = difficulties[difficulty_level.get()]
    # print(num_q)
    # print(categ)
    # print(dif)
    parameters = {
            'amount': num_q,
            'type': 'boolean',
            'category': categ,
            'difficulty': dif
        }
    if categ == 'any':
        parameters.pop('category')
    
    if dif == 'any':
        parameters.pop('difficulty')

    # print(parameters)
    get_questions(parameters)


window = Tk()
window.title('Open Trivia')
window.config(bg=THEME_COLOR, padx=20, pady=20)

# parameters = {
#     'amount': 10,
#     'type': 'boolean',
#     'category': 18,
#     'difficulty': 'easy'
# }

canvas = Canvas(height=150, width=400, bg='white')
canvas.grid(row=0, column=0)


canvas.create_text(65,20, text='Number of Questions: ')

default_questions = IntVar(value=10)
no_of_questions = Spinbox(canvas, from_=1, to=50, increment=1, textvariable=default_questions, state='readonly')
canvas.create_window(200,20, window=no_of_questions)


canvas.create_text(50,50, text='Select Category: ')

category = ttk.Combobox(canvas, width=40 , textvariable=StringVar(), state='readonly')
category['values'] = trivia_categories_keys
canvas.create_window(250,50, window=category)
category.current(0)

canvas.create_text(50,90 , text='Select Difficulty: ')

difficulty_level = ttk.Combobox(canvas, width=20 , textvariable=StringVar(), state='readonly')
difficulty_level['values'] = difficulties_keys
canvas.create_window(200,90, window=difficulty_level)
difficulty_level.current(0)

btn = Button(canvas, text='Start', highlightthickness=0, width=10, command=generate_questions)
canvas.create_window(200,130,window=btn)


def get_questions(params):
    global question_data
    response = requests.get(url="https://opentdb.com/api.php", params=params)

    response.raise_for_status()
    
    data = response.json()
    # print(data)
    question_data = data['results']
    # print(question_data)
    window.destroy()


# this line moved to main.py
# window.mainloop()