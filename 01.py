def get_input():
    inputs = []
    for i in range(5):
        inputs.append(input())
    return inputs


def get_total(values: list):
    result = 0
    for score in [int(value) for value in values[2:]]:
        result += score
    return result


def print_info(values: list):
    print(f"Name:{values[0]}")
    print(f"ID:{values[1]}")
    print(f"Average:{values[2]:.0f}")
    print(f"Total:{values[3]}")


def main():
    inputs = get_input()
    total = get_total(inputs)
    print_info([inputs[0], inputs[1], total/3, total])


main()
