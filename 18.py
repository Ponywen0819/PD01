def validate_input(type: int, height: int):
    if (type < 1 or type > 4):
        print('error')
        return False
    if (height % 2 == 0):
        print('error')
        return False
    return True


def printUpTriangle(height: int):
    middle = height - 1
    for h in range(height):
        for j in range(height * 2 - 1):
            if (j <= (middle + h) and j >= (middle - h)):
                print("*", end='')
            else:
                print("#", end='')
        print()


def printDownTriangle(height: int):
    max = height * 2 - 2
    for h in range(height):
        for j in range(height * 2 - 1):
            if (j <= (max - h) and j >= h):
                print("*", end='')
            else:
                print("#", end='')
        print()


def printDiamond(height: int):
    middle = height // 2
    for h in range(height // 2):
        print(" " * (middle - h), end="")
        print("*" * (h * 2 + 1), end='')
        print(" " * (middle - h))
    print("*" * height)
    for h in range(height // 2):
        print(" " * (h + 1), end="")
        print("*" * ((middle - h) * 2 - 1),end='')
        print(" " * (h + 1))



def printFish(height: int):
    middle = height // 2
    for h in range(height // 2):
        print(" " * (middle - h), end="")
        print("*" * (h * 2 + 1), end="")
        print(" " * (middle - h), end="")
        print(" " * (middle - h), end="")
        print("-" * (h))

    print("*" * height, end='')
    print("-" * middle)
    for h in range(height // 2):
        print(" " * (h + 1), end="")
        print("*" * ((middle - h) * 2 - 1), end='')
        print(" " * (h + 1), end="")
        print(" " * (h + 1), end="")
        print("-" * ((middle - h) - 1))


def main():
    type = int(input())
    height = int(input())

    if(validate_input(type, height)):
        if(type == 1):
            printUpTriangle(height)
        elif(type == 2):
            printDownTriangle(height)
        elif(type == 3):
            printDiamond(height)
        else:
            printFish(height)

if __name__ == '__main__':
    main()