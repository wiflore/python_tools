import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Dif you mean %s instead?" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doen't exist. Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doen't exist. Please double check it"

word = input('Enter word: ')
output = (translate(word))

check = True

while check:
    if type(output) == list:
        check = False
        for item in output:
            print(item)
    else:
        print(output)
        word = input('\nEnter word: ')
        output = (translate(word))
