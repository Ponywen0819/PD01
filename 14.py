def single_round():
    first = int(input())

    if first == 10:
        return [first]

    second = int(input())
    return [first, second]


def final_round():
    first = int(input())
    second = int(input())

    if first + second >= 10:
        third = int(input())
        return [first, second, third]

    return [first, second]


def record_all():
    scores = []
    for i in range(9):
        scores += single_round()
    scores += final_round()

    return scores


def calc_score(scores: list):
    total = 0
    for _ in range(9):
        score_1 = scores.pop(0)
        total += score_1
        if score_1 == 10:
            total += scores[0] + scores[1]
            continue

        score_2 = scores.pop(0)
        total += score_2
        if score_1 + score_2 == 10:
            total += scores[0]

    for score in scores:
        total += score
    return total

def main():
    scores = record_all()
    total = calc_score(scores)

    print(total)

if __name__ == '__main__':
    main()