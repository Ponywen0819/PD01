import re


def get_card():
    card = input()
    if re.match("^[JQK]$", card):
        return 5

    elif card == "A":
        return 10
    else:
        return int(card) * 10


def main():
    user = get_card()
    computer = get_card()

    user_continue = True
    computer_continue = True

    while user_continue or computer_continue:
        if user_continue:
            option = input()
            if option == "Y":
                user += get_card()
                if user > 105:
                    user = 0
                    break
            else:
                user_continue = False

        # computer_continue = computer_continue and( computer < user or computer <= 80)
        computer_continue =  computer <= 80
        if computer_continue:
            computer += get_card()
            if computer > 105:
                computer = 0
                break

    if user == computer:
        print("it's a tie")
    elif user > computer:
        print("player win")
    else:
        print("computer win")


if __name__ == '__main__':
    main()
