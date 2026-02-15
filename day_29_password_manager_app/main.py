from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
from pathlib import Path

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = list(letters) + list(letters.upper())
    numbers = list('0123456789')
    symbols = list('!#$%&()*+')

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo('Password Manager', 'Password copied to clipboard')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def check_data(website, email):
    file_path = Path(__file__).parent.joinpath('data.txt')
        # check if email and website already exists
    with open(file_path, 'r') as data:
        for line in data:
            # print(line.strip('\n'))
            web = line.split('|')[0].strip()
            eml = line.split('|')[1].strip()
            if web == website and eml == email:
                return True
    return False


def overwrite_data(website, email, password):
    file_path = Path(__file__).parent.joinpath('data.txt')
    update_pass = messagebox.askokcancel(title=website, message=f'You have already added this website before with same email/username. Do you want to overwrite/update the password?')
    if update_pass:
        with open(file_path, 'r') as data:
            lines = data.readlines()
        with open(file_path, 'w') as data:
            for line in lines:
                if website in line and email in line:
                    data.write(f'{website} | {email} | {password}\n')
                else:
                    data.write(line)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo('Password Manager', 'Data saved succesfully')
        return #return after updating
    else:
        return # return without overwriting



def add_data():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title='Error', message='Please enter website')
    elif len(email) == 0:
        messagebox.showinfo(title='Error', message='Please enter email')
    elif len(password) == 0:
        messagebox.showinfo(title='Error', message='Please enter password')
    else:
        file_path = Path(__file__).parent.joinpath('data.txt')
        # check if email and website already exists
        if check_data(website, email):
            overwrite_data(website, email, password)
            return



        # with open(file_path, 'r') as data:
        #     for line in data:
        #         # print(line.strip('\n'))
        #         web = line.split('|')[0].strip()
        #         eml = line.split('|')[1].strip()
        #         if web == website and eml == email:
        #             update_pass = messagebox.askokcancel(title=website, message=f'You have already added this website before with same email/username. Do you want to overwrite/update the password?')
        #             if update_pass:
        #                 with open(file_path, 'r') as data:
        #                     lines = data.readlines()
        #                 with open(file_path, 'w') as data:
        #                     for line in lines:
        #                         if web in line and eml in line:
        #                             data.write(f'{website} | {email} | {password}\n')
        #                         else:
        #                             data.write(line)
        #                 website_entry.delete(0, END)
        #                 password_entry.delete(0, END)
        #                 messagebox.showinfo('Password Manager', 'Data saved succesfully')
        #                 return #return after updating
        #             else:
        #                 return # return without overwriting

        # add new data
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open(file_path, 'a') as data:
                data_to_add = f'{website} | {email} | {password}\n'
                data.write(data_to_add)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo('Password Manager', 'Data saved succesfully')

# print(f)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
# print(Path.cwd())
logo_path = Path(__file__).parent.joinpath('logo.png')
# print(logo_path)
logo = PhotoImage(file=logo_path)
canvas.create_image((100,100),image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text='Website:', font=("Arial", 10))
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=("Arial", 10))
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=("Arial", 10))
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=52)
email_entry.insert(0, 'name@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons

generate_pass_btn = Button(text='Generate Password', command=generate_password)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=44, command=add_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()