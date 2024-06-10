import random
import time


class GuessNum():

  def __init__(self):
    self.num = random.randint(1, 1000)
    self.ctr = 0

  def guess(self, number: int):
    if self.num == number:
      self.congo()
    elif self.num < number:
      self.low()
    else:
      self.high()
    self.ctr += 1

  def congo(self):
    print("Congratulation you have guessed the number correctly in {} guesses".
          format(self.ctr + 1))
    exit()

  def low(self):
    print("The number is lower than what you have entered")

  def high(self):
    print("The number is higher than what you have entered")


def main():
  print("The Number is being generated")
  time.sleep(5)

  genNum = GuessNum()
  while (True):
    user_number = int(input("Guess The Number- "))
    genNum.guess(user_number)


if __name__ == '__main__':
  main()
