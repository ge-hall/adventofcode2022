from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 2
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)

# A = X = 1 = ROCK
# B = Y = 2 = PAPER
# C = Z = 3 = SCISSORS
def score(round):
    if round[0] == 'A':
        if round[1] == 'X':
            return 3 + 1
        if round[1] == 'Y':
            return 6 + 2
        if round[1] == 'Z':
            return 0 + 3
    if round[0] == 'B':
        if round[1] == 'X':
            return 0 + 1
        if round[1] == 'Y':
            return 3 + 2
        if round[1] == 'Z':
            return 6 + 3
    if round[0] == 'C':
        if round[1] == 'X':
            return 6 + 1
        if round[1] == 'Y':
            return 0 + 2
        if round[1] == 'Z':
            return 3 + 3

# A = X = 1 = ROCK
# B = Y = 2 = PAPER
# C = Z = 3 = SCISSORS
def score2(round):
    # lose
    if round[1] == 'X':
        if round[0] == 'A':
            return 0 + 3
        if round[0] == 'B':
            return 0 + 1
        if round[0] == 'C':
            return 0 + 2
    # draw
    if round[1] == 'Y':
        if round[0] == 'A':
            return 3 + 1
        if round[0] == 'B':
            return 3 + 2
        if round[0] == 'C':
            return 3 + 3
    # win
    if round[1] == 'Z':
        if round[0] == 'A':
            return 6 + 2
        if round[0] == 'B':
            return 6 + 3
        if round[0] == 'C':
            return 6 + 1

def solve_part1():
    print(header_line)
    print(f'solution part 1')
    # solution code
    total = 0
    for line in data.splitlines():
        round = line.split()
        print(round)
        total += score(round)
    print(total)
    print(header_line)

def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    total = 0
    for line in data.splitlines():
        round = line.split()
        print(round)
        total += score2(round)
    print(total)
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
