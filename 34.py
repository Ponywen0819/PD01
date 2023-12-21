def record_relation(relation_map, relation):
    source, to, weight = relation.split(" ")
    if source not in relation_map.keys():
        relation_map[source] = dict()

    relation_map[source][to] = int(weight)
    return relation_map


def find_min_depth(relation_map, path, to):
    current_node = path[-1]

    if current_node == to:
        return path

    if len(path) >= len(relation_map.keys()):
        return None

    for node in relation_map[current_node].keys():
        if node not in path:
            res = find_min_depth(relation_map, path + [node], to)
            if res is not None:
                return res
    return None


def find_max_weight(relation_map, path, to, weight):
    current_node = path[-1]

    if current_node == to:
        return weight, path

    if len(path) >= len(relation_map.keys()):
        return None

    weight_list = []
    for node in relation_map[current_node].keys():
        if node not in path:
            res = find_max_weight(relation_map, path + [node], to,
                                  weight + min(relation_map[current_node][node], relation_map[node][current_node]))
            if res is not None:
                weight_list.append(res)

    if len(weight_list) > 0:
        weight_list.sort(key=lambda e: e[0])
        return weight_list[-1]

    return None


def main():
    number_of_people = int(input())
    relation_map = dict()
    while 1:
        relation = input()
        if relation == "-1":
            break
        record_relation(relation_map, relation)

    # print(relation_map)
    min_depth = find_min_depth(relation_map, ["A"], "B")
    # print(min_depth)
    print(len(min_depth) - 1)
    print(" ".join(min_depth))
    max_weight = find_max_weight(relation_map, ["A"], "B", 0)
    # print(max_weight)
    print(max_weight[0])
    print(" ".join(max_weight[1]))


if __name__ == '__main__':
    main()
