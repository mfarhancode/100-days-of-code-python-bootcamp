import art
import random

def guess_number():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    a,b = 1,100
    ran_num = random.randint(a,b)
    # print('Number to guess is:',ran_num)
    print(f"I'm thinking of a number between {a} and {b}.")
    attempts = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5

    guessed = False
    def check_close(guess, random_number):
        if (random_number-5) < guess < (random_number+5):
            return True
        else:
            return False

    while attempts > 0 and not guessed:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        close = check_close(guess_num, ran_num)
        # print(close)
        if guess_num > ran_num:
            if not close:
                print("Too high.\nGuess again.")
            else:
                print("High.\nClose!!\nGuess again.")
        elif guess_num < ran_num:
            if not close:
                print("Too low.\nGuess again.")
            else:
                print("Low.\nClose!!\nGuess again.")
        else:
            print(f"You got it! The answer was {ran_num}.")
            guessed = True
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses.")
guess_number() 
# print(10<11<30)