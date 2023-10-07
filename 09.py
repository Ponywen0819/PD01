def get_line_info() -> tuple:
    x_1 = int(input())
    x_2 = int(input())

    return (x_1, x_2)


def get_lines_info() -> list:
    res = []
    for _ in range(3):
        res.append(get_line_info())
    return res

def merge_lines(lines: list):
    coverage = set()
    for line in lines:
        for i in range(line[0], line[1]):
            coverage.add(i)
    return coverage


def main():
    lines = get_lines_info()
    coverage = merge_lines(lines)

    print(len(coverage))

main()