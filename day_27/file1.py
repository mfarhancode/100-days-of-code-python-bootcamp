import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Minsize Example")

# Set the initial size (optional, minsize will still be enforced)
# root.geometry("1000x300") 

# Set the minimum size of the window to 300 pixels wide and 200 pixels high
root.minsize(300, 200)

# Add a label to the window
label = tk.Label(root, text="Try to resize the window smaller than 300x200")
label.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
