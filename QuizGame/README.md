# QuizGame

-- Created a small Quiz Game in Python with OOPs implementations 

This code snippet is a Python program that implements a simple quiz game. Here is a breakdown of the code:

The import time statement is used to include the time module in the program, which provides various time-related functions.

The QuizGame class is defined, which represents the quiz game itself. It has the following methods:

__init__(self): Initializes the QuizGame object with attributes __score set to 0 and questions dictionary containing the quiz questions and their respective answers.
increaseScore(self): Prints a message indicating a correct answer and increments the score by 1.
result(self): Prints a completion message displaying the score achieved in the quiz as a percentage out of 5 marks.
welcome(self): Asks the user if they want to play the game. If the user responds with anything other than "yes", it exits the game; otherwise, it starts the game by calling the game() method.
game(self): Iterates over the quiz questions, asks the user for answers, checks if the answer is correct, increments the score if correct, and prints messages accordingly.
The main() function is defined, which serves as the entry point of the program. It prints a welcome message, creates an instance of the QuizGame class, calls the welcome() method to start the game, and finally calls the result() method to display the final score at the end of the quiz.

The conditional block if __name__ == "__main__": ensures that the main() function is only executed if the script is run directly (not imported as a module).

Overall, this code snippet defines a quiz game application where the user can answer a series of questions, receive feedback on their answers, and see their final score at the end of the quiz.
