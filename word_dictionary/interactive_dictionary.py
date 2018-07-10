
# coding: utf-8

# In[40]:


import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return word.capitalize(), data[word]
    else:
        print("\nThe word does not exist. Please double check it.\n")
        matches = close_match(word) + ['None of the above.']
        print("Which word did you want?")
        for position in range(len(matches)):
            print("\t{}. {}".format(position + 1, matches[position]))
        choice = int(input("Please choose the corresponding number: "))
        word = matches[choice-1]
        return word.capitalize(), data[word]
            
def close_match(word):
    close = get_close_matches(word, data.keys())
    return close

def define(word):
    # Response to the word submitted to search in the dictionary
    word, definitions = translate(word)
    print("\n{}".format(word))
    count = 1
    for definition in definitions:
        print("  {}. {}\n".format(count, definition))
        count+=1

word = input("Enter word: ")
define(word)

