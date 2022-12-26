from ctypes import wstring_at
from data import get_data_from_file, header_line
import numpy as np

DAY = 14
# data = get_data_from_file(f"sample")
data = get_data_from_file(f"day{DAY}.input")
print(f"transformed data for solution")
print(data)
print(header_line)

#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.
# x,y indexes
x = 0
y = 1


def orderTuples(tup1, tup2):
    """order two tuples"""
    # print(f"tup1 = {tup1}, tup2 = {tup2}")
    if tup1 > tup2:
        # print(f"tup1 > tup2")
        return tup2, tup1
    else:
        # print(f"tup1 <= tup2")
        return tup1, tup2


def createPaths(path_lines):
    """append points between paths"""
    new_paths = []
    for path in path_lines:
        points = []
        for i in range(len(path) - 1):
            p1, p2 = orderTuples(path[i], path[i + 1])
            # print(f"p1 = {p1}, p2 = {p2}")
            for py in range(p1[0], p2[0] + 1):
                for px in range(p1[1], p2[1] + 1):
                    points.append((py, px))
        new_paths.append(points)
    return new_paths


def buildCaveSystem(path_lines, minX, maxX, minY, maxY):
    print(f"buildCaveSystem", end="\n\n")
    # create cave system offsets from minX and minY
    Yoffset = minY - maxX - minX
    cave_system = np.zeros((maxY + 1, maxX - minX + 1), dtype=str)
    print(f"cave_system.shape = {cave_system.shape}", end="\n\n")
    for y in range(cave_system.shape[0]):
        for x in range(cave_system.shape[1]):
            cave_system[y][x] = "."
    print()
    for path in path_lines:
        for coord in path:
            # print(f"{coord[1]}, {coord[0]}")
            cave_system[coord[1]][coord[0] - minX] = "#"
    return cave_system


def buildCaveSystem2(path_lines, minX, maxX, minY, maxY):
    print(f"buildCaveSystem", end="\n\n")
    Xoffset = maxY - minY + 1
    cave_system = np.zeros((maxY + 3, Xoffset * 3), dtype=str)
    print(f"cave_system.shape = {cave_system.shape}", end="\n\n")
    for y in range(cave_system.shape[0]):
        for x in range(cave_system.shape[1]):
            cave_system[y][x] = "."
    print()
    for path in path_lines:
        for coord in path:
            # print(f"{coord[1]}, {coord[0]}")
            cave_system[coord[1]][coord[0] - minX + Xoffset] = "#"
    # add floor
    for x in range(cave_system.shape[1]):
        cave_system[cave_system.shape[0] - 1][x] = "#"  # floor:w

    return cave_system


def pourSand(sand, caveSystem):
    print(f"pourSand")

    # pour sand
    # start at sand
    # move down until you hit a wall
    # move left and right until you hit a wall
    # if you hit a wall on both sides, stop
    abyss = 0
    settled = 0
    while not abyss and not settled:
        print(
            f"sand = {sand} = {caveSystem[sand[y]][sand[x]]} abyss = {abyss} settled = {settled}"
        )
        # really shold not need this trap, indicates we are not setting abyss or settled correctly
        if caveSystem[sand[y]][sand[x]] in ("#", "o"):
            abyss = 1

        # move down
        while caveSystem[sand[y]][sand[x]] == ".":  # move down one
            try_sand = (sand[x], sand[y] + 1)
            print(f"sand = {try_sand}|{caveSystem[sand[y]][sand[x]]}")

            # check if we hit the
            if (
                try_sand[y] >= caveSystem.shape[0]
                or try_sand[x] >= caveSystem.shape[1]
                or try_sand[x] < 0
            ):
                # print(f"sand[1] = {try_sand[y]} >= caveSystem.shape[1] = {caveSystem.shape[0]}")
                abyss = 1
                break
            # move left if we hit rock
            if caveSystem[try_sand[y]][try_sand[x]] in ("#", "o"):
                try_sand = (try_sand[x] - 1, try_sand[y])
                # print(f"left_sand = {try_sand}")
            # move right
            if caveSystem[try_sand[y]][try_sand[x]] in ("#", "o"):
                try_sand = (try_sand[x] + 2, try_sand[y])
                # print(f"right_sand = {try_sand}")
            if caveSystem[try_sand[y]][try_sand[x]] in ("#", "o"):
                settled = 1
                caveSystem[sand[y]][sand[x]] = "o"
                break
            sand = try_sand
    return abyss, caveSystem


def solve_part1():
    print(header_line)
    print(f"solution part 1")

    # solution code
    # each line is a path
    # each path is a list of coordinates
    # each coordinate is a tuple (x, y)
    paths = [path.split(" -> ") for path in [line for line in data.splitlines()]]
    print(f"paths: {paths}")
    print(header_line, end="\n\n")

    #
    # for coords in paths:
    #     for i, coord in enumerate(coords):
    #         print(f"list {i} = {tuple(coord.split(','))}", end=",")
    #     print()
    # print(paths)
    # print()
    # print(f"result = ")

    print("convert path coords to tuples")
    path_lines = []
    for path in paths:
        print(path)
        lines = []
        for coord in path:
            print(coord)
            converted = tuple(int(x) for x in coord.split(","))
            lines.append(converted)
        path_lines.append(lines)
    print()
    print(f"path_lines{path_lines}", end="\n\n")

    # get dimensions for map
    # this is the width and height of the map
    minX: int = 2417000
    minY: int = 2417000
    maxX: int = 0
    maxY: int = 0

    for path in path_lines:
        for coord in path:
            if int(coord[0]) < int(minX):
                minX = int(coord[0])
            if int(coord[0]) > int(maxX):
                maxX = int(coord[0])
            if int(coord[1]) < int(minY):
                minY = int(coord[1])
            if int(coord[1]) > int(maxY):
                maxY = int(coord[1])

    print(f"minX = {minX}, maxX = {maxX}, minY = {minY}, maxY = {maxY}", end="\n\n")

    # create points between paths
    new_paths = createPaths(path_lines)
    # print(f"new_paths = {new_paths}", end="\n\n")

    # draw cave map
    caveSystem = buildCaveSystem(new_paths, minX, maxX, minY, maxY)
    print(caveSystem)

    # sand sand = (500,0)
    sand = (500 - minX, 0)
    abyss = 0
    grains = 0
    while not abyss:
        abyss, caveSystem = pourSand(sand, caveSystem)
        print(f"pouring sand {grains}")
        if not abyss:
            grains += 1
    print(caveSystem)
    print(f"grains = {grains}")

    print(header_line)


def solve_part2():
    print(header_line)
    print(f"solution part 2")
    # solution code
    # each line is a path
    # each path is a list of coordinates
    # each coordinate is a tuple (x, y)
    paths = [path.split(" -> ") for path in [line for line in data.splitlines()]]
    print(f"paths: {paths}")
    print(header_line, end="\n\n")

    #
    # for coords in paths:
    #     for i, coord in enumerate(coords):
    #         print(f"list {i} = {tuple(coord.split(','))}", end=",")
    #     print()
    # print(paths)
    # print()
    # print(f"result = ")

    print("convert path coords to tuples")
    path_lines = []
    for path in paths:
        print(path)
        lines = []
        for coord in path:
            print(coord)
            converted = tuple(int(x) for x in coord.split(","))
            lines.append(converted)
        path_lines.append(lines)
    print()
    print(f"path_lines{path_lines}", end="\n\n")

    # get dimensions for map
    # this is the width and height of the map
    minX: int = 2417000
    minY: int = 2417000
    maxX: int = 0
    maxY: int = 0

    for path in path_lines:
        for coord in path:
            if int(coord[0]) < int(minX):
                minX = int(coord[0])
            if int(coord[0]) > int(maxX):
                maxX = int(coord[0])
            if int(coord[1]) < int(minY):
                minY = int(coord[1])
            if int(coord[1]) > int(maxY):
                maxY = int(coord[1])

    print(f"minX = {minX}, maxX = {maxX}, minY = {minY}, maxY = {maxY}", end="\n\n")

    # create points between paths
    new_paths = createPaths(path_lines)
    # print(f"new_paths = {new_paths}", end="\n\n")

    # draw cave map
    caveSystem = buildCaveSystem2(new_paths, minX, maxX, minY, maxY)
    print(caveSystem)

    # sand sand = (500,0)
    Xoffset = maxY - minY + 1

    sand = (500 - minX + Xoffset, 0)
    abyss = 0
    grains = 0
    while not abyss:
        abyss, caveSystem = pourSand(sand, caveSystem)
        print(f"pouring sand {grains}")
        if not abyss:
            grains += 1
    print(caveSystem)
    with open("outfile.txt", "w") as fp:
        for r in caveSystem:
            fp.write("".join(r) + "\n")
    print(f"grains = {grains}")
    print()
    print(f"result = ")
    print(header_line)


if __name__ == "__main__":
    # solve_part1()
    solve_part2()
