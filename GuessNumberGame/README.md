# GuessNumberGame

This code snippet is a Python program that allows a user to play a number guessing game. Here's a breakdown of the key components:

Import Statements:

The program starts by importing the random and time modules in order to generate random numbers and introduce delays in the program.
GuessNum Class:

This class defines the logic for the number guessing game.
__init__(self) method initializes the num attribute with a random integer between 1 and 1000, and sets the ctr (counter) to 0.
guess(self, number: int) method receives a user's guessed number and compares it with the randomly generated number (num attribute).
If the guessed number matches the generated number, it calls the congo() method to congratulate the user.
If the guessed number is lower than the generated number, it calls the low() method.
If the guessed number is higher than the generated number, it calls the high() method.
Finally, it increments the counter (ctr) by 1.
congo(self) method prints a congratulatory message with the number of guesses made and exits the program.
low(self) method prints a message indicating that the guessed number is lower than the actual number.
high(self) method prints a message indicating that the guessed number is higher than the actual number.

Main Function:

The main() function is where the number guessing game is conducted.
It starts by printing a message indicating that the number is being generated and then pauses execution for 5 seconds using time.sleep(5).
It creates an instance of the GuessNum class.
It enters a while loop that continues indefinitely.
Within the loop, it prompts the user to input a guessed number.
It then calls the guess() method on the genNum instance to process the user's input.
Execution:

The code checks if it is being run as the main script using if __name__ == '__main__': and then calls the main() function to start the game.
Overall, this code snippet implements a simple number guessing game where the user is asked to guess a randomly generated number between 1 and 1000, and the program provides feedback based on the user's inputs until the correct number is guessed.
