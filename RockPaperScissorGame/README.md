# RockPaperScissorGame

This Python code snippet defines a simple Rock-Paper-Scissors game implemented through a class named rockPaperScissor. Here's an explanation of the code snippet:

The code starts by importing the random module, allowing random selection of choices for the game.

A class rockPaperScissor is defined, representing the Rock-Paper-Scissors game.

The constructor __init__ initializes two instance variables user_score and comp_score to 0, and prints a welcome message for the game.

The cont method takes user input to start the game. If the user confirms by typing 'yes', it starts the game by calling the game method; otherwise, it displays the final result and exits the game.

The game method prompts the user to select Rock, Paper, or Scissors by typing the corresponding commands (R/r, P/p, S/s). It then compares the user's choice with the computer's choice (randomly selected) by calling the compare method.

The compare method determines the game result based on the user's choice and the computer's choice. If the user wins, it calls the win method; if there is a draw, it calls the draw method; otherwise, it calls the lose method.

The curr_score method prints the current score of the user and computer.

The win, lose, and draw methods handle the scenarios when the user wins, loses, or there is a draw, respectively. They update the scores and display messages accordingly.

The result method prints the final scores and declares the winner based on the comparison of user and computer scores.

The main function creates an instance of the rockPaperScissor class, asks the user if they want to start the game, and initiates the game based on the user's response by calling the cont method.

Finally, the script checks if it is being run directly (not imported as a module) and calls the main function to start the game if that's the case.

Feel free to run this code in your Python environment to play the Rock-Paper-Scissors game!
