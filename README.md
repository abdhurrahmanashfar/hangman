# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

### Milestone 2

This implementation of Hangman is built using Python, using the base language and the .choice() method from the random library.

A pre-determined list of possible words is supplied, and the random.choice() method is used to choose one word from the list. This is the 'answer' or hidden word in the Hangman game.

The user is then asked to provide a single letter as input, using the Python input() function. This input is assigned to the variable "guess". This occurs in a while loop, such that while the input length is not equal to one, the user is reminded of the input constraints, and re-prompted for a new input.

Once a single-character input is stored in the variable "guess", the .isalpha() method is used in an if statement, to determine whether the single-character guess is alphabetical. If isalpha(guess) returns true, then the user is thanked for their input, otherwise the user is told the guess is invalid.

### Milestone 3:

Two functions are defined:

ask_for_input() - Checks if the input is an alphabeth and in the length of 1.

check_guess() - This function checks the validity of the guess, and feeds it back to the user.

### Milestone 4:

This iteration of the Hangman code defines Hangman as an object class, with various attributes representing the current game state (eg. number of lives remaining, list of previous guesses), and the functions developed in milestone 3 are reproduced as methods inside the class. The game can be started by instantiating a Hangman object, passing it a list of possible words, from which it will choose a random word as the focus of the game.
