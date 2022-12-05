from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 4
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
# print(data)
print(header_line)

def solve_part1():
    print(header_line)
    print(f'solution part 1')
    # solution code
    contains = 0
    lineCount = 0
    for line in data.splitlines():
        lineCount +=1
        assignments = line.split(',')
        print(assignments)
        first = assignments[0].split('-')
        firstList = []
        for i in range(int(first[0]), int(first[1])+1):
            firstList.append(i)
        print(firstList)
        second = assignments[1].split('-')
        secondList = []
        for i in range(int(second[0]), int(second[1])+1):
            secondList.append(i)
        print(secondList)
        if all(item in firstList for item in secondList) or all(item in secondList for item in firstList):
            print(f'match:{line}')
            contains +=1
            # if all(item in firstList for item in secondList) and all(item in secondList for item in firstList):
            #     contains -=1

    print(contains)
    print(lineCount)
    print(header_line)

def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code

    contains = 0
    lineCount = 0
    for line in data.splitlines():
        lineCount +=1
        assignments = line.split(',')
        print(assignments)
        first = assignments[0].split('-')
        firstList = []
        for i in range(int(first[0]), int(first[1])+1):
            firstList.append(i)
        print(firstList)
        second = assignments[1].split('-')
        secondList = []
        for i in range(int(second[0]), int(second[1])+1):
            secondList.append(i)
        print(secondList)
        if any(item in firstList for item in secondList) or all(item in secondList for item in firstList):
            print(f'match:{line}')
            contains +=1
            # if all(item in firstList for item in secondList) and all(item in secondList for item in firstList):
            #     contains -=1

    print(contains)
    print(lineCount)
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
