def round(num):
    num *= 1000
    last = int(num % 10)
    if (last > 5):
        num += 10
    elif last == 5 and int(num / 10) % 10 % 2 == 1:
        num += 10

    num = int(num / 10)

    return num / 100


def get_bmi():
    h, w = [float(data) for data in input().split(" ")]
    bmi = w / (h ** 2)
    return round(bmi)


def record_bmi():
    number = int(input())
    bmis = []
    for _ in range(number):
        bmis.append(get_bmi())
    bmis.sort()
    return bmis


def print_max(bmis):
    print(f"{bmis[-1]:.2f}")


def print_min(bmis):
    print(f"{bmis[0]:.2f}")


def print_middle(bmis):
    middle = len(bmis) // 2
    if len(bmis) % 2 == 0:
        print(f"{round((bmis[middle] + bmis[middle - 1]) / 2):.2f}")
    else:
        print(f"{bmis[middle]:.2f}")


def print_many(bmis):
    time_record = {}
    for bmi in bmis:
        if bmi in time_record.keys():
            time_record[bmi] += 1
        else:
            time_record[bmi] = 1

    max = 0
    val = 0
    for bmi in bmis:
        if (time_record[bmi] > max):
            max = time_record[bmi]
            val = bmi
    print(f"{val:.2f}")


def main():
    bmis = record_bmi()
    print_max(bmis)
    print_min(bmis)
    print_middle(bmis)
    print_many(bmis)


if __name__ == '__main__':
    main()
