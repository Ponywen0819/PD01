import re


def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def extract_middle_strings(text, prefix, postfix_list):
    end_pattern = '|'.join(map(re.escape, postfix_list))
    pattern = f'{re.escape(prefix)}(.*?)(?:{end_pattern})'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        if not is_prime(len(match)):
            matches.remove(match)
            
    matches = list(set(matches))
    matches.sort()
    results = sorted(matches, key=len, reverse=False)
    return results


def main():
    prefix = input()
    postfix_list = input().split(" ")
    gene = input()
    result = extract_middle_strings(gene, prefix, postfix_list)
    if len(result) > 0:
        print("\n".join(result))
    else:
        print("No gene")


main()
