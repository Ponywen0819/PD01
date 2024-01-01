def create_path(path_map):
    start, end = list(map(int, input().split()))

    if start not in path_map.keys():
        path_map[start] = set()
    path_map[start].add(end)

    if end not in path_map.keys():
        path_map[end] = set()
    path_map[end].add(start)

    return path_map


def find_path(graph, current, end, visit, path=[]):
    visit[current] = True

    path.append(current)

    if current == end:
        yield path.copy()

    for neighbor in graph[current]:
        if not visit[neighbor]:
            yield from find_path(graph, neighbor, end, visit, path)

    visit[current] = False
    path.pop()


def main():
    number_of_path, start, end = map(int, input().split())
    required_stop_list = set(map(int, input().split()))

    path_map = {}
    for _ in range(number_of_path):
        path_map = create_path(path_map)

    paths = []
    for i in path_map[start]:
        visit = {node: False for node in path_map}
        visit[i] = True

        for path in find_path(path_map, i, end, visit):
            paths.append(path)

    for temp in paths:
        temp.insert(0, start)

    length = [len(temp) for temp in paths]
    if len(paths) == 0:
        print("NO")
    else:
        index = length.index(min(length))
        for village in paths[index]:
            if village in required_stop_list:
                print(village, end=" ")
        print()
        for village in paths[index]:
            print(village, end=" ")


if __name__ == "__main__":
    main()
