from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 5
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)


def solve_part1():
    print(header_line)
    print(f'solution part 1')
    # solution code
    stacks = []
    for line in data.splitlines():
        print(line)
        #  skip blank line
        if line == '':
            continue
        if 'move' in line:
            moves = [int(i) for i in line.split() if i.isdigit()]
            print(moves)
            # move moves[0] crates from stack moves[1] to stack moves[2]
            # remove item from stacks[moves[1]
            # insert item to stacks[moves[2]
            for move in range(moves[0]):
                item = stacks[moves[1]-1][0]
                stacks[moves[1]-1].remove(item)
                print(stacks[moves[1]-1])
                print(f'item = {item}')
                stacks[moves[2]-1].insert(0,item)
            print(stacks)
            continue
        # get orders

        # find stacks
        # first line
        line_len = len(line)
        # [ ] [ ] [ ]
        # 012345678910
        # 1,5,9
        index = 0
        for char in range(1, line_len, 4):
            if len(stacks) <= index:
                stacks.append(list())
            if line[char] != ' ':
                stacks[index].append(line[char])
            index += 1

    print(stacks)
    for stack in stacks:
        print(stack[0], end='')
    print()

    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    stacks = []
    for line in data.splitlines():
        print(line)
        #  skip blank line
        if line == '':
            continue
        if 'move' in line:
            moves = [int(i) for i in line.split() if i.isdigit()]
            print(moves)
            # move moves[0] crates from stack moves[1] to stack moves[2]
            # remove item from stacks[moves[1]
            # insert item to stacks[moves[2]i

            # items to move
            items = []
            for move in range(moves[0]):
                item = stacks[moves[1]-1][0]
                stacks[moves[1]-1].remove(item)
                items.append(item)
                print(stacks[moves[1]-1])
                print(f'item = {item}')

            items.reverse();
            for item in items:
                stacks[moves[2]-1].insert(0,item)
            print(stacks)
            continue
        # get orders

        # find stacks
        # first line
        line_len = len(line)
        # [ ] [ ] [ ]
        # 012345678910
        # 1,5,9
        index = 0
        for char in range(1, line_len, 4):
            if len(stacks) <= index:
                stacks.append(list())
            if line[char] != ' ':
                stacks[index].append(line[char])
            index += 1

    print(stacks)
    for stack in stacks:
        print(stack[0], end='')
    print()
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
