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

max_recursion_level = 6
results = []

# need to track all the open valves
def moveToValve(
    valve: list,
    discovered_valves: list,
    remaining_minutes: int,
    pressure_released: int,
    recursion_level: int,
):
    """
    Resursive function to traverse the tunnel system
    keep track of remaining_minutes
    discovered valves should not be traversed again
    @param valve: the valve we are currently at
    @param discovered_valves: the valves we have discovered so far
    @param remaining_minutes: the remaining minutes we have to traverse the tunnel system
    @param pressure_released: the pressure released so far
    @param recursion_level: the current recursion level
    @return (remaining_minutes, pressure_released)

    """
    if recursion_level > max_recursion_level:
        return

    if remaining_minutes <= 0:
        results.append(pressure_released)
        return
    # cost of traversing to this valve  = 1 minute
    remaining_minutes -= 1
    discovered_valves.append(valve[1])

    print(f"valve = {valve}")
    print(f"discovered_valves = {discovered_valves}")
    # cost of opening this valve = 1 minute
    if valve[-1] > 0:

        pressure_released += valve[-1] * remaining_minutes
        print(f"pressure_released by this valve: {valve[-1]}")
        print(
            f"eventual pressure released: {pressure_released} with {remaining_minutes} minutes remaining"
        )
        remaining_minutes -= 1

    print()
    child_valves = sorted(
        [v for v in valves if v[1] in valve[2:-1] and v[1] not in discovered_valves],
        key=lambda x: -x[-1],
    )

    print(f"child_valves = {child_valves}")
    for child_valve in child_valves:
        if child_valve[1] in discovered_valves:
            continue

        moveToValve(
            child_valve,
            discovered_valves,
            remaining_minutes,
            pressure_released,
            recursion_level + 1,
        )

    return (remaining_minutes, pressure_released)


# maximum cost matrix with limit on number of edges and nodes to traverse
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def buildAdjacencyMatrix(self):
        matrix = [[0 for x in range(self.V)] for y in range(self.V)]
        print(f"matrix = {matrix}")
        for u in self.graph:
            print(f"u = {u}")
            for v, w in self.graph[u]:
                print(f"u = {u}, v = {v}, w = {w}")
                _u = get_index_from_valve_name(u)
                v = get_index_from_valve_name(v)
                print(f"u = {_u}, v = {v}, w = {w}")
                matrix[_u][v] = w
        for row in matrix:
            print(row)

    def maxCostMatrix(self):
        self.buildAdjacencyMatrix()
        dist = [float("Inf")] * self.V
        dist[0] = 0
        print(f"len(V) = {self.V}")
        for _ in range(self.V - 1):
            for u in range(self.V):
                for v, w in self.graph[u]:
                    print(f"u = {u}, v = {v}, w = {w}")
                    if dist[u] != float("Inf") and dist[u] + w > dist[v]:
                        dist[v] = dist[u] + w

        for u in range(self.V):
            for v, w in self.graph[u]:
                print(f"u = {u}, v = {v}, w = {w}")
                if dist[u] != float("Inf") and dist[u] + w > dist[v]:
                    print("Graph contains negative weight cycle")
                    return

        self.printArr(dist)

    def printGraph(self):
        print(self.graph)


def get_index_from_valve_name(valve_name: str):
    print(valve_name)
    print([v[0] for v in valves if v[1] == valve_name])
    return [v[0] for v in valves if v[1] == valve_name][0]


def solve_part1():
    print(header_line)
    print(f"solution part 1")

    # solution code

    # Valve AA has flow rate=0; tunnels lead to Valves DD II BB
    for i, line in enumerate(data.splitlines()):
        print(line)
        valve = []
        valve.append(i)
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
    print(header_line)
    # traverse each possible tunnel path. calculate the pressure at the end of each path
    # get path with minimum pressure
    # set first valve as discovered
    # result = moveToValve(valves[0], [], 30, 0, 0)

    # get number of vertices from valves
    g = Graph(len(valves))

    for valve in valves:
        for v in valve[2:-1]:
            rate = [vi for vi in valves if vi[1] == v][0][-1]
            g.addEdge(valve[1], v, rate)

    g.printGraph()
    g.maxCostMatrix()

    print(header_line)


def solve_part2():
    print(header_line)
    print(f"solution part 2")
    # solution code
    print()

    print(header_line)


if __name__ == "__main__":
    solve_part1()
    # solve_part2()
