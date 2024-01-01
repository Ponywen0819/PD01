import math


def insert_course_and_return_self(database):
    no, semester, student_count = input().split(" ")

    course_table = database["Course"]

    course_table[no + semester[0:3]] = {
        "no": no,
        "year": int(semester[0:3]),
        "semester": semester,
        "student_count": int(student_count)
    }

    return course_table[no + semester[0:3]]


def insert_student_and_return_self(database, student_no):
    student_table = database["Student"]

    student_table[student_no] = {
        "no": student_no,
        "start_year": int(student_no[0:3]),
        "department": student_no[3:6],
    }

    return student_table[student_no]


def insert_record_and_return_self(database, course, student_no, score):
    record_table = database["Record"]

    avg_score = 0
    if len(score) == 2:
        avg_score = math.ceil(float(score[0]) * 0.7 + float(score[1]) * 0.3)
    elif score[0] == "w":
        avg_score = -1
    else:
        avg_score = int(score[0])

    record_table[course["no"] + student_no + str(course['year'])] = {
        "course_no": course['no'],
        "student_no": student_no,
        "year": course['year'],
        "score": avg_score,
        "drop": avg_score == -1
    }

    return record_table[course['no'] + student_no + str(course['year'])]


def get_unique_class_list(database):
    student_table = database["Student"]
    unique_list = list(set([f"{student['start_year']}-{student['department']}" for student in student_table.values()]))
    return sorted(unique_list)


def get_unique_year_list(database):
    course_table = database["Course"]
    return list(set([course["year"] for course in course_table.values()]))


def get_unique_course_list(database):
    course_table = database["Course"]
    course_list = list(set([course["no"] for course in course_table.values()]))
    return sorted(course_list)


def get_drop_ratio_by_no(database, student_no, year):
    record_table = database["Record"]
    course_table = database["Course"]
    record_list = [record for record in record_table.values() if
                   record["student_no"] == student_no and (record["course_no"] + str(year)) in course_table.keys()]
    drop_count = len([record for record in record_list if record["drop"]])
    return drop_count / len(record_list)


def get_ranking(database, start_year, department, year):
    student_table = database["Student"]
    record_table = database["Record"]
    course_table = database["Course"]

    student_list = [student for student in student_table.values() if
                    student["start_year"] == start_year and student["department"] == department]
    course_list = [course for course in course_table.values() if course["year"] == year]

    score_table = {}
    for student in student_list:
        for course in course_list:
            if (course["no"] + student["no"] + str(year)) not in record_table.keys():
                continue

            record = record_table[course["no"] + student["no"] + str(year)]
            if record["drop"]:
                continue
            if student["no"] not in score_table:
                score_table[student["no"]] = [record["score"] for _ in range(int(record['course_no'][-1]))]
            else:
                score_table[student["no"]] += [record["score"] for _ in range(int(record['course_no'][-1]))]

    score_table = {k: math.floor(sum(v) / len(v)) for k, v in score_table.items()}
    score_table = {k: v for k, v in
                   sorted(sorted(score_table.items(), key=lambda item: item[0]), key=lambda item: item[1],
                          reverse=True)}

    top_ranking = list(score_table.items())[0:3]
    print(department, start_year, year)
    for index, [student_no, score] in enumerate(top_ranking):
        print(student_no, end=" ")
        print(math.ceil(score), end=" ")
        for i in range(1, 100):
            rank = math.ceil(len(student_list) * i / 100)
            if rank >= (index + 1):
                print(f"{i}%", end=" ")
                break

        print(f"{math.ceil(get_drop_ratio_by_no(database, student_no, year) * 100)}%")
    return


def get_ranking_by_course(database, course_no, year):
    record_table = database["Record"]

    record_list = [record for record in record_table.values() if
                   record["course_no"] == course_no and record["year"] == year]
    if len(record_list) == 0:
        return
    ranking = sorted([record for record in record_list if not record["drop"]], key=lambda item: item["student_no"],
                     reverse=False)
    ranking = sorted(ranking, key=lambda item: item["score"], reverse=True)

    print(course_no, year)

    avg = math.floor(sum([score['score'] for score in ranking]) / len(ranking))
    drop_ratio = math.floor((1 - (len(ranking) / len(record_list))) * 100)
    print(ranking[0]["score"], avg, ranking[-1]["score"], f"{drop_ratio}%")

    for index, record in enumerate(ranking[0:3]):
        print(record["student_no"], end=" ")
        print(record['score'], end=" ")
        for i in range(1, 100):
            rank = math.ceil(len(record_list) * i / 100)
            if rank >= (index + 1):
                print(f"{i}%")
                break
    return


def get_course_info(database, course_no):
    record_table = database["Record"]
    record_list = [record for record in record_table.values() if record["course_no"] == course_no]

    if len(record_list) == 0:
        return

    record_sorted = sorted(sorted(record_list, key=lambda item: item["student_no"]), key=lambda item: item["score"],
                           reverse=True)
    print(record_sorted[0]["student_no"], end=" ")
    print(record_sorted[1]["student_no"], end=" ")

    class_count = {}
    for record in record_list:
        if record["student_no"][3:6] not in class_count:
            class_count[record["student_no"][3:6]] = 1
        else:
            class_count[record["student_no"][3:6]] += 1
    class_count_sorted = sorted(class_count.items(), key=lambda item: item[1], reverse=True)
    print(class_count_sorted[0][0], end=" ")
    if len(class_count_sorted) > 1:
        print(class_count_sorted[1][0])


def main():
    number_of_courses = int(input())

    database = {
        "Course": {},
        "Student": {},
        "Record": {}
    }

    for i in range(number_of_courses):
        course = insert_course_and_return_self(database)
        for _ in range(course["student_count"]):
            [student_no, *score] = input().split(" ")
            student = insert_student_and_return_self(database, student_no)
            insert_record_and_return_self(database, course, student["no"], score)

    class_list = get_unique_class_list(database)
    count_years = get_unique_year_list(database)
    course_list = get_unique_course_list(database)

    for class_ in class_list:
        for year in count_years:
            get_ranking(database, int(class_[0:3]), class_[4:7], year)

    for course in course_list:
        for year in count_years:
            get_ranking_by_course(database, course, year)

    course_no = input()
    get_course_info(database, course_no)


if __name__ == '__main__':
    main()
