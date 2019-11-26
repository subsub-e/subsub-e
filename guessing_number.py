import random
# The main function of the program
def main():
    solved = False
    guess_count = 0
    num_to_guess = get_num()
    while not solved:
        guess = input("Guess a number: ")
        guess_count += 1
        if guess == num_to_guess:
            print ("\nCongratulations! You Win!\nTook you " + str(guess_count) + " guesses!")
            solved = True
        else:
            give_hint(guess, num_to_guess)

# Generates the number for the user to guess
def get_num():
    high_end = input("What number do you want to guess up to?\n")
    num = str(random.randint(0, int(high_end)))
    print ('\nYou will be guessing a number between 0 - ' + high_end)
    return num

# Checks if the user guessed correctly
def give_hint(guess, num_to_guess):
    if guess < num_to_guess:
        if int(guess) >= int(num_to_guess) - 10:
            print ("you're a little low")
        elif int(guess) >= int(num_to_guess) - 25:
            print ("guess higher")
        else:
            print ("Way too low")

    if guess > num_to_guess:
        if int(guess) <= int(num_to_guess) + 10:
            print ("you're a little high")
        elif int(guess) <= int(num_to_guess) + 25:
            print ("guess lower")
        else:
            print ("Way too high")



if __name__ == "__main__":
    main()