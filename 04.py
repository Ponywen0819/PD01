import decimal


def get_height() -> float:
    return float(input())


def get_weight() -> int:
    return int(input())


def calc_bmi(height, weight) -> float:
    return weight / (height ** 2)


def round_rr(value: float):
    string = str(value)
    integers, decimal = string.split(".")

    if len(decimal) < 3:
        print(f"{value:.2f}")

    if decimal[2] == '5':
        if int(decimal[2]) % 2:
            print(f"{integers}.{decimal[:2]}")
            return
        else:
            value = float(f"{integers}.{decimal[:2]}")
            print(value + 0.01)
            return
    print(round(value, 2))


def main():
    height = get_height()
    weight = get_weight()

    bmi = calc_bmi(height, weight)

    round_rr(bmi)


if __name__ == '__main__':
    main()