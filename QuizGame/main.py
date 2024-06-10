class QuizGame():

  def __init__(self):
    self.__score = 0
    self.questions = {
        "What is the brain of Computer System??": "cpu",
        "What is used to type in Computer??": "keyboard",
        "What is used to handle cursor in Computer??": "mouse",
        "This program is written in which language??": 'python',
        "What is the extension of Python File??": '.py'
    }

  def increaseScore(self):
    print("Congratulation your answer was correct.")
    print()
    self.__score += 1

  def result(self):
    print("Congratulations you have completed the Test")
    print("You have recieved {} out of 5 marks and got {}%".format(
        self.__score, (self.__score / 5 * 100)))

  def welcome(self):

    play = input("Do you want to play the game??")

    if play != "yes":
      print("Exiting the Game. Thank You")
      quit()
    else:
      print("The game is now Started")
      self.game()

  def game(self):
    import time
    for num, ques in enumerate(self.questions):
      print("Q", num + 1, "- ", ques)
      user_answer = input("Enter the answer ")
      if user_answer == self.questions[ques]:
        self.increaseScore()
        time.sleep(2)
      else:
        print("Wrong Answer")
        print()
        time.sleep(2)


def main():
  print("Welcome to the QUIZ Game")
  player = QuizGame()
  player.welcome()
  player.result()


if __name__ == "__main__":
  main()
