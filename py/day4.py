def in_interval(value, interval):
    return interval[0] <= value <= interval[1]

def part1():
    f = open("data/day04.txt")

    answer = 0

    for line in f.readlines():
        lhs, rhs = line.split(",")
        lhs = list(map(int, lhs.split("-")))
        rhs = list(map(int, rhs.split("-")))

        if (in_interval(rhs[0], lhs) and in_interval(rhs[1], lhs)) or (in_interval(lhs[0], rhs) and in_interval(lhs[1], rhs)):
            answer += 1


    print(answer)

def part2():
    f = open("data/day04.txt")

    answer = 0

    for line in f.readlines():
        lhs, rhs = line.split(",")
        lhs = list(map(int, lhs.split("-")))
        rhs = list(map(int, rhs.split("-")))

        if in_interval(rhs[0], lhs) or in_interval(rhs[1], lhs) or in_interval(lhs[0], rhs) or in_interval(lhs[1], rhs):
            answer += 1

    print(answer)

if __name__ == "__main__":
    #part1()
    part2()