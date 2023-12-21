import re


def replace(string:str, old, new):
    tokens = string.split(" ")
    res = []
    for token in tokens:
        if token.lower() == old.lower():
            res.append(new)
        else:
            res.append(token)
    return  " ".join(res)
def main():
    a = input()
    b = input()
    x = input()
    y = input()

    c = f'{a} {b}'
    print(c)

    pattern = f"(?=\\s){x}(?= )"
    d = replace(c, x, y)
    print(d)
    c_without_space = c.replace(" ", "")
    d_without_space = d.replace(" ", "")
    print(len(c_without_space), len(d_without_space))
    e = replace(c, x, y[::-1])
    print(e)
    step = abs(len(x) - len(y))
    last = ""
    count = step - 1
    for char in c:
        if count == step - 1:
            count = 0
            if last != " " or char != " ":
                print(char, end='')
                last = char
        else:
            count += 1
    print()


if __name__ == '__main__':
    main()

