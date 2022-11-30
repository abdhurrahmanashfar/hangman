import random

word_list = ["apple", "mango", "orange", "banana", "avocado"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter : ")


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ["_"] * len(self.word)
        self.number_letters = len(set(word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter : ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses += guess
    
    ask_for_input(guess)