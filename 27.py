import re


def is_left_parentheses(char):
    return re.match("[{\[(]$", char) is not None


def is_right_parentheses(char):
    return re.match("[}\])]$", char) is not None


def is_pair(l, r):
    return re.match("\[\]|\(\)|{}", f"{l}{r}") is not None


class Node:
    def __init__(self):
        self.parent = None
        self.value = ""
        self.children = []

    def set_value(self, value):
        self.value = value

    def add_children(self, child):
        self.children.append(child)


def build(string):
    parentheses_stack = []
    node_stack = []
    value_stack = []
    current = None

    for i, c in enumerate(string):
        if is_left_parentheses(c):
            parentheses_stack.append((c, len(value_stack)))
            if current:
                node_stack.append(current)
            current = Node()
        elif is_right_parentheses(c):
            left = parentheses_stack.pop()
            if is_pair(left[0], c):
                current.set_value("".join(value_stack[left[-1]:]))
                value_stack = value_stack[:left[-1]]

                if len(node_stack) != 0:
                    parent = node_stack.pop()
                    parent.add_children(current)
                    current = parent
            else:
                raise Exception()
        else:
            value_stack.append(c)

    if len(node_stack) != 0:
        raise Exception()

    return current


def getvalue(node, depth, curr):
    if depth == curr:
        return node.value

    res = ""
    for c in node.children:
        res += getvalue(c, depth, curr + 1)
    return res


def main():
    number = int(input())
    depth = int(input())
    for _ in range(number):
        string = input()
        try:
            nodes = build(string)

            res = getvalue(nodes, depth, 1)
            print(f"pass, {'EMPTY' if res == '' else res}")
        except:
            print("fail")


if __name__ == '__main__':
    main()
