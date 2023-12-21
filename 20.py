def create_matrix(n: int):
    matrix = []
    for i in range(n):
        start = i * n + 1
        matrix.append([n for n in range(start, start + n)])
    return matrix

def handle_operate(operations: str):
    count = {"L": 0, "R": 0}
    for operate in operations:
        count[operate] += 1

    diff = abs(count["L"] - count["R"])

    if count["L"] > count["R"]:
        return ["L", diff]
    else:
        return ["R", diff]


def handle_left(matrix: list):
    size = len(matrix)
    new_matrix = []
    for i in range(size):
        new_matrix.append([ matrix[n][size-i -1] for n in range(size) ])
    return  new_matrix

def handle_right(matrix: list):
    size = len(matrix)
    new_matrix = []
    for i in range(size):
        new_matrix.append([matrix[size - n - 1][i] for n in range(size)])
    return new_matrix

def print_matrix(matrix: list):
    for r in matrix:
        for n in r:
            print(n, end=' ')
        print()
def main():
    size = int(input())
    matrix = create_matrix(size)
    [operations_type, times] = handle_operate(input())

    for _ in range(times):
        if(operations_type == "L"):
            matrix = handle_left(matrix)
        else:
            matrix = handle_right(matrix)


    print_matrix(matrix)

if __name__ == '__main__':
    main()