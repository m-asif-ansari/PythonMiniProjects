# Dice Game

### This python program implements a dice game. Here's a step-by-step breakdown of how it works:

### Importing the random module:

The random module is imported to generate random numbers for the dice rolls.

### Setting up the Game:

The diceGame class is defined to represent the game.
It initializes the game with a welcome message (**init**).
The roll() method simulates rolling a dice by generating a random number between 1 and 6.

The player() method takes the number of players as input and stores their names in a list. It then creates a dictionary p_dict to keep track of each player's score, starting with 0 for everyone.

### Playing the Game:

The playerTurn() method handles each player's turn.
It iterates through each player in the p_dict dictionary.
It prompts the player if they want to roll the dice ('y' for yes, 'n' for no).
If the player chooses to roll:
The roll() method is called to get the dice roll result.
If the roll is 1, the player's score is reset to 0, and they are declared "GAME OVER!".
If the roll is not 1, the score is updated by adding the roll value.
The player's current score is updated in the p_dict dictionary.

### Determining the Winner:

The result() method calculates the winner based on the scores in p_dict.
It finds the player with the highest score and declares them the winner.

### Running the Game:

The main() function:
Creates an instance of the diceGame class.
Prompts the user to enter the number of players (between 2 and 10).
Calls the player() method to get the player names.
Calls playerTurn() to play the game.
Calls result() to announce the winner.
