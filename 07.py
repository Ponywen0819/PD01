def get_data():
    data = []
    for _ in range(6):
        data.append(int(input()))

    return data


type_a = [0.08, 0.139, 0.135, 1.128, 1.483, 1, 250, 183]
type_b = [0.07, 0.13, 0.121, 1.128, 1.483, 3, 200, 383]
type_c = [0.06, 0.108, 0.101, 1.128, 1.483, 5, 150, 983]
type_d = [0.05, 0.1, 0.09, 1.128, 1.483, 0, 0, 1283]


def calc_payment(type: list[float], data: list[int]) -> float:
    money = 0
    for i in range(5):
        money += data[i] * type[i]
    if data[5] > type[5]:
        money += (data[5] - type[5]) * type[6]

    if money < type[7]:
        return type[7]
    return money


def print_best(payment: list[float]):
    min = payment[0]
    min_index = 0
    for index, pay in enumerate(payment):
        if pay < min:
            min = pay
            min_index = index
    print(int(payment[min_index]))
    print(['183', "383", "983", "1283"][min_index])


def main():
    data = get_data()
    payment_a = calc_payment(type_a, data)
    payment_b = calc_payment(type_b, data)
    payment_c = calc_payment(type_c, data)
    payment_d = calc_payment(type_d, data)

    payment = [payment_a, payment_b, payment_c, payment_d]
    print_best(payment)


if __name__ == '__main__':
    main()
