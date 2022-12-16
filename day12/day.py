from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 12
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
print(data)
print(header_line)


def printPath(heightMap, visited):
    for r in visited:
        print(heightMap[r[0]][r[1]], end=',')
    print()


minPath = 247112288888
# [R,D,L,U]
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
stepLimit = 10
maxPath = 0



def move(heightMap, old_pos, visited):
    global minPath, maxPath
    # debug step limit
    global stepLimit
    stepLimit -=1
    # if stepLimit <= 0:
    #     return

    if maxPath < len(visited):
        maxPath = len(visited)
        # print step
        print(f'{len(visited)} visited at {visited[len(visited) - 1]} value {heightMap[old_pos[0]][old_pos[1]]}')

    # do we already have better solution
    if len(visited) >= minPath:
        print(f'{old_pos} already > {minPath}')
        return

    # have we reached a solution
    if heightMap[old_pos[0]][old_pos[1]] == 'z':
        pathlen = len(visited)
        if pathlen < minPath and heightMap[old_pos[0]][old_pos[1]] == 'z':
            minPath = pathlen
        print(f'Found E in {pathlen} steps')
        # printPath(heightMap, visited)
        return
    moves = []
    # try to move
    for d in DIR:
        # candidate move
        r = [old_pos[i] + d[i] for i in range(len(d))]

        # don't step off the edge
        if r[0] < 0 or r[1] < 0 or r[0] >= len(heightMap) or r[1] >= len(heightMap[0]):
            # print('avoiding the edge')
            continue

        # dont visit a visited
        if tuple(r) in visited:
            # print(f'{tuple(r)} has already been visited')
            continue

        # step up only one step
        if heightMap[old_pos[0]][old_pos[1]] != 'S' and ord(heightMap[r[0]][r[1]]) - ord(
                heightMap[old_pos[0]][old_pos[1]]) > 1:
            # print('hit step too high')
            continue

        # it is possible to order the list of possible paths and go up as a priority
        moves.append(tuple(r))

    if len(moves) == 0:
        return
        # print(f'dead end {visited}')
    for m in moves:
        new_visited = list(visited)
        new_visited.append(m)
        move(heightMap, m, new_visited)


def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    W = H = 0
    heightMap = [list(mapLine) for mapLine in data.splitlines()]
    print(heightMap)

    # heightMap dimensions
    W = len(heightMap[0])
    H = len(heightMap)
    for r in range(H):
        for c in range(W):
            print(heightMap[r][c], end='')
        print()
    # navigate
    # find start pos
    S = (0,0)
    for r in range(len(heightMap)):
        for c in range(len(heightMap[r])):
            if heightMap[r][c] == 'S':
                S = tuple([r, c])
    pos = S
    visited = [pos]
    pos = move(heightMap, pos, visited)
    print(f' result = {minPath}')

    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code

    print(header_line)


if __name__ == '__main__':
    solve_part1()
    # solve_part2()
