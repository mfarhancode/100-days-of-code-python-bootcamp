from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=100, pady=20)

entry = Entry(width=10)
entry.insert(END, string='0')
entry.grid(column=1, row=0)


def converter():
    km = entry.get()
    mile = int(float(km)* 1.60934)
    label3.config(text=mile)

# mile = converter()

label1 = Label(text='Miles', font=('Arial', 10))
label1.grid(column=2, row=0)

label2 = Label(text='is equal to', font=('Arial', 10))
label2.grid(column=0, row=1)

label3 = Label(text=0, font=('Arial', 10))
label3.grid(column=1, row=1)

label4 = Label(text='Km', font=('Arial', 10))
label4.grid(column=2, row=1)

button = Button(text='Calculate', command=converter)
button.grid(column=1, row=2)


window.mainloop()