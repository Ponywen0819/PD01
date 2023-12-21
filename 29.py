def circuit(num, times):
    if (num == 0) or (num == 1):
        return times
    elif num % 2 == 0:
        return circuit(num / 2, times + 1)
    else:
        return circuit((num + 1) / 2, times + 1)


def main():
    while 1:
        initial_num = int(input(), 2)
        times = circuit(initial_num, 0)
        print(bin(times)[2:].zfill(4))
        option = input()
        if option == "-1":
            break


if __name__ == '__main__':
    main()
