import random


class diceGame:

    def __init__(self):
        print("Welcome to the Dice Game")

    def roll(self):
        return random.randint(1, 6)

    def player(self, num):
        self.playerName = []
        for i in range(num):
            print(f"Enter player {i+1} name - ")
            self.playerName.append(input())

        self.p_dict = {i: 0 for i in self.playerName}

    def playerTurn(self):
        for player, score in self.p_dict.items():
            print(player.upper(), "is playing the game")
            while True:

                print("Do you want to role the dice", player, "(y/n) ??")
                if input().lower() == "y":
                    turn = self.roll()
                    print()
                    print("The dice rolled to", turn)
                    if turn == 1:
                        score = 0
                        print("You rolled to 1. GAME OVER!!!!")
                        print()
                        break
                    else:
                        score = score + turn
                        print(player, "Your current score is", score)
                        self.p_dict[player] = score
                else:
                    print()
                    break
                print()

    def result(self):
        playerList, scoreList = list(self.p_dict.keys()), list(self.p_dict.values())
        maxscore = max(scoreList)
        print()
        print(
            "Congratulations the Winner is ",
            playerList[scoreList.index(maxscore)].upper(),
        )


def main():
    game = diceGame()
    while True:
        print("enter the number of players (2-10)")
        p_num = int(input())
        if p_num >= 2:
            game.player(p_num)
            break
        else:
            print("incorrect number of players")

    game.playerTurn()
    game.result()


if __name__ == "__main__":
    main()
