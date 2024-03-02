import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

name_input = input("Type your name: ").upper()

nato_phonetic_name = [nato_phonetic[name_letter] for name_letter in name_input]

print(nato_phonetic_name)
