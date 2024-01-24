#!/usr/bin/env python3

#######
# Print the debug messages only if script is called with argument (`python3 hangman.py --debug`)
import sys
DEBUG = False
for arg in sys.argv:
    if (arg == "--debug"): DEBUG = True
def print_debug(string):
    if DEBUG: print(string)
#######

# deneme

def parse_file(filename):
    print_debug("parse_file: Called... Filename is " + filename)
    name_list = list(()) # empty list

    # TODO(weltas): Open `filename` file. Read it line by line in a loop. (https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python)
    a= open('wordlist.txt', 'r')
    lines = a.readlines()
    # bu lines ın tipi ne oldu acaba? liste tipi mi oldu acep? bunlara bak
    count = 0
    for line in lines
        count = count + 1
        
    

    # TODO(weltas): In the loop, append each read name to `name_list` and return the list. (https://www.w3schools.com/python/python_lists_add.asp)

    print_debug("parse_file: Done, " + str(len(name_list)) + " elements in list.")
    return name_list

def pick_random_name(name_list):
    print_debug("pick_random_name: Called...")
    
    name = ""

    # TODO(weltas): Pick and return a random name from `name_list` (https://pynative.com/python-random-choice)

    print_debug("pick_random_name: Picked the name " + name)
    return name

def print_game_state(picked_name, guessed_state):
    string = ""
    for (letter, guessed) in zip(picked_name, guessed_state):
        # `zip` function iterates the letters in `picked_name` and booleans in `guessed_state` together
        # If the letter is guessed (True), print the letter. If not (False), print underscore "_".
        # e.g. `picked_name` is "çükübik", player guessed letter "ü": print "_ ü _ ü _ _ _"
        if guessed:
            string += " " + letter
        else:
            string += " _"
    print(string)

def victory():
    sys.exit("Congratulations! You won!")

def defeat(picked_name):
    sys.exit("You lost :( Name was " + picked_name)

def game_loop(picked_name):
    print_debug("game_loop: Called...")
    
    # Game state is kept as a list of booleans for each letter in order.
    # e.g. `picked_name` is "çükübik"; game_state is `[False, False, False, False, False, False, False]`
    #      Player guesses the letter "ü"; game state becomes `[False, True, False, True, False, False, False]`
    guessed_state = [False] * len(picked_name)
    left_num_guesses = 7

    # Loop until there are no guesses left
    while left_num_guesses > 0:
        print("Number of guesses left: " + str(left_num_guesses))
        print_game_state(picked_name, guessed_state)
        
        # TODO(weltas): Get a single letter input from the player (https://www.geeksforgeeks.org/how-to-take-only-a-single-character-as-an-input-in-python)
        
        # `enumerate` iterates every letter in `picked_name` with its number index
        for index, letter_in_name in enumerate(picked_name):
            # TODO(weltas): if `letter_in_name` is the guessed letter, change `game_state[index]` to True.
            # TODO(weltas): if guessed letter is none of the letters in name, decrement `left_num_guesses` by 1.
            pass # TODO(weltas): Delete `pass` after you write some code in the for loop.

        # Print victory message and quit if all letters are guessed (all of `game_state` is True)
        if all(guessed_state): victory()
    
    # Number of guesses depleted.
    defeat(picked_name)

def main():
    print("Welcome to Hangman!")
    name_list = parse_file("wordlist.txt")
    picked_name = pick_random_name(name_list)
    game_loop(picked_name)

# Call main function
main()
