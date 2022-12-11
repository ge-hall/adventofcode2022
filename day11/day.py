import cProfile
import math
import re
from functools import reduce

from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 11
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
# print(data)
print(header_line)


def getWorryLevel(item, rule):
    if re.findall(r"new\s*=\s*old\s*\*", rule) != []:
        val = re.findall(r"\d+\.?\d*", rule)
        if val:
            # print(f'val = {val}')
            return item * int(val[0])
        else:
            return item * item
    if re.findall(r"new\s*=\s*old\s*\+", rule) != []:
        val = re.findall(r"\d+\.?\d*", rule)
        if val:
            # print(f'val = {val}')
            return item + int(val[0])
        else:
            return item + item

    return item


# Pre-compile the regular expression patterns
rule_pattern = re.compile(r"new\s*=\s*old\s*\*")
val_pattern = re.compile(r"\d+\.?\d*")


def getWorryLevel2(item, rule):
    if rule_pattern.search(rule):
        val = val_pattern.findall(rule)
        if val:
            # print(f'val = {val}')
            return item * int(val[0])
        else:
            return item * item
    if re.findall(r"new\s*=\s*old\s*\+", rule) != []:
        val = re.findall(r"\d+\.?\d*", rule)
        if val:
            # print(f'val = {val}')
            return item + int(val[0])
        else:
            return item + item

    return item

def itemBy19(item):
    return item * 19

def itemByItem(item):
    return item * item
def itemPlus3(item):
    return item + 3
def itemPlus6(item):
    return item +6

def itemPlusItem(item):
    return item + item
def getWorryFunction(rule):
    if rule_pattern.search(rule):
        val = val_pattern.findall(rule)
        if val:
            # print(f'val = {val}')
            return itemBy19
        else:
            return itemByItem
    if re.findall(r"new\s*=\s*old\s*\+", rule) != []:
        val = re.findall(r"\d+\.?\d*", rule)
        print(f'val = {val}')

        if val:

            if int(val[0]) == 3:
                return itemPlus3
            else:
                return itemPlus6
        else:
            return itemPlusItem



def multiply(x, y):
    return x * y


def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    monkeyInfo = []
    lines = [line for line in data.splitlines()]
    for spec in range(int(len(lines) / 7) + 1):
        monkeyInfo.append(lines[spec * 7:(spec + 1) * 7])
    print(monkeyInfo)
    monkeys = []
    for monkey in monkeyInfo:
        monkeys.append(re.findall(r"\d+\.?\d*", monkey[1]))
    print(monkeys)
    inspections = [0] * len(monkeys)
    # asses worry level
    for round in range(20):
        print(f'Round {round}')
        # inspect items
        for i, monkey in enumerate(monkeys):
            # print(f'Monkey {i} items:{monkey}')
            throwItems = []
            for j, item in enumerate(monkey):
                # print(f'inspecting item {item}')
                inspections[i] += 1
                item_new = getWorryLevel(int(item), monkeyInfo[i][2])
                item_new = int(item_new / 3)
                # print(f'inspected item {item_new}')
                # print(monkey)

                # test
                divisor = re.findall(r"\d+\.?\d*", monkeyInfo[i][3])[0]
                if item_new % int(divisor) == 0:
                    toMonkey = re.findall(r"\d+\.?\d*", monkeyInfo[i][4])[0]
                else:
                    toMonkey = re.findall(r"\d+\.?\d*", monkeyInfo[i][5])[0]
                # print(f'throw item to monkey {toMonkey}')
                throwItems.append([int(toMonkey), item_new, item])
            for throw in throwItems:
                monkey.remove(throw[2])
                monkeys[throw[0]].append(throw[1])
        print(monkeys)
    print(inspections)
    print(reduce(multiply, sorted(inspections)[len(inspections) - 2:]))

    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    monkeyInfo = []
    lines = [line for line in data.splitlines()]
    for spec in range(int(len(lines) / 7) + 1):
        monkeyInfo.append(lines[spec * 7:(spec + 1) * 7])
    print(monkeyInfo)
    monkeys = []
    rules = []
    divisors = []
    for monkey in monkeyInfo:
        monkeys.append(re.findall(r"\d+\.?\d*", monkey[1]))
        print(monkey[2])
        rules.append(getWorryFunction(monkey[2]))
        divisors.append(int(re.findall(r"\d+\.?\d*", monkey[3])[0]))

    lcm = divisors[0]
    for i in range(1, len(divisors)):
        lcm = lcm * divisors[i] // math.gcd(lcm, divisors[i])

    # print(monkeys)
    inspections = [0] * len(monkeys)

    # asses worry level
    for round in range(10000):
        print(f'Round {round}')
        # inspect items
        for i, monkey in enumerate(monkeys):
            # print(f'Monkey {i} items:{monkey}')
            throwItems = []
            for j, item in enumerate(monkey):
                if item == 0:
                    continue
                # print(f'inspecting item {j}')
                inspections[i] += 1
                item_new = getWorryLevel(int(item), monkeyInfo[i][2])%lcm
                # item_new = rules[i](int(item))%(lcm)
                # test
                divisor = re.findall(r"\d+\.?\d*", monkeyInfo[i][3])[0]
                if item_new % int(divisor) == 0:
                    toMonkey = re.findall(r"\d+\.?\d*", monkeyInfo[i][4])[0]
                else:
                    toMonkey = re.findall(r"\d+\.?\d*", monkeyInfo[i][5])[0]
                # print(f'throw item to monkey {toMonkey}')
                throwItems.append([int(toMonkey), item_new, item])
            for throw in throwItems:
                # print(f'throwing {len(throw)} items')
                monkey.remove(throw[2])
                monkeys[throw[0]].append(throw[1])
        # print(monkeys)
    print(inspections)
    print(reduce(multiply, sorted(inspections)[len(inspections)-2:]))
    print(header_line)


if __name__ == '__main__':
    profiler = cProfile.Profile()
    # solve_part1()
    solve_part2()
    # cProfile.run('solve_part2()')
