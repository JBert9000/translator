import json
from difflib import SequenceMatcher
from difflib import get_close_matches

with open("data.json") as json_file:
    json_data = json.load(json_file)
# data = json.load(open("data.json"))

word = input("Type in a word in English: ")

# takes the user input as an argument and looks through the JSON file for a match.
def translate(word):
    word = word.lower()
    if word in json_data:
        return json_data[word]
    elif len(get_close_matches(word, json_data.keys())) > 0:
        yn = input("Did you mean to write %s instead? Y or N? " % get_close_matches(word, json_data.keys())[0])
        if yn == "y":
            return json_data[get_close_matches(word, json_data.keys())[0]]
        elif yn == "n":
            return "That is not a word. Please double check it."
        else:
            return "Sorry, your query is not understood."
    else:
        print("That is not a word. Please double check it.")

    translate = True

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
