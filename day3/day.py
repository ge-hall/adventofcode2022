from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 3
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)


def get_invalid_item(rucksack):
    split = int(len(rucksack) / 2)
    # print(split)
    comp1 = rucksack[:split]
    comp2 = rucksack[split:]
    # print(comp1)
    # print(comp2)
    # find char that exists in both
    return list(set(comp1).intersection(comp2))[0]


def get_priority(item):
    return ord(item) - 65 + 27 if ord(item) < 97 else ord(item) - 96


def solve_part1():
    print(header_line)
    print(f'solution part 1')
    # solution code
    priority = 0
    # for each line as a Rucksack
    for rucksack in data.splitlines():
        item = get_invalid_item(rucksack)
        # print(item)
        priority += get_priority(item)
        # store priority
    # return sum of priority
    print(priority)
    print(header_line)


def get_group_badge(group_rucksacks):
    return list(set(group_rucksacks[0]).intersection(set(group_rucksacks[1])).intersection(set(group_rucksacks[2])))[0]


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    priority = 0
    group_rucksacks = []
    row = 0
    # for each line as a Rucksack
    for rucksack in data.splitlines():
        group_rucksacks.append(rucksack)
        # update group
        row += 1
        if row == 3:
            priority += get_priority(get_group_badge(group_rucksacks))
            group_rucksacks = []
            row = 0
    # return sum of priority
    print(priority)
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
