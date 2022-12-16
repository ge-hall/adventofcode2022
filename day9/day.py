from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 9
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)


def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    bridge = {}
    h = [500, 500]
    t = [500, 500]
    # tuple is immutable but list cannot be dict key so
    # convert list t to tupple on each bridge update
    bridge[tuple(t)] = 1
    DIR = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
    x = 0
    y = 1
    for line in data.splitlines():
        move = [t for t in line.split(" ")]
        print(f'({move[0]},{move[1]})')
        # move
        m = move[0]
        mag = int(move[1])
        print(f'm = {m}')
        d = DIR[m]

        if m in ['R', 'L']:
            print(d)
            for p in range(mag):
                h[x] += d
                if abs(h[x] - t[x]) > 1:
                    t[x] += d
                    if t[y] != h[y]:
                        print('move tail diag')
                        t[y] = h[y]
                print(f't={t}|h={h}')
                bridge[tuple(t)] = 1

        elif m in ['U', 'D']:
            print(f' U/D:{d}')
            for p in range(mag):
                h[y] += d

                if abs(h[y] - t[y]) > 1:
                    t[y] += d
                    if t[x] != h[x]:
                        print('move tail diag')
                        t[x] = h[x]
                print(f't={t}|h={h}')

                bridge[tuple(t)] = 1

    print(bridge)
    print(len(set(bridge.keys())))
    print(header_line)


def printRope(rope):
    #     get range of print out
    #  26 x 21
    # s = 11,15
    for y in range(0, 5):
        for x in range(0, 6):
            if y == 0 and x == 0:
                print('  ',end='')
                for h in range(0,6):
                    print(f'{h}', end='')
                print()

            if x == 0:
                print(f'{y}|', end='')
            val = '.'
            for i, knot in enumerate(rope):
                if knot[0] == x and knot[1] == y:
                    if i == 0:
                        val = 'H'
                    else:
                        val = f'{i}'
                    break
            print(val, end='')

        print()


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    bridge = {}
    rope = [[0, 4] for i in range(10)]
    print(rope)
    # tuple is immutable but list cannot be dict key so
    # convert list t to tupple on each bridge update
    bridge[tuple(rope[len(rope) - 1])] = 1
    DIR = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
    x = 0
    y = 1

    for line in data.splitlines():
        move = [t for t in line.split(" ")]
        print(f'({move[0]},{move[1]})')
        # move
        m = move[0]
        mag = int(move[1])
        print(f'm = {m}')
        d = DIR[m]

        if m in ['R', 'L']:
            print(d)
            c = x
            cc = y
        elif m in ['U', 'D']:
            print(f' U/D:{d}')

            c = y
            cc = x
        for p in range(mag):
            # move head
            printRope(rope)
            print(f'move {p+1}')
            print('moved head')
            rope[0][c] += d
            printRope(rope)
            print('===========>')


            #  follow head
            # print(f'{rope}')
            diag = False
            if abs(rope[0][c] - rope[1][c]) > 1:
                rope[1][c] += d
                print('moving knot 1')
                if rope[1][cc] != rope[0][cc]:
                    diag = True
                    if rope[1][cc] - rope[0][cc] > 0:
                        rope[1][cc] -=1
                    elif rope[1][cc] - rope[0][cc] < 0:
                        rope[1][cc] +=1
                printRope(rope)
                # should only process visible knots
                covered = len(rope)
                for knot in reversed(range(1, len(rope))):
                    if rope[knot][c] == rope[knot-1][c] and rope[knot][cc] == rope[knot-1][cc]:
                        covered = knot
                    else:
                        break
                print(f'{covered} covered')
                for knot in range(2, covered):
                    printRope(rope)

                    # check we have not reached invisible knots
                    print(f'moving knot {knot},{rope[knot-1]},{rope[knot]}, {d}')
                    print(rope)
                    # # dont stack knots
                    # if rope[knot-1][c] == rope[knot][c]+d and not diag:
                    #     print(f'stacked knot {knot},{rope[knot-1]},{rope[knot]}, {d}, c = {c}')
                    #     break
                    # # no diagonal to move to
                    # elif rope[knot-1][c] == rope[knot][c]+d and abs(rope[knot-1][cc] - rope[knot][cc]) == 1:
                    #     print(f'diag stack {knot},{rope[knot-1]},{rope[knot]}, {d}, c = {c}')
                    #     break

                    print(f'move knot:{knot}')
                    # check for diagonal movement
                    if abs(rope[knot-1][c] - rope[knot][c]) + abs(rope[knot-1][cc] - rope[knot][cc]) > 2 or diag:
                        print('knot -1 went diagonal so we follow')
                        if rope[knot][cc] - rope[0][cc] > 0:
                            rope[knot][cc] -=1
                        elif rope[knot][cc] - rope[0][cc] < 0:
                            rope[knot][cc] +=1
                        rope[knot][c] +=d
                        print(rope[knot])
                    else:
                        # move straight in direction to follow knot 1
                        # but only if we are directly behind it
                        # if knot 1 is diagonal from knot 2 dir becomes orthogonal move cc
                        # if abs(rope[knot-1][c] - rope[knot][c]) == 1 and abs(rope[knot-1][cc] - rope[knot][cc]) == 1:
                        #     print('orth move')
                        #     rope[knot][cc] += rope[knot-1][cc] - rope[knot][cc]
                        # else probable need to catch up with knot -1 but what direction is it in
                        if rope[knot-1][x] == rope[knot][x]:
                            print('same x')
                            if rope[knot-1][y] - rope[knot][y] > 1:
                                rope[knot][y] += DIR['D']
                            elif rope[knot][y] - rope[knot-1][y] > 1:
                                rope[knot][y] += DIR['U']
                        else:
                            print('same y')
                            if rope[knot-1][x] - rope[knot][x]  > 1:
                                rope[knot][x] += DIR['R']
                            elif rope[knot][x] - rope[knot-1][x]  > 1:
                                rope[knot][x] += DIR['L']


            print(f't={rope[len(rope) - 1]}|h={rope[0]}')
            bridge[tuple(rope[len(rope) - 1])] = 1
        # print(rope)
        printRope(rope)

        # elif m in ['U', 'D']:
        #     print(f' U/D:{d}')
        #
        #     for p in range(mag):
        #         # move head
        #         print('moved head')
        #         rope[0][y] += d
        #         # print(rope[0])
        #         print('===========>')
        #         printRope(rope)
        #         print(f'move {p} moving rest')
        #         #  follow head
        #         move = 0
        #         if abs(rope[0][y] - rope[1][y]) > 1:
        #             move = 1
        #             rope[1][y] += d
        #             if rope[1][x] != rope[0][x]:
        #                 print('move tail diag')
        #                 if rope[1][x] - rope[0][x] > 0:
        #                     rope[1][x] -=1
        #                 elif rope[1][x] - rope[0][x] < 0:
        #                     rope[1][x] +=1
        #
        #             for knot in range(2, len(rope)):
        #                 # check we have not reached invisible knots
        #
        #                 if abs(rope[knot-1][x] - rope[knot][x]) == 0:
        #                     continue
        #                 print(f'move knot:{knot}')
        #                 if abs(rope[1][y] - rope[knot][y]) > 1:
        #                     rope[knot][y] += d
        #                     print('Move')
        #                 if abs(rope[knot-1][x] - rope[knot][x]) > 1:
        #                     rope[knot][x] += rope[knot-1][x] - rope[knot][x]-1
        #
        #
        #         # print(f't={rope[len(rope)-1]}|h={rope[0]}')
        #         bridge[tuple(rope[len(rope) - 1])] = 1
        #         print(rope)
        #         printRope(rope)

    print(bridge)
    print(len(set(bridge.keys())))
    print(header_line)


if __name__ == '__main__':
    # solve_part1()
    solve_part2()
