class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_qstn =  self.question_list[self.question_number]
        self.question_number += 1
        print(f'Q.{self.question_number}: {current_qstn.text}')
        user_ans = input(f'Answer (True/False): ')
        self.check_answer(current_qstn.answer, user_ans=user_ans)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False
    
    def check_answer(self, correct_ans, user_ans):
        if correct_ans.lower() == user_ans.lower():
            print('You got it right!')
            self.score += 1
            
        else:
            print("That's wrong!")
        print(f'The correct answer was {correct_ans}.')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print()

