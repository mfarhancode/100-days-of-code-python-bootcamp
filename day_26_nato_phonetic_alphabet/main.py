import pandas
from pathlib import Path

folder_path = Path(__file__).parent
data = pandas.read_csv(f'{folder_path}/nato_phonetic_alphabet.csv')
code_dict = {row.letter:row.code for (index, row) in data.iterrows()}
word = input('Enter a word: ').upper()
code_list=[code_dict[letter] for letter in word if letter.isalpha()]
print(code_list)
