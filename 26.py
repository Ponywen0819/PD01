import math


class Record:
    def __init__(self, increase, decrease):
        self.increase = increase
        self.decrease = decrease

def calc_current_count(records):
    current_count = 0
    for record in records:
        current_count += record.increase - record.decrease

    return current_count


def display_summary(date, current_count,records):
    print(f"{date} {current_count} {records[0].increase} {records[0].decrease}")

def main():
    total = int(input())
    duration = int(input())
    initial_influencer = int(input())
    influence_rate_in_duration = float(input())
    cure_duration = int(input())
    initial_cure_rate = float(input())

    records = [Record(initial_influencer, 0)]
    current_count = calc_current_count(records)
    display_summary(1, current_count, records)

    can_be_influence = math.floor(total * (1 - initial_cure_rate))

    for i in range(1,duration):
        total_influencer = sum([record.increase for record in records])
        can_be_influence_rate = (can_be_influence / total)
        influence_rate = (influence_rate_in_duration / cure_duration) * can_be_influence_rate
        new_increase = math.floor(current_count * influence_rate)

        shit = can_be_influence - total_influencer
        if new_increase >= shit:
            new_increase = shit if shit > 0 else 0


        new_decrease = 0
        if len(records) >= cure_duration:
            new_decrease = records[cure_duration - 1].increase
            can_be_influence -= new_decrease

        records = [Record(new_increase, new_decrease)] + records

        current_count = calc_current_count(records)
        display_summary(i+1, current_count, records)

    total_influencer = sum([record.increase for record in records])

    print(total_influencer)


if __name__ == '__main__':
    main()