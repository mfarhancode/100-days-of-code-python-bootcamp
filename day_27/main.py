from tkinter import *

window = Tk()
window.title('My First GUI Program')
# print(window.minsize())
window.minsize(width=100, height=300)
window.config(padx=100, pady=20)

# Label

my_label = Label(text='I am a label', font=('Arial', 24))
my_label.grid(column=0, row=0)

# my_label['text'] = 'New text'
# my_label.config(text='New text')

entry = Entry()
entry.grid(column=3, row=2)

def change_label():
    print(entry.get())
    # my_label.config(text=entry.get())

# Buttons

def button_clicked():
    print('I got clicked')
    my_label.config(text='Button got clicked')

button = Button(text='Click Me', command=change_label)
button.grid(column=1, row=1)

button2 = Button(text='New Button')
button2.grid(column=2, row=0)














window.mainloop()