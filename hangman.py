import random

def hangman():
    word_list = ["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream"]
    word = random.choice(word_list)
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessed_letters = ''

    while len(word) > 0:
        display_word = ""
        missed = 0

        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        if display_word == word:
            print(display_word)
            print("You win!")
            break

        print("Guess the word:", display_word)
        guess = input().lower()

        if guess in valid_letters:
            guessed_letters += guess
        else:
            print("Enter a valid character")
            continue

        if guess not in word:
            turns -= 1
            print(f"Incorrect guess. {turns} turns left.")
            if turns == 0:
                print("You lose. The hangman has been hanged!")
                print(f"The correct word was: {word}")
                break
        else:
            print("Correct guess!")

        print_hangman(turns)

def print_hangman(turns):
    hangman_stages = [
        "  ---------  ",
        "      O      ",
        "      |      ",
        "     /|\\    ",
        "     / \\    "
    ]

    print("Hangman:")
    for i in range(5 - turns):
        print(hangman_stages[i])

name = input("Enter your name: ")
print(f"Welcome {name}")
print("=====================")
print("Try to guess it less than 10 attempts")
hangman()
