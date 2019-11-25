import random

bunchofwords = ["tomato", "banana", "keyboard", "wind", "cat",
                "number", "water", "apple", "music", "drill", "palace", "swerve", "give", "game",
                "mouse", "elephant", "dog", "turtle", "glasses", "phone", "rhythm"]
secret_word = random.choice(bunchofwords)
chances = int(len(secret_word) + 2)
guessed = []
wrong = []

print("Welcome to the Hangman Game.  You will have to guess the hidden word represented by the underscores.  "
      "You get as many chance as letters in the word plus 2.  Good Luck!")

while chances > 0:

    failed = 0

    out = ""
    for letter in secret_word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_ "
            failed = failed + 1
    if failed == 0:
        break

    print("The word: " + out)
    print("You have already guessed: " + str(wrong))
    print("You have " + str(chances) + " chances left.")
    guess = (input("Please enter a letter or word guess: ")).lower()

    if guess == secret_word:
        break
    elif guess in guessed or guess in wrong:
        print("You already guessed that.")
    elif guess in secret_word:
        print("Nice guess!")
        guessed.append(guess)
    else:
        print("Sorry, that's not in the word.")
        chances = chances - 1
        wrong.append(guess)
    print("")

print("")
if chances:
    print("You guessed the word! The word was " + secret_word + ".")
else:
    print("You lost. The word was " + secret_word + ".")