import random
import time


class timeMath():

  def __init__(self):
    print('welcome to the Timed Challenge')

    self.lowRange = 2
    self.highRange = 10
    self.mathOpers = ['+', '-', '*']
    self.wrong = 0

  def generateQuestion(self, questions):
    print('Your Time has Started now')
    self.startTime = time.time()

    for i in range(questions):
      self.first = random.randint(self.lowRange, self.highRange)
      self.oper = random.choice(self.mathOpers)
      self.last = random.randint(self.lowRange, self.highRange)
      print(f"{self.first} {self.oper} {self.last} = ")
      self.expression = f"{self.first} {self.oper} {self.last}"
      self.result = eval(self.expression)
      self.userInput = int(input('Enter the result for the above expressions'))

      if self.userInput == self.result:
        print('It is correct answer')
      else:
        print("WRONG Answer")
        self.wrong += 1

    self.endTime = time.time() 
    self.timeTaken = self.endTime - self.startTime

  def endGame(self, num):
    self.finalScore = self.timeTaken + (3 * self.wrong)
    print()
    print(f'you have solved {num} Questions in { self.timeTaken:.2f} seconds')
    print()
    print(f'You got { self.wrong } questions wrong')
    print()
    print(f'After calculating penalty your time is { self.finalScore:.2f} seconds')


def main():
  timeGame = timeMath()

  numQuestion = int(
      input("Enter the number of question that you want to play"))

  timeGame.generateQuestion(numQuestion)
  timeGame.endGame(numQuestion)


if __name__ == '__main__':
  main()
