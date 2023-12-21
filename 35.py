class School:
    def __init__(self, setting_string: str):
        setting = setting_string.split(" ")
        self.name = setting[0]
        self.props = setting[1:]


def create_school():
    setting_string = input()
    return School(setting_string)


def create_condition():
    condition_list = input().split(" + ")
    return [c.split(" ") for c in condition_list]


def test_fit(school, condition_list):
    for condition in condition_list:
        fitness = 0
        for prop in condition:
            try:
                school.props.index(prop)
                fitness += 1
            except ValueError:
                break
        if fitness == len(condition):
            return True
    return False


def test_fitness(school, condition_list):
    fitness = 0
    for condition in condition_list:
        for prop in condition:
            try:
                school.props.index(prop)
                fitness += 1
            except ValueError:
                pass
    return fitness


def find_fit(school_list, condition_list):
    school_list = [(school, test_fit(school, condition_list)) for school in school_list]

    fit_condition_list = [school for school, fit in school_list if fit]
    return fit_condition_list


def find_fit_and_only(school_list, condition_list):
    school_list = [(school, test_fitness(school, condition_list)) for school in school_list]

    school_list.sort(key=lambda x: x[1], reverse=True)
    res = [school_list[0]]

    index = 1
    while 1:
        if  index >= len(school_list):
            break
        if school_list[index - 1][1] != school_list[index][1]:
            break
        res.append(school_list[index])
        index += 1

    fit_condition_list = [school for school, fit in res if fit]
    return fit_condition_list


def main():
    number_of_school = int(input())
    school_list = [create_school() for _ in range(number_of_school)]

    number_of_condition = int(input())
    condition_list = [create_condition() for _ in range(number_of_condition)]

    mode = input()
    for condition in condition_list:
        if mode == "0":
            fit_school_list = find_fit(school_list, condition)
            print(f"{' '.join([school.name for school in fit_school_list])}")
        else:
            most_fit_school_list = find_fit_and_only(school_list, condition)
            print(f"{' '.join([school.name for school in most_fit_school_list])}")


if __name__ == '__main__':
    main()
