import math


def get_input():
    inputs = []
    for i in range(3):
        inputs.append(int(input()))
    return inputs


def print_info(values: list):
    a, b, c = values
    x_1 = ((-b) + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x_2 = ((-b) - math.sqrt(b * b - 4 * a * c)) / (2 * a)

    print("%.1f" % x_1)
    print("%.1f" % x_2)


def main():
    inputs = get_input()
    print_info(inputs)


if __name__ == '__main__':
    main()
