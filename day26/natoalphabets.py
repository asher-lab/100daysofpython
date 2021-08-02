
#TODO Create a dictionary from CSV
import pandas as pd
dict = {row.letter : row.code for index, row in pd.read_csv("nato_phonetic_alphabet.csv").iterrows()}
print(dict)
#TODO Create a list of phonetic code words from
user_input = input("What is your name?:     ").upper()
print(f"Nato Alphabet Equivalent:\n")
input_present = [dict[letter] for letter in user_input]
print(input_present)
