'''This program is a guessing game with an infinite number of chances to guess
the correct answer'''

import random

HIGHEST = 1000
ANSWER = random.randint(1, HIGHEST)

print("Please guess a number between 1 and {}: ".format(HIGHEST))
GUESS = int(input())
while GUESS != ANSWER:
    if GUESS < ANSWER:
        print("Please guess higher")
    elif GUESS > ANSWER:
        print("Please guess lower")
    elif GUESS == 0:
        break
    else:
        print("Well done, you guessed it")
    GUESS = int(input())
else:
    print("You got it first time")
