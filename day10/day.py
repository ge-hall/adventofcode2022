from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 10
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)

def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    X=1
    cycleCount =0
    adder = 0
    instructions = [command.split() for command in data.splitlines()]
    print(instructions)
    processingComplete = False
    instPtr = 0
    activeInst = 0
    command = None
    signals = []
    while not processingComplete:
        cycleCount +=1
        if cycleCount % 40 == 20 or cycleCount == 20:
            print(f'signal strength is {cycleCount*X}')
            signals.append(cycleCount*X)
        if activeInst == 0:
            # print('reading instruction')
            if instPtr == len(instructions):
                break
            command = instructions[instPtr]
            instPtr += 1


        if command[0] == 'addx':
            # print(f'add {command[1]}')
            if activeInst == 0:
                activeInst +=2
            elif activeInst == 1:
                X += int(command[1])
        elif command[0] == 'noop':
            activeInst = 1
            pass
        activeInst -=1
    print(f'result = {X}')






    print(f'adder = {adder}, cycleCOunt = {cycleCount}')
    print(f'result = {sum(signals)}')

    print(header_line)

def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    X=1
    cycleCount =0
    adder = 0
    instructions = [command.split() for command in data.splitlines()]
    # print(instructions)
    processingComplete = False
    instPtr = 0
    activeInst = 0
    command = None
    signals = []
    spritePosition = 1
    while not processingComplete:
        cycleCount +=1
        # print pixel

        if cycleCount % 40 == 20 or cycleCount == 20:
            # print(f'signal strength is {cycleCount*X}')
            signals.append(cycleCount*X)
        if activeInst == 0:
            # print('reading instruction')
            if instPtr == len(instructions):
                break
            command = instructions[instPtr]
            instPtr += 1

        if cycleCount % 40 == 1:
            print()
        if cycleCount%40 in [spritePosition-1, spritePosition, spritePosition+1]:
            print('#',end='')
        else:
            print('.', end='')
        # print(f'cycle:{cycleCount%40 } sprite:{spritePosition}')
        # ...............###......................
        if command[0] == 'addx':
            # print(f'add {command[1]}')
            if activeInst == 0:
                activeInst +=2
            elif activeInst == 1:
                X += int(command[1])
                spritePosition = X+1
        elif command[0] == 'noop':
            activeInst = 1
            pass
        activeInst -=1
    print()
    print(f'result = {X}')
    print(header_line)


if __name__ == '__main__':
    # solve_part1()
    solve_part2()
