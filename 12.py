import re


class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.score = self.calc_score()

    def calc_score(self):
        score = 0
        for card in self.cards:
            if re.match("^[AJQK]$", card):
                score += 0.5
            else:
                score += int(card)
        if score > 10.5:
            score = 0
        return score


def get_info():
    name = input()
    cards = []
    for _ in range(3):
        cards.append(input())

    return Player(name=name, cards=cards)


def rule_a(playerA: Player, playerB: Player):
    if playerA.score == 0:
        print(f"{playerB.name} Win")
        return

    rule_b(playerA, playerB)



def rule_b(playerA: Player, playerB: Player):
    if playerA.score == playerB.score:
        print("Tie")
    elif playerA.score > playerB.score:
        print(f"{playerA.name} Win")
    else:
        print(f"{playerB.name} Win")


def main():
    playerA = get_info()
    playerB = get_info()

    rule_a(playerA, playerB)
    rule_b(playerA, playerB)


if __name__ == '__main__':
    main()
