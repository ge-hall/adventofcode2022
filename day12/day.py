from collections import deque

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
    stepLimit -= 1
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


alpha = 'abcdefghijklmnopqrstuvwxyzS'


def bfs(map, pos):
    w, h = len(map[0]), len(map)
    q = deque([[pos]])
    seen = {pos}
    while q:
        path = q.popleft()
        x, y = path[-1]
        if map[y][x] == "E":
            return path
        e = alpha.index(map[y][x])
        # print(f'path {path}')
        for x2, y2 in [(d[0] + path[-1][0], d[1] + path[-1][1]) for d in DIR]:  # [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                e2 = alpha.index(map[y2][x2]) if map[y2][x2] != "E" else 25
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))


def solve_part1():
    print(header_line)
    print(f'solution part 1')

    # solution code
    W = H = 0
    heightMap = [[c for c in line] for line in data.splitlines()]
    for row in heightMap:
        print(row)

    # heightMap dimensions
    W = len(heightMap[0])
    H = len(heightMap)
    # for r in range(H):
    #     for c in range(W):
    #         print(heightMap[r][c], end='')
    #     print()
    # navigate
    # find start pos
    S = (0, 0)
    for y in range(len(heightMap)):
        for x in range(len(heightMap[y])):
            if heightMap[y][x] == 'S':
                S = (x, y)
    pos = S
    visited = [pos]
    print(f'Starting at {pos}')
    # recursive move not working going to try bfs
    # pos = move(heightMap, pos, visited)
    result = bfs(heightMap, S)
    print(f'found {len(result) - 1} steps')
    print(result)

    print(header_line)


def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code

    W = H = 0
    heightMap = [[c for c in line] for line in data.splitlines()]
    for row in heightMap:
        print(row)

    # heightMap dimensions
    W = len(heightMap[0])
    H = len(heightMap)
    # for r in range(H):
    #     for c in range(W):
    #         print(heightMap[r][c], end='')
    #     print()
    # navigate
    # find start pos
    S = (0, 0)
    for y in range(len(heightMap)):
        for x in range(len(heightMap[y])):
            if heightMap[y][x] == 'S':
                S = (x, y)
    pos = S
    visited = [pos]
    print(f'Starting at {pos}')
    # recursive move not working going to try bfs
    # pos = move(heightMap, pos, visited)
    starts = [(x, y) for y in range(len(heightMap)) for x in range(len(heightMap[y])) if heightMap[y][x] == 'a']
    result = min([len(bfs(heightMap, s)) - 1 for s in starts if bfs(heightMap, s)])
    print(f'found {result} steps')
    print(result)
    print(header_line)


if __name__ == '__main__':
    # solve_part1()
    solve_part2()
