from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 16
data = get_data_from_file(f"sample.input")
# data = get_data_from_file(f"day{DAY}.input")
print(f"transformed data for solution")
print(data)
print(header_line)

valves = []
valve_names = [
    "AA",
    "BB",
    "CC",
    "DD",
    "EE",
    "FF",
    "GG",
    "HH",
    "II",
    "JJ",
    "KK",
    "LL",
    "MM",
    "NN",
    "OO",
    "PP",
    "QQ",
    "RR",
    "SS",
    "TT",
    "UU",
    "VV",
    "WW",
    "XX",
    "YY",
    "ZZ",
]

max_recursion_level = 2
open_valves = []
skip_valves = []

# need to track all the open valves
def moveToValve(valve, minutes, recursion_level):
    if recursion_level > max_recursion_level:
        return

    if minutes <= 0:
        return

    current_pressure = sum([int(valve[-1]) for valve in open_valves])
    print(f" valves {open_valves} are open, releasing {current_pressure} pressure")

    for valve_spec in valves:
        if valve_spec[1] == valve:
            if valve_spec[-1] > 0:
                # open valve if closed
                if valve_spec[0] == False:
                    print(f"open valve {valve_spec[1]}")
                    valve_spec[0] = True
                    open_valves.append(valve_spec)
                    minutes -= 1
            else:
                skip_valves.append(valve_spec[1])
            for to_valve in valve_spec[2:-1]:
                if (
                    to_valve in [valve[1] for valve in open_valves]
                    or to_valve in skip_valves
                ):
                    continue
                print(f"move from {valve} To Valve {to_valve}")
                moveToValve(
                    to_valve,
                    minutes - 1,
                    recursion_level + 1,
                )
    return


def solve_part1():
    print(header_line)
    print(f"solution part 1")

    # solution code

    # Valve AA has flow rate=0; tunnels lead to Valves DD II BB
    for line in data.splitlines():
        print(line)
        valve = []
        valve.append(False)
        rate = 0
        for word in line.split(" "):
            if word[-1] == ",":
                word = word[:-1]
            if word in valve_names:
                valve.append(word)
            if word.startswith("rate"):
                rate = int(word.split("=")[1][:-1])
        valve.append(rate)
        valves.append(valve)
    print(valves)

    minutes = 30
    # traverse each possible tunnel path. calculate the pressure at the end of each path
    # get path with minimum pressure
    moveToValve("AA", minutes, 0)

    print(header_line)


def solve_part2():
    print(header_line)
    print(f"solution part 2")
    # solution code
    print()

    print(f"result = {X}")
    print(header_line)


if __name__ == "__main__":
    solve_part1()
    # solve_part2()
