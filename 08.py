# import re
# from dataclasses import dataclass

class Course:
    name: str
    duration: int
    schedule: list

    def __init__(self, name, duration, schedule):
        self.name = name
        self.duration = duration
        self.schedule = schedule
        if self.duration < 1 or self.duration > 3:
            raise ValueError
        self.validate_schedule()

    def validate_schedule(self):
        for schedule in self.schedule:
            day = schedule[0]
            period = schedule[1]
            # if not re.match("^[1-5]$", day):
            if day not in ["1", "2", "3", "4", "5"]:
                raise ValueError
            # if not re.match("^[1-9abc]$", period):
            if period not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c"]:
                raise ValueError


def get_infos():
    res = []
    for _ in range(3):
        res.append(get_course_info())
    return res


def get_course_info():
    name = input()
    duration = int(input())
    schedule = []
    for _ in range(duration):
        schedule.append(input())
    return {"name": name, "duration": duration, "schedule": schedule}


def convert(raw_info: list):
    res = []
    for info in raw_info:
        res.append(Course(**info))
    return res


def validate_schedule(courseA: Course, courseB: Course):
    conflict = False
    for a_index in range(courseA.duration):
        for b_index in range(courseB.duration):
            if courseA.schedule[a_index] == courseB.schedule[b_index]:
                print(f"{courseA.name},{courseB.name},{courseA.schedule[a_index]}")
                conflict = True
    return conflict


def validate_not_conflict(courses: list):
    conflict = False
    for i in range(2):
        for j in range(i + 1, 3):
            if validate_schedule(courses[i], courses[j]):
                conflict = True

    if not conflict:
        print("correct")


def main():
    raw_infos = get_infos()
    try:
        courses = convert(raw_infos)
    except Exception:
        print(-1)
        return
    validate_not_conflict(courses)


# if __name__ == '__main__':
#     main()
main()
