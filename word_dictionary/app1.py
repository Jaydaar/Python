import json
from difflib import get_close_matches

data = json.load(open("data.json"))
## data contains a dictionary filled with the definition of 49537 words
def translate(find_word):
    find_word = find_word.lower()
    if find_word in data:
        return data[find_word]
    else:
        return "fail"

def get_word():
    word = input("Enter a word: ")
    if word in data.keys():
        use_word(word)
    else:
        close_word = get_close_matches(word, data.keys())
        if len(close_word) > 0:
            ask_which_word(close_word)
        else:
            print("Check over the word and try again...")
            get_word()
    
def use_word(a_word):
    result = translate(a_word)
    show(list(result))

def show(answers):
    size = len(answers)
    for i in range(size):
        print("{} --> {}".format(i + 1, answers[i]))
    print("*" * 50)

def ask_which_word(words_list):
    print("Select the number for the word you wish to use.")
    show(words_list)
    choice = int(input("Which word: "))
    word = words_list[choice - 1]
    show(list(translate(word)))

def main():
    print(len(data.keys()))
    new = True
    while new:
        get_word()
        choice = ["Another Word", "Done"]
        show(choice)
        reply = int(input("What do you want to do? Type the number: "))
        answer = choice[reply - 1]
        if answer == choice[0]:
            continue
        elif answer == choice[1]:
            new = False
        else:
            print("Invalid choice let us start over")

main()

    
