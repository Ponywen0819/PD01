def get_path_and_gold(cave_list, start, end, gold, tempAns, final) -> list:
    if start == end:
        return [tempAns[:-1] + [gold]]

    for i in cave_list:
        if i[0] == start:
            for j in i[2:]:
                if j not in tempAns:
                    ans = get_path_and_gold(cave_list, j, end, gold + i[1], tempAns + [j], final)

                else:
                    ans = [tempAns + [gold + i[1]]]

                for t in ans:
                    if t not in final:
                        final.append(t)

    return final


def main():
    nums, start = map(int, input().split())
    cave_list = list(list(map(int, input().split())) for _ in range(int(nums)))

    ans = get_path_and_gold(cave_list, int(start), 0, 0, [start], [])
    max_path = max(ans, key=lambda x: x[-1])

    print(max_path[-1])


if __name__ == "__main__":
    main()
