import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name_input = input("Type your name: ").upper()

    try:
        nato_phonetic_name = [nato_phonetic[name_letter] for name_letter in name_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_phonetic_name)


generate_phonetic()
