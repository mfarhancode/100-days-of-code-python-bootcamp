from question_model import Question
import data
from quiz_brain import QuizBrain
from ui import QuizInterface

data.window.mainloop()

question_bank = []
for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
