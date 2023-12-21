def create_path(path_map):
    start, end = input().split(" ")

    if start not in path_map.keys():
        path_map[start] = set()
    path_map[start].add(end)

    if end not in path_map.keys():
        path_map[end] = set()
    path_map[end].add(start)

    return path_map


def find_path(path_map, path, end):
    current_node = path[-1]

    if current_node == end:
        return path

    if len(path) >= len(path_map.keys()):
        return None

    valid_path = []
    for node in path_map[current_node]:
        if node not in path:
            res = find_path(path_map, path + [node], end)
            if res is not None:
                valid_path.append(res)
    valid_path.sort(key=lambda e: len(e))
    if len(valid_path) > 0:
        return valid_path[0]
    return None


def find_path_with_required(path_map, start, end, required_stop):
    left_half = find_path(path_map, [start], required_stop)
    right_half = find_path(path_map, [required_stop], end)

    if left_half is not None and right_half is not None:
        return (left_half + right_half[1:]), required_stop
    return None


def main():
    number_of_path_string, start, end = input().split(" ")
    number_of_path = int(number_of_path_string)

    required_stop_list = input().split(" ")

    path_map = dict()
    for i in range(number_of_path):
        create_path(path_map)

    required_path_list = []
    for required_stop in required_stop_list:
        res = find_path_with_required(path_map, start, end, required_stop)
        if res is not None:
            required_path_list.append(res)

    if len(required_path_list) > 0:
        required_path_list.sort(key=lambda e: len(e[0]))
        best_path = required_path_list[0]
        print(best_path[1])
        print(" ".join(best_path[0]))
    else:
        print("NO")


if __name__ == '__main__':
    main()
