
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice string handling, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Word Selection

#### Description
Create a list of words and randomly select one for the player to guess.

#### Requirements
Completed program should:

- Use a predefined list of words.
- Select one word at random for each game.
- Keep the chosen word hidden from the player.

### 🛠️ Guessing Logic

#### Description
Allow the player to guess letters and reveal correct guesses in the word progress display.

#### Requirements
Completed program should:

- Accept single-letter input from the player.
- Show the current progress using placeholders like `_ _ _ _`.
- Reveal correct letters in their proper positions.
- Prevent repeated guesses from changing the game state incorrectly.

### 🛠️ Game State and End Conditions

#### Description
Track wrong guesses and end the game with a win or lose message based on the player's progress.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining.
- End the game when the word is fully guessed or no attempts remain.
- Display a win message if the player guesses the word.
- Display a lose message and reveal the correct word if the player runs out of attempts.
