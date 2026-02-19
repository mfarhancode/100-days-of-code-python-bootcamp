from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}


try:
    data = pandas.read_csv(filepath_or_buffer='data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/indonesian_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# print(to_learn)

current_word = {}

def flip_card():
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_word['English'], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)

window = Tk()
# window.config(height=400, width=500, bg=BACKGROUND_COLOR, pady=50, padx=50)
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title('Flashy')

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image((400,263),image=card_front_img)



def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    indo_word = current_word['Indonesian']
    canvas.itemconfig(word, text=indo_word, fill='black')
    canvas.itemconfig(title, text='Indonesian', fill='black')
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)



def is_known():
    to_learn.remove(current_word)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

title = canvas.create_text((400, 150),text='', font=('Ariel', 40, 'italic'))
word = canvas.create_text((400, 350),text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0,columnspan=2)
next_card()

cross_image = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=cross_image, highlightthickness=0, relief='flat', bg=BACKGROUND_COLOR, command=next_card)
unknown_btn.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_btn = Button(image=check_image, highlightthickness=0,relief="flat", bg=BACKGROUND_COLOR, command=is_known)
known_btn.grid(row=1, column=1)





window.mainloop()