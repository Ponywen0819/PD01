def dataIn():
    data = [int(input()) for i in range(4)]
    if data[2] == 10:
        data.append(int(input()))
    return data

def dataProcess(data):
    total = 0
    if data[0] + data[1] == 10:
        total += data[0] + data[1] + data[2]
    else :
        total += data[0] + data[1]
    if data[2] == 10:
        total += data[2] + data[3] + data[4]
    else:
        total += data[2] + data[3]
    return total

def main():
    print(dataProcess(dataIn()))


main()