from os import wait
from data import get_data_from_file, get_data_from_file_as_int_list, header_line
import re
import numpy as np

DAY = 15
# data = get_data_from_file(f"sample.input")
data = get_data_from_file(f"day{DAY}.input")
print(f"transformed data for solution")
print(data)
print(header_line)


def extract_numbers_from_string(string):
    return [int(i) for i in re.findall(r"-?\b\d+\b", string)]


# Example
string = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"

print(extract_numbers_from_string(string))  # Output: [2, 4]


def solve_part1():
    print(header_line)
    print(f"solution part 1")

    # solution code
    # get sensor and beacon data
    sensors = []
    for line in data.splitlines():
        sensor_beacon_pair = extract_numbers_from_string(line)
        sensors.append(sensor_beacon_pair)
    # process each sensor onto a map
    min_x = min([min(sensor[::2]) for sensor in sensors])
    max_x = max([max(sensor[::2]) for sensor in sensors])
    min_y = min([min(sensor[1::2]) for sensor in sensors])
    max_y = max([max(sensor[1::2]) for sensor in sensors])
    print(f"min_x {min_x}, max_x {max_x}, min_y {min_y}, max_y {max_y}")

    print(sensors)
    print(header_line)

    # cannot make a ndarray to fit the solution.
    # create map
    # map = np.zeros(
    #     (max_y - min_y + 1, max_x - min_x + 1),
    #     dtype=str,
    # )
    # map[:] = "."

    # we only care about distances from sensors that cross Y=200000
    # check each point on line 200000 between minx and maxx
    # if it is in range of a sensor, add to count
    y = 2000000
    H = max_y - min_y + 1
    count = 0
    for x in range(min_x - H, max_x + H):
        print(x)
        for sensor in sensors:
            x1 = sensor[0]
            y1 = sensor[1]
            x2 = sensor[2]
            y2 = sensor[3]
            # get manhattan distance from sensor to beacon
            distance = abs(x1 - x2) + abs(y1 - y2)
            # check no Beacon
            if x == x2 and y == y2:
                # print(f"beacon exists ({x2},{y2})")
                break
            # distance from sensor to point
            line_distance = abs(x1 - x) + abs(y1 - y)
            # print(
            # f"line_distance {line_distance} distance {distance} x {x} y {y} x1 {x1} y1 {y1} x2 {x2} y2 {y2}"
            # )
            if line_distance <= distance:
                # print(f"point ({x},{y}) is in range of sensor ({x1},{y1})")
                count += 1
                break
    # wrong answer too low 5350387
    # 5157464 second answer for row 2000000
    # 5511201
    print(f"count {count}")
    print(header_line)


def solve_part2():
    print(header_line)
    print(f"solution part 2")
    # solution code
    # get sensor and beacon data
    sensors = []
    for line in data.splitlines():
        sensor_beacon_pair = extract_numbers_from_string(line)
        sensors.append(sensor_beacon_pair)
    sensor_distances = []
    for sensor in sensors:
        x1 = sensor[0]
        y1 = sensor[1]
        x2 = sensor[2]
        y2 = sensor[3]
        # get manhattan distance from sensor to beacon
        distance = abs(x1 - x2) + abs(y1 - y2)
        sensor_distances.append([x1, y1, distance])
    found = False
    for x in range(0, 4000000):
        for y in range(0, 4000000):
            in_range = 0
            if y % 100000 == 0:
                print(x, y)
            for sensor in sensor_distances:
                line_distance = abs(sensor[0] - x) + abs(sensor[1] - y)
                if line_distance <= sensor[2]:
                    in_range += 1
            if in_range == 0:
                print(
                    f"point ({x},{y}) is not in range of all sensors with in_range {in_range}"
                )
                print(4000000 * x + y)
                found = True
                break
        if found:
            break

    print(header_line)


def solve_part2_1():
    # solution code
    # get sensor and beacon data
    sensors = []
    for line in data.splitlines():
        sensor_beacon_pair = extract_numbers_from_string(line)
        sensors.append(sensor_beacon_pair)
    sensor_distances = []
    for sensor in sensors:
        x1 = sensor[0]
        y1 = sensor[1]
        x2 = sensor[2]
        y2 = sensor[3]
        # get manhattan distance from sensor to beacon
        distance = abs(x1 - x2) + abs(y1 - y2)
        sensor_distances.append([x1, y1, distance])
    LINES = 4000000
    for line in range(0, LINES):
        ranges = []
        print(line)
        for sensor in sensor_distances:
            x1 = sensor[0]
            y1 = sensor[1]
            distance = sensor[2]
            # check if line is in range of sensor
            # build range of sensor over line
            # check if line is in range of sensor
            if sensor[1] - sensor[2] <= line <= sensor[1] + sensor[2]:
                # get x range of sensor over this line
                ranges.append(
                    [
                        sensor[2] - abs(line - sensor[1]),
                        sensor[2] + abs(line - sensor[1]),
                    ]
                )
        # merge ranges
        for r1 in ranges:
            for r2 in ranges:
                if r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]:
                    r1[0] = min(r1[0], r2[0])
                    r1[1] = max(r1[1], r2[1])
                    ranges.remove(r2)
        print(f"line {line} ranges {ranges}")


if __name__ == "__main__":
    # solve_part1()
    solve_part2_1()
