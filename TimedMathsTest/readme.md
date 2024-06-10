# Timed Maths Game

### This is a Python program that creates a timed math challenge game. Here's how it works:

    Setup:
        The code imports the random and time modules.
        It defines a class timeMath to manage the game logic.
        Inside timeMath, the __init__ method initializes game settings:
            It prints a welcome message.
            It sets the range of numbers (2-10) for the questions.
            It defines the possible mathematical operations (+, -, *).
            It initializes the wrong counter to track incorrect answers.

    Generating Questions:
        The generateQuestion method is called with the desired number of questions.
        It starts a timer when the method is called.
        Inside a loop for each question:
            It generates two random numbers and a random operation.
            It displays the math problem to the user and gets their input.
            It checks if the user's answer is correct. If it's incorrect, it increments the wrong counter.

    Ending the Game:
        After the loop, the endGame method calculates the final score:
            It adds the total time taken to 3 times the number of incorrect answers.
            It prints the number of questions answered, time taken, number of wrong answers, and the final score.

    Running the Game:
        The main function:
            Creates an instance of the timeMath class.
            Asks the user how many questions they want to play.
            Calls generateQuestion to start the game.
            Calls endGame to display the results.

In essence,
sets up the game, generates random math problems, tracks user responses, calculates a score based on time and mistakes, and then presents the final results.
