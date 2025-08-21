import pandas

data = pandas.read_csv('DAY 26/NATO-alphabet-start/nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for index,row in data.iterrows()}

user_input = input('Write any Word ? ').upper()

print([data_dict[letter] for letter in user_input])