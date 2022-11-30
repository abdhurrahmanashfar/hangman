import random

word_list = ["apple", "mango", "orange", "banana", "avocado"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter : ")


def check_guess(guess):
    guess = guess.lower()
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while guess.isalpha() == True and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()




