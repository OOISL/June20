#!/usr/bin/env python

import random

def main():
    """Start a Periodic table."""
    print("Guess the Alkali metals!")

    Alkali = [
        "Lithium or lithium",
        "Sodium or sodium",
        "Potassium or potassium",
        "Rubidium or rubidium",
        "Caesium or caesium",
        "Francium or francium",
        ]

    x = random.choice(Alkali)
    guess = None

    while x != guess:

        guess = str(input("What Alkali am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()

