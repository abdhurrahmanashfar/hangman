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
            for i in range(len(word)):
                if guess == word[i]:
                    self.word_guessed[i] = guess
                    number_letters -= 1
                else:
                    num_lives -= 1
        print(f"Sorry, {letter} is not in the word.")
        print(f"You have {num_lives} lives left.")
        list_of_guesses += guess
    

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

def play_game(self, word_list):
    game = Hangman(word_list, self.num_lives)
    while True:
        if self.num_lives == 0:
            print("You lost!")
        elif self.num_letter > 0:
            return ask_for_input()
        elif self.num_lives != 0 and self.num_letters > 0 == False:
            print('Congratulations. You won the game!')

play_game(word)


