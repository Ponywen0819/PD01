import math


class Hydron:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def calcDistence(self, other):
        # print(self, other)
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __str__(self):
        return "%s %s %s" % (self.x, self.y, self.z)

    def __repr__(self):
        return self.__str__()


def calcDistenceList(hydronList: list):
    distancelist = []
    for index, hydron in enumerate(hydronList):
        for i in range(index + 1, len(hydronList)):
            distance = hydron.calcDistence(hydronList[i])
            distancelist.append((hydron, hydronList[i], distance))
    distancelist.sort(key=lambda e: e[2])
    return distancelist


def main():
    numberOfHydron = int(input())
    hydronList = []
    for i in range(numberOfHydron):
        parameter = input().split(" ")
        hydron = Hydron(parameter[0], *[int(x) for x in parameter[1:]])

        hydronList.append(hydron)
    distenceList = calcDistenceList(hydronList)
    print(distenceList[0][0].name, distenceList[0][1].name, distenceList[0][0], distenceList[0][1])
    print(distenceList[1][0].name, distenceList[1][1].name, distenceList[1][0], distenceList[1][1])
    print(distenceList[2][0].name, distenceList[2][1].name, distenceList[2][0], distenceList[2][1])


if __name__ == '__main__':
    main()
