from data import get_data_from_file, header_line

DAY = 14
data = get_data_from_file(f"sample")
# data = get_data_from_file(f"day{DAY}.input")
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
def printCaveSystem(path_lines, minX, maxX, minY, maxY):
    print(f"printCaveSystem")
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            print(f"({x},{y})", end="")
        print()


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
            lines.append(tuple(coord.split(",")))
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

    # draw map
    # map is a 2D array
    printCaveSystem(path_lines, minX, maxX, minY, maxY)

    print(header_line)


def solve_part2():
    print(header_line)
    print(f"solution part 2")
    # solution code

    print()
    print(f"result = ")
    print(header_line)


if __name__ == "__main__":
    solve_part1()
    # solve_part2()
