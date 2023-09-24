import math


def get_coefficient():
    coefficients = []
    for _ in range(3):
        coefficients.append(int(input()))
    return coefficients


def calc_determine(coefficients: list) -> int:
    a, b, c = coefficients
    return (b ** 2) - (4 * a * c)


def print_root(coefficients, det):
    a, b, c = coefficients
    if det < 0:
        det *= -1
        sqrt = math.sqrt(det)
        print(f"{-b / (2 * a):.1f}+{sqrt / (2 * a):.1f}i")
        print(f"{-b / (2 * a):.1f}-{sqrt / (2 * a):.1f}i")

    else:
        sqrt = math.sqrt(det)
        print(f"{(-b + sqrt )/ (2 * a):.1f}")
        print(f"{(-b - sqrt) / (2 * a):.1f}")


def main():
    coefficients = get_coefficient()

    det = calc_determine(coefficients)

    print_root(coefficients, det)


if __name__ == '__main__':
    main()
