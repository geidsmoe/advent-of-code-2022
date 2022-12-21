
def calc_next(point, row_len):
    if point[0] 


def part1(graph, start):
    queue = [start]

    while queue:
        node = queue.pop(0)
        neighbors = calc_next(node, len(graph[0]))

if __name__ == "__main__":
    f = open("data/day12.test")
    graph = []
    
    start = None

    for i, line in enumerate(f.readlines()):
        line = line.strip()
        if "S" in line:
            start = (i, line.index("S"))
        graph += list(line)
    
    part1(graph, start)