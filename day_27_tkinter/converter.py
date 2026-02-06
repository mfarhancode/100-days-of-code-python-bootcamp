import tkinter as tk

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=100, pady=20)

entry = tk.Entry(width=10)
entry.insert(tk.END, string='.0')
entry.grid(column=1, row=0)

def converter():
    try:
        miles = entry.get()
        km = round((float(miles)* 1.60934), 1)
        label2.config(text=f'Kilometers: {km} KM')
    except ValueError:
        label2.config(text='Please enter a number')


label1 = tk.Label(text='Miles:', font=('Arial', 10))
label1.grid(column=0, row=0)

label2 = tk.Label(text='Kilometers: 0 KM', font=('Arial', 10))
label2.grid(column=1, row=1)

button = tk.Button(text='Calculate', command=converter)
button.grid(column=1, row=2)

window.mainloop()