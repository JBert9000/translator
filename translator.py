import json
from difflib import SequenceMatcher
from difflib import get_close_matches

with open("data.json") as json_file:
    json_data = json.load(json_file)
# data = json.load(open("data.json"))


# takes the user input as an argument and looks through the JSON file for a match.
def translate(word):
    word = word.lower()
    if word in json_data:
        return json_data[word]
    else:
        print("That is not a word. Please double check it.")

word = input("Type in a word in English: ")

print(translate(word))
