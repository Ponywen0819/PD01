def get_line_number():
    number = int(input())
    return number


def get_line_info():
    x_1, x_2 = input().split(" ")
    x_1 = int(x_1) + 20
    x_2 = int(x_2) + 20

    return x_1, x_2


def get_coverage(lines):
    coverage = set()
    for line in lines:
        for i in range(line[0], line[1]):
            coverage.add(i)

    return len(coverage)


def main():
    number = get_line_number()
    lines = []
    for _ in range(number):
        lines.append(get_line_info())
    coverage = get_coverage(lines)

    print(coverage)

if __name__ == '__main__':
    main()
