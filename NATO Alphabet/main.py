# NATO phonetic alphabet let us assign one particular word to each
# letter in the alphabet, so we can identify the letter easily.
# The user enters a word and it is decomposed in its letters and
# its corresponding words of the NATO phonetic alphabet.
import pandas as p

NATO_PHONETIC_ALPHABET_FILE_PATH = "nato_phonetic_alphabet.csv"

nato_data = p.read_csv(NATO_PHONETIC_ALPHABET_FILE_PATH)
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
word = input("Enter a word: ")
nato_equivalent = [nato_dict[letter.upper()] for letter in word]
print(nato_equivalent)
