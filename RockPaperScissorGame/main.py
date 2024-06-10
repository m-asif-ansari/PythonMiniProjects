import random


class rockPaperScissor():

  def __init__(self):
    self.user_score = 0
    self.comp_score = 0
    print("Welcome to Rock/Paper/Scissor Game")

  def cont(self, confirm):
    if confirm.lower() == 'yes':
      print("Rock/Paper/Scissor Game is starting now!!!")
      self.game()
    else:
      self.result()
      quit()

  def game(self):
    print("""Select Rock/Paper/Scissor by typing the following command - 
    1) R/r for Rock
    2) P/p for Paper
    3) S/s for Scissors 
    4) Q/q for QUIT
    """)
    user_input = input()
    if user_input.lower() == 'r':
      self.compare('Rock')
    elif user_input.lower() == 'p':
      self.compare('Paper')
    elif user_input.lower() == 's':
      self.compare('Scissors')
    elif user_input.lower() == 'q':
      self.result()
    else:
      print('Enter correct option')
      self.game()

  def compare(self, value):
    comp_val = random.choice(['Rock', 'Paper', 'Scissors'])

    if value == 'Rock' and comp_val == 'Paper' or value == 'Paper' and comp_val == 'Scissors' or value == 'Scissors' and comp_val == 'Rock':
      self.win()
    elif value == comp_val:
      self.draw()
    else:
      self.lose()

  def curr_score(self):
    print("""
    Current score :
    User Score = {}
    Computer Score = {}
    """.format(self.user_score, self.comp_score))

  def win(self):
    self.user_score += 1
    print("You WIN!!!")
    self.curr_score()
    self.game()

  def lose(self):
    self.comp_score += 1
    print("You Lose!!!")
    self.curr_score()
    self.game()

  def draw(self):
    print("It is a draw!!!")
    self.curr_score()
    self.game()

  def result(self):
    print("""
    Final score :
    User Score = {}
    Computer Score = {}
    """.format(self.user_score, self.comp_score))
    print()
    if self.user_score > self.comp_score:
      print("Congratulation you have won the game!!")
    elif self.user_score == self.comp_score:
      print("It is a Draw")
    else:
      print("You have lose the game!!")


def main():
  rps = rockPaperScissor()
  user_cont = input("Do you want start the game (yes/no)")
  rps.cont(user_cont)


if __name__ == '__main__':
  main()
