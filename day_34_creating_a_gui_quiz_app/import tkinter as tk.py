# import tkinter as tk

# # Initialize window
# root = tk.Tk()
# root.title("Spinbox on Canvas")

# # Create Canvas
# canvas = tk.Canvas(root, width=300, height=200, bg="white")
# canvas.pack()

# # --- Spinbox 1: Numeric Range ---
# var1 = tk.IntVar(value=10)
# spin1 = tk.Spinbox(root, from_=0, to=100, textvariable=var1)
# # Create_window places the widget at (x, y)
# canvas.create_window(150, 50, window=spin1)

# # --- Spinbox 2: List of Values ---
# var2 = tk.StringVar(value="Option A")
# spin2 = tk.Spinbox(root, values=("Option A", "Option B", "Option C"), textvariable=var2)
# canvas.create_window(150, 100, window=spin2)

# # Optional: Add text to canvas
# canvas.create_text(150, 20, text="Numeric Range", fill="black")
# canvas.create_text(150, 80, text="Option Selector", fill="black")

# root.mainloop()
# python program demonstrating
# Combobox widget using tkinter


import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
ttk.Label(window, text = "GFG Combobox Widget", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()
