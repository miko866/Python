# import important stuff
import json
from difflib import get_close_matches

# load json in data
data = json.load(open("data.json"))

# this w is from [word = input ...]
def translate(w):
    # create all w(word) lower
    w = w.lower()
    if w in data:
        return data[w]
    # if user entered "texas" this will check for "Texas" as well
    elif w.title() in data:
        return data[w.title()]
    # in case user enters words like USA or NATO
    elif w.upper() in data:
        return data[w.upper()]
    # enter a word that is not a json but is similar
    elif len(get_close_matches(w, data.keys())) > 0:
        # get_close_matches(w, data.keys())[0] -> only first index, that is more relevant
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understant your entry."
    else:
        return "The word doesn't exist."


word = input("Enter word: ")

output = translate(word)

# input at two line in bash only when is type(list)
print()
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)