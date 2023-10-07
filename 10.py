def get_one_round() -> list:
    hits = []
    for _ in range(2):
        hits.append(int(input()))
        if hits[0] == 10:
            break
    return hits


def get_info() -> list:
    hits = []
    for _ in range(2):
        hits += get_one_round()
    if hits[-1] == 10:
        hits += get_one_round()
    return hits


def calc_next_score(hits: list):
    score = 0
    for i in range(3):
        if i >= len(hits):
            break
        score += hits[i]
    return score


def calc_one_round(hits: list) -> tuple:
    if hits[0] == 10:
        return (calc_next_score(hits), 1)
    elif hits[0] + hits[1] == 10:
        return (calc_next_score(hits), 2)
    else:
        return (hits[0] + hits[1], 2)


def get_score(hits: list) -> int:
    score = 0
    for _ in range(2):
        info = calc_one_round(hits)
        score += info[0]
        hits = hits[info[1]:]

    return score

def main():
    hits = get_info()
    score = get_score(hits)
    print(score)


main()
