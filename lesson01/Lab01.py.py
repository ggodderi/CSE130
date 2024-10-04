# 1. Name: Brother Godderidge
#    -your name-
# 2. Assignment Name: Lab 01: Guessing Game
#    Lab 01: Python Review
# 3. Assignment Description:  Write a python program to display a message on the screen, prompt the user
#         for information, make a decision, store data in a list, and loop.
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random

# Game introduction.

# Prompt the user for how difficult the game will be. Ask for an integer.

print('This is a "Guess a number" game')
value_max = int(input('Input the maximum positive number for the guessing game: '))
print(f'You will try to guess a random number betwee 1 and {value_max} in the fewest guesses.')

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
done = False
number_of_guesses = 0
guess_array = []

while not done:
    value_guess = int(input(f'Guess a number between 1 and {value_max}: '))
    number_of_guesses += 1
    guess_array.append(value_guess)
    if value_guess > value_random:
        print(f'{value_guess} is too high')
    elif value_guess < value_random:
        print(f'{value_guess} is too low')
    else:
        print(f'Guessed Correctly:  {value_guess} equals the random number of: {value_random}')
        print(f'It took you {number_of_guesses} to guess the correct number')
        print(f'The numbers you guessed were: {guess_array}')
        done = True
