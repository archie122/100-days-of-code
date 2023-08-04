import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter : row.code for (index, row) in data.iterrows()}

error = False

while not error:
    try:
        NATO_word = [NATO_dict[letter] for letter in input("Enter a word: ").upper()]
    except KeyError:
        print("Please enter a valid word.")
    else:
        print(NATO_word)
        error = True