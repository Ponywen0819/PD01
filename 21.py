import re


def get_cards():
    cards = input().split(" ")
    return cards


def validate_card(cards: list):
    for card in cards:
        number = card[:-1]
        decor = card[-1]
        if not re.match('^[2-9JQKA]$', number) and number != "10":
            return False

        if not re.match("^[HSDC]$", decor):
            return False
    return True


def validate_not_dup(cards: list):
    card_set = set()
    for card in cards:
        card_set.add(card)
    return len(card_set) == 5


def convert_number(cards: list):
    res = []
    for card in cards:
        number = card[:-1]
        if number == "J":
            res.append(f"{11}{card[-1]}")
        elif number == "Q":
            res.append(f"{12}{card[-1]}")
        elif number == "K":
            res.append(f"{13}{card[-1]}")
        elif number == "A":
            res.append(f"{1}{card[-1]}")
        else:
            res.append(f"{number}{card[-1]}")

    return res


def validate_straight_flush(cards: list):
    for card in cards:
        if card[-1] != cards[0][-1]:
            return False
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)
    temp = numbers[0]
    for number in numbers[1:]:
        diff = number - temp
        if diff != -1 and diff != -9:
            return False
        temp = number
    return True


def validate_four_of_kind(cards: list):
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)
    f_same = numbers[0] == numbers[1] == numbers[2] == numbers[3]
    b_same = numbers[1] == numbers[2] == numbers[3] == numbers[4]

    return f_same or b_same


def validate_full_house(cards: list):
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)
    f_same = (numbers[0] == numbers[1] == numbers[2]) and (numbers[3] == numbers[4])
    b_same = (numbers[2] == numbers[3] == numbers[4]) and (numbers[1] == numbers[0])

    return f_same or b_same


def validate_flush(cards: list):
    decors = [card[-1] for card in cards]
    return decors[0] == decors[1] == decors[2] == decors[3] == decors[4]


def validate_straight(cards: list):
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)
    temp = numbers[0]
    for number in numbers[1:]:
        diff = number - temp
        if diff != -1 and diff != -9:
            return False
        temp = number
    return True


def validate_three_of_kind(cards: list):
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)
    f_same = numbers[0] == numbers[1] == numbers[2]
    m_same = numbers[1] == numbers[2] == numbers[3]
    b_same = numbers[2] == numbers[3] == numbers[4]

    return f_same or m_same or b_same


def validate_two_pair(cards: list):
    number_set = set()
    for card in cards:
        number_set.add(card[:-1])

    return len(number_set) == 3


def validate_one_pair(cards: list):
    numbers = sorted([int(card[:-1]) for card in cards], reverse=True)

    return numbers[0] == numbers[1] or numbers[1] == numbers[2] or numbers[2] == numbers[3] or numbers[3] == numbers[4]


def main():
    cards = get_cards()
    if not validate_card(cards):
        print("Error input")
        return
    if not validate_not_dup(cards):
        print("Duplicate deal")
        return

    cards = convert_number(cards)

    if validate_straight_flush(cards):
        print(9)
    elif validate_four_of_kind(cards):
        print(8)
    elif validate_full_house(cards):
        print(7)
    elif validate_flush(cards):
        print(6)
    elif validate_straight(cards):
        print(5)
    elif validate_three_of_kind(cards):
        print(4)
    elif validate_two_pair(cards):
        print(3)
    elif validate_one_pair(cards):
        print(2)
    else:
        print(1)


if __name__ == '__main__':
    main()


'''
JS QS KS AS 2S
10S JS QS KS AS
QS KS AS 2S 3S
KS AS 2S 3S 4S
5S 2S 3S 4S 5S


'''