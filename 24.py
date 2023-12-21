import re

class Player:
    def __init__(self, bet):
        self.bet = bet
        self.score = 0
        self.broken = False

    def get_card(self, new_score: int):
        self.score += new_score
        if self.score > 10.5:
            self.score = 0
            self.broken = True


def creat_players():
    input()
    bets = [int(number) for number in input().split(" ")]

    return [Player(bet) for bet in bets]


def get_score(card: str):
    if re.match("^[JQK]$", card):
        return  0.5
    elif card == "A":
        return 1
    return int(card)


def set_initial_score(players):
    for index, card in enumerate(input().split(" ")):
        score = get_score(card)
        players[index].get_card(score)


def player_round(player):
    while True:
        inputs = input().split(" ")
        option = inputs[0]
        if option == "Y":
            player.get_card(get_score(inputs[1]))
            if player.broken:
                break
            if player.score == 10.5:
                break
        else:
            break


def check_is_end(players):
    for player in players:
        if player.score != 10.5 or player.broken:
            return False
    return True


def computer_round(players):
    computer = players[0]
    players = players[1:]

    lowest_score = min([player.score if not player.broken else 10.5 for player in players])


    while not computer.broken and computer.score <= lowest_score:
        computer.get_card(get_score(input()))


def judge(players):
    computer = players[0]
    players = players[1:]
    computer_earn = 0

    for index, player in enumerate(players):
        is_winning = not player.broken and player.score > computer.score
        finial_earn = (1 if is_winning else -1) * player.bet
        print(f"Player{index + 1} {'+' if finial_earn>0 else ''}{finial_earn}")
        computer_earn += -1* finial_earn

    print(f"Computer {'+' if computer_earn > 0 else '' }{computer_earn}")


def main():
    players = [Player(0)] + creat_players()

    set_initial_score(players)

    for player in players[1:]:
        player_round(player)

    if not check_is_end(players[1:]):
        computer_round(players)

    judge(players)

if __name__ == '__main__':
    main()



