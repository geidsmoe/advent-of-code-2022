
def part1():
    f = open("data/day10.txt")

    cycle = 1
    X = 1

    answer = 0

    signal_cycles = set([20, 60, 100, 140, 180, 220])

    for line in f.readlines():
        line = line.rstrip().split()

        if line[0] == "noop":
            cycle += 1
        elif line[0] == "addx":
            X += int(line[1])
            cycle += 2

        if cycle in signal_cycles:
            strength = cycle * X
            answer += strength
        elif line[0] == "addx" and cycle - 1 in signal_cycles:
            strength = (cycle - 1) * (X - int(line[1]))
            answer += strength

    print(answer)

def display_crt(crt):
    for end in range(40, 241, 40):
        begin = end - 40
        print("".join(crt[begin:end]))

def part2():
    f = open("data/day10.txt")

    queue = []
    X = 1
    cycle = 1

    crt = ["." for _ in range(240)]

    while cycle <= 240:
        if cycle == 40:
            print("yay")

        if (cycle % 40) <= X + 2 and (cycle % 40) >= X:
            crt[cycle - 1] = "#"

        if len(queue) > 0:
            X += queue.pop()
        else:
            line = f.readline().rstrip().split()
            if line[0] == "addx":
                queue.append(int(line[1]))
            elif line[0] == "noop":
                pass

        cycle += 1

    display_crt(crt)


if __name__ == "__main__":
    #part1()
    part2()