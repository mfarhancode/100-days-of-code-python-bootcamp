from tkinter import *
import tkinter.messagebox as messagebox
import math
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
sessions = 0 # work session + break sessions
timer = None
focus_session = 0 # set of four work sessions
marks = ''
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label.config(text='Timer', fg=GREEN)

    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    global sessions, marks
    marks = ''
    sessions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global sessions

    sessions += 1
    check_marks.config(text=marks)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if sessions % 8 == 0:
        count_down(long_break_sec)
        label.config(text='Break', fg=RED)
    elif sessions % 2 == 0:
        count_down(short_break_sec)
        label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)

        label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global sessions, marks
        if sessions % 2 == 0:
            marks += '⏰' # for break
            if sessions % 8 == 0:
                marks += '\n'
        else:
            marks += '✔' # for break
        check_marks.config(text=marks)
        messagebox.showinfo("Pomodoro | Notification",  "Session is done!\nClick Ok to move to next session.")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_path = Path(__file__).parent / 'tomato.png'
tomato_img = PhotoImage(file=image_path)
canvas.create_image((100, 112), image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold') )
# count_down(5)

canvas.grid(row=1, column=1)

# Label

label = Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 30, 'bold'), fg=GREEN)
label.grid(row=0, column=1)

# Check marks
info_text = '''✔ = Work Session Done
⏰ = Break Session Done'''
info = Label(text=info_text, bg=YELLOW, fg=GREEN, font=(50))
info.grid(row=3, column=1)

check_marks = Label(text='', bg=YELLOW, fg=GREEN, font=(20))
check_marks.grid(row=4, column=1)

# Buttons
start_btn = Button(text='Start', font=("Arial", 10), highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text='Reset', font=("Arial", 10), highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)













window.mainloop()