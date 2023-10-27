def print_left_triangle(height: int):
    for h in range(height):
        for l in range(h + 1):
            print(l + 1, end='')
        for r in range(h,0, -1):
            print(r , end='')
        print()

def print_up_triangle(height: int):
    for h in range(height):
        print("_"*(height -h -1),end='')
        for l in range(h + 1):
            print(l + 1, end='')
        for r in range(h,0, -1):
            print(r , end='')
        print("_"*(height -h -1),end='')

        print()

def print_down_triangle(height: int):
    for h in range(height -1, -1,-1):
        print("_"*(height -h -1),end='')
        for l in range(h + 1):
            print(l + 1, end='')
        for r in range(h,0, -1):
            print(r , end='')
        print("_"*(height -h -1),end='')
        print()


def main():
    type = int(input())
    height = int(input())

    if(type == 1):
        print_left_triangle(height)
    elif(type == 2):
        print_up_triangle(height)
    elif(type == 3):
        print_down_triangle(height)

if __name__ == '__main__':
    main()
