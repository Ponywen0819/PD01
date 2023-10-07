def get_edges() -> list:
    return [int(data) for data in input().split(" ")]


def get_triangle_area(a, b, c):
    edges = [a, b, c]
    edges.sort()

    if edges[0] < 0 or (edges[0] + edges[1]) <= edges[2]:
        print('not a triangle')
        return []

    s = (a + b + c) / 2
    area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)

    if edges[0] == edges[2]:
        print(f"equilateral triangle {area:.2f}")

    elif edges[0] == edges[1] or edges[1] == edges[2]:
        print(f"isosceles triangle {area:.2f}")

    elif edges[0] ** 2 + edges[1] ** 2 < edges[2] ** 2:
        print(f"obtuse triangle {area:.2f}")

    elif edges[0] ** 2 + edges[1] ** 2 > edges[2] ** 2:
        print(f"acute triangle {area:.2f}")

    elif edges[0] ** 2 + edges[1] ** 2 == edges[2] ** 2:
        print(f"right triangle {area:.2f}")

    return [area]


def main():
    number = int(input())
    areas = []
    for _ in range(number):
        edges = get_edges()
        area = get_triangle_area(edges[0], edges[1], edges[2])
        areas+=area

    areas.sort()
    if len(areas) == 0:
        print("All inputs are not triangles!")
    else:
        print(f"{areas[-1]:.2f}")
        print(f"{areas[0]:.2f}")



if __name__ == '__main__':
    main()
