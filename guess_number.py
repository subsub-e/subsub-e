# generate random number.
import random

number = random.randrange(0, 101)

# initialize guesses
guesses = 5
win = False  # to break while loop

while win == False:

    guesses -= 1

    user_guess = int(input('Guess the random number: '))
    if user_guess > number:
        print('Your guess was too high. You have,', guesses, 'left.')
    elif user_guess < number:
        print('Your guess was too low. You have,', guesses, 'left.')
    else:
        print('Yay! You guessed the correct number', number)
        win = True

    if guesses == 0 and win == False:  # Both need to be true for user to lose.
        print('Sorry, you lose. The correct number was', number)

### End ###