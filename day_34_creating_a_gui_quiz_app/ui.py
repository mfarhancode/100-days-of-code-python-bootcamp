from tkinter import *
from quiz_brain import QuizBrain
from pathlib import Path

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        
        self.question_number = Label(text=f'Q: 0/{self.quiz.total_questions}', font=("Courier", 14), bg=THEME_COLOR, fg='white')
        self.question_number.grid(row=0, column=0)

        self.score_label = Label(text='Score: 0', font=("Courier", 14), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text((150, 125),
                                     text='',
                                     width=280,
                                     fill=THEME_COLOR,
                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        image_folder = Path(__file__).parent.joinpath('images')
        true_img = PhotoImage(file=f'{image_folder}/true.png')
        false_img = PhotoImage(file=f'{image_folder}/false.png')

        # self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.which_button("True"))
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=1)

        # self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.which_button("False"))
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.question_number.config(text=f"Q: {self.quiz.question_number+1}/{self.quiz.total_questions}")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    # def which_button(self, false_or_true):
    #     self.check_answer(false_or_true)
    #
    # def check_answer(self, ans):
    #     self.quiz.check_answer(ans)

    def true_pressed(self):
        is_right =  self.quiz.check_answer('True')
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

