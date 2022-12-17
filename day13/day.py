import ast

from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 13
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
# print(data)
print(header_line)


def parse_list(llist: list, rlist: list) -> bool:
    """
    If both values are integers, the lower integer should come first.
    :param llist:
    :param rlist:
    :return:
    """
    print(f'parseList: {llist}')
    # If exactly one value is an integer, convert the integer to a list
    # which contains that integer as its only value, then retry the comparison
    consumerIndex = 0

    if len(rlist) == 0:
        return False
    if len(llist) == 0:
        return True
    if type(llist[0]) == int and type(rlist[0]) == list:
        llist[0] = [llist[0]]
    valid = True
    for i in range(len(llist)):
        consumerIndex = i
        if i >= len(rlist):
            return False
        if type(llist[i]) == list and type(rlist[i]) == int:
            rlist[i] = [rlist[i]]
        if type(llist[i]) == int and type(rlist[i]) == list:
            llist[i] = [llist[i]]
        if type(llist[i]) == int and type(rlist[i]) == int:
            if llist[i] < rlist[i]:
                return True
            elif llist[i] > rlist[i]:
                return False
            else:
                continue


        scalarList = not list_has_nesting(llist[i]) and not list_has_nesting(rlist[i])

        if scalarList:
            if not test_list(llist[i], rlist[i]):
                return False
        else:
            if not parse_list(llist[i], rlist[i]):
                return False



    return valid


def test_list(llist: list, rlist: list) -> bool:
    try:
        for i in range(len(llist)):
            if llist[i] < rlist[i]:
                return True
            elif llist[i] > rlist[i]:
                return False
        return True

    except:
        return False


def list_has_nesting(l: list):
    return len([item for item in l if type(item) == list]) > 0


def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    # process file data
    # get list of packets
    filtered_list = [line for line in data.splitlines() if line != '']
    pairs = [[item1, item2] for i, item1 in enumerate(filtered_list) for j, item2 in enumerate(filtered_list) if
             i % 2 == 0 and i == j - 1]
    # print(pairs)
    winners = []
    for n, pairs in enumerate(pairs):
        left_packet = ast.literal_eval(pairs[0])
        right_packet = ast.literal_eval(pairs[1])

        print(f'Pair {n + 1}: {left_packet} and {right_packet}')
        print('===========================================')
        # print(f'left_packet: {left_packet}')
        # test is pairs is just two lists no nesting
        scalarList = not list_has_nesting(left_packet) and not list_has_nesting(right_packet)
        # print(f'scalarList: {scalarList}')
        if scalarList:
            if test_list(left_packet, right_packet):
                winners.append(n+1)
                print('*** won as scalar list ***')
        else:
            if parse_list(left_packet, right_packet):
                winners.append(n+1)
                print('*** won as nested list ***')
    print(winners)
    print(sum(winners))

    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code

    print()
    print(f'result = {X}')
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    # solve_part2()
