def checkLine(size, checkNumber, player):
    line = 0
    for i in range(size):
        count = 0
        for j in range(size):
            if player[i * size + j] in checkNumber:
                count += 1
                if count == size:
                    line += 1
                    break
            else:
                break

    for i in range(size):
        count = 0
        for j in range(size):
            if player[i + size * j] in checkNumber:
                count += 1
                if count == size:
                    line += 1
                    break
            else:
                break

    count = 0
    for i in range(size):
        if player[i *(size + 1)] in checkNumber:
            count += 1
            if count == size:
                line += 1
                break
        else:
            break
    count = 0
    for i in range(1, size + 1):
        if player[i * (size - 1)] in checkNumber:
            count += 1
            if count == size:
                line += 1
                break
        else:
            break
    return line

def main():
    size = int(input())
    checkCount = int(input())

    metrix1 = input().split(" ")
    metrix2 = input().split(" ")

    selected_list = input().split(" ")
    score1 = checkLine(size, selected_list, metrix1)
    score2 = checkLine(size, selected_list, metrix2)
    if score1 > score2:
        print("A Win")
    elif score2 > score1:
        print("B Win")
    else:
        print("Tie")



main()