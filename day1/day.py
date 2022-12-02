from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 1
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)


def solve_part1():
    print(header_line)
    print(f'solution part 1')
    # solution code
    elves = []
    elfCount = 0
    calories = 0
    for line in data.splitlines():
        print(line)
        if line == '':
            print('end elf')
            elves.append(calories)
            calories = 0
            continue
        calories += int(line)

    print(f'Result:{max(elves)}')
    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    elves = []
    elfCount = 0
    calories = 0
    for line in data.splitlines():
        print(line)
        if line == '':
            print('end elf')
            elves.append(calories)
            calories = 0
            continue
        calories += int(line)

    print(f'Result:{sum(sorted(elves, reverse=True)[:3])}')
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
