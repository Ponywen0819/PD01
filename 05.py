def get_edges() -> list[int]:
    edges = []
    for _ in range(3):
        edges.append(int(input()))
    return edges


def getTriangle(a, b, c):
    edges = [a, b, c]
    edges.sort()

    if edges[0] < 0 or (edges[0] + edges[1]) <= edges[2]:
        return "not a triangle"

    if edges[0] == edges[2]:
        return "equilateral triangle"

    if edges[0] == edges[1] or edges[1] == edges[2]:
        return "isosceles triangle"

    if edges[0] ** 2 + edges[1] ** 2 < edges[2] ** 2:
        return "obtuse triangle"

    if edges[0] ** 2 + edges[1] ** 2 > edges[2] ** 2:
        return "acute triangle"

    if edges[0] ** 2 + edges[1] ** 2 == edges[2] ** 2:
        return "right triangle"


def main():
    edges = get_edges()
    result = getTriangle(edges[0], edges[1], edges[2])

    print(result)


if __name__ == '__main__':
    main()
