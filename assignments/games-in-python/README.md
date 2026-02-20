
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the core game structure by defining a word list and writing logic to randomly select a word at the start of each game.

#### Requirements
Completed program should:

- Define a list of at least 10 words for the game to use
- Randomly select one word at the start of each game using the `random` module
- Initialize tracking variables for guessed letters and remaining attempts


### 🛠️ Implement Game Loop and User Input

#### Description
Write the main game loop that accepts letter guesses from the player, updates the display, and tracks progress until the game ends.

#### Requirements
Completed program should:

- Display the current word progress using underscores (e.g. `_ _ _ _`) and reveal correctly guessed letters
- Accept a single letter guess from the player each turn
- Track incorrect guesses and decrement remaining attempts accordingly
- End the game when the word is fully guessed or the player runs out of attempts
- Display an appropriate win or lose message at the end
