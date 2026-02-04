from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q['text'], q['answer']) for q in question_data]

quiz_brain = QuizBrain(question_list=question_bank)

quiz_brain.next_question()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")