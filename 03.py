def get_input():
    res = []
    for i in range(2):
        res.append(input())
    return res


def generate_formula(inputs: list):
    num1, num2 = inputs
    res = []
    for operator in ["+", "-", "*", "/"]:
        res.append(f"{num1}{operator}{num2}")
    return res


def is_operator(char: str):
    return char in ["+", "-", "*", "/"]


def is_parentheses(char: str):
    return char in ["(", ")"]


def split(formula: str) -> list:
    formula = f"({formula})"
    temp = ''
    res = []
    for char in formula:
        if char == " ":
            continue
        if is_parentheses(char) or is_operator(char):
            if temp != "":
                res.append(temp)
                temp = ''

            if char == "-" and (is_operator(res[-1]) or is_parentheses(res[-1])):
                temp += char
            else:
                res.append(char)
        else:
            temp += char
    return res


def stack_out(stack: list):
    res = []
    while len(stack):
        element = stack.pop()
        if element != "(":
            res.append(element)
        else:
            break
    return res


def priority(node):
    operators = ["+", "-", "*", "/"]
    return operators.index(node)


def stack_in(stack: list, node: str) -> list:
    res = []

    while len(stack):
        element = stack.pop()
        if element == "(":
            stack.append(element)
            break
        elif priority(element) > priority(node):
            res.append(element)
        else:
            stack.append(element)
            break
    stack.append(node)
    return res


def to_post(nodes: list) -> list:
    res = []
    stack = []
    for node in nodes:
        if node == ")":
            res += stack_out(stack)
        elif is_parentheses(node):
            stack.append(node)
        elif is_operator(node):
            res += stack_in(stack, node)
        else:
            res.append(node)
    return res


def calculate(nodes: list) -> float:
    stack = []
    while len(nodes):
        element = nodes.pop(0)
        if element == "+":
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            stack.append(num2 + num1)
        elif element == "-":
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            stack.append(num2 - num1)
        elif element == "*":
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            stack.append(num2 * num1)
        elif element == "/":
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            stack.append(num2 / num1)
        else:
            stack.append(element)
    return stack[0]


def main():
    inputs = get_input()
    formulas = generate_formula(inputs)
    labels = ["Sum:", "Difference:", "Product:", "Quotient:"]
    for index, formula in enumerate(formulas):
        nodes = split(formula)
        nodes = to_post(nodes)
        res = calculate(nodes)
        print(f"{labels[index]}{res:.2f}")


if __name__ == '__main__':
    main()
