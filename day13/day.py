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
    # check for None list
    if rlist == llist:
        return None
    if len(rlist) == 0:
        return False
    if len(llist) == 0:
        return None
    if type(llist[0]) == int and type(rlist[0]) == list:
        llist[0] = [llist[0]]
    valid = None
    for i in range(len(llist)):
        try:
            if type(llist[i]) == list and type(rlist[i]) == int:
                rlist[i] = [rlist[i]]
        except:
            return False
        try:
            if type(llist[i]) == int and type(rlist[i]) == list:
                llist[i] = [llist[i]]
        except:
            return False

        if type(llist[i]) == int and type(rlist[i]) == int:
            if llist[i] < rlist[i]:
                return None
            elif llist[i] > rlist[i]:
                return False
            else:
                continue

        sorted = parse_list(llist[i], rlist[i])
        if sorted == False:
            return False
        if sorted:
            return True
        else:
            continue

            # missing the case when a list runs out so need to switch to -1,0,1
            # when running
    if(len(llist) < len(rlist)):
        valid = True
    elif(len(llist) > len(rlist)):
        valid = False
    return valid


def is_sorted(llist: list, rlist: list) -> bool:
    try:
        for i in range(len(llist)):
            if llist[i] < rlist[i]:
                return True
            elif llist[i] > rlist[i]:
                return False
        return None

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
        # scalarList = not list_has_nesting(left_packet) and not list_has_nesting(right_packet)
        # print(f'scalarList: {scalarList}')
        # if scalarList:
        #     if is_sorted(left_packet, right_packet):
        #         winners.append(n+1)
        #         print('*** won as scalar list ***')
        # else:
        result = parse_list(left_packet, right_packet)
        if result or result == None:
            winners.append(n + 1)
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
