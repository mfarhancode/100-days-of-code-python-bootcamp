import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_move = ''
if choice == 0:
    user_move = 'rock'
    print(rock)
elif choice == 1:
    user_move = 'paper'
    print(paper)
elif choice == 2:
    user_move = 'scissors'
    print(scissors)

moves = ['rock','paper','scissors']
random_move = random.choice(moves)
print("Computer chose:\n")
if random_move == 'rock':
    print(rock)
elif random_move == 'paper':
    print(paper)
elif random_move == 'scissors':
    print(scissors)

result = ''
if user_move == 'rock':
    if random_move == 'paper':
        result = 'You lose'
    elif random_move == 'scissors':
        result = 'You win!'
    else:
        result = "It's a draw"
elif user_move == 'paper':
    if random_move == 'scissors':
        result = 'You lose'
    elif random_move == 'rock':
        result = 'You win!'
    else:
        result = "It's a draw"
elif user_move == 'scissors':
    if random_move == 'rock':
        result = 'You lose'
    elif random_move == 'paper':
        result = 'You win!'
    else:
        result = "It's a draw"

print(result)
