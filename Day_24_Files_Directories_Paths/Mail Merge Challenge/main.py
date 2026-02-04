from pathlib import Path

folder_path = Path(__file__).parent
# print(folder_path)

with open(f"{folder_path}/Input/Letters/starting_letter.txt") as starting_letter:
    content_letter = starting_letter.read()

with open(f"{folder_path}/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.read().split('\n')
    for name in names:
        # print(name)
        with open(f"{folder_path}/Output/ReadyToSend/letter_for_{name}", mode='w') as new_letter:
            new_letter.write(content_letter.replace('[name]', name))
