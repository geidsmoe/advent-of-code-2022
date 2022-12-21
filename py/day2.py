
RPS1 = ("A", "B", "C")#{"A": 0, "B": 1, "C": 2}
RPS2 = ("X", "Y", "Z")#{"X": 0, "Y": 1, "Z": 2}


def part1():
    f = open("data/day02.txt")

    score = 0

    for line in f.readlines():
        theirs, ours = line.split()
        if RPS1.index(theirs) == RPS2.index(ours):
            score += RPS2.index(ours)+1 + 3
        elif (RPS1.index(theirs) - 1) % 3 == RPS2.index(ours):
            score += RPS2.index(ours)+1
        else:
            score += RPS2.index(ours)+1 + 6
    
    print(score)

def part2():
    f = open("data/day02.txt")

    score = 0

    for line in f.readlines():
        theirs, ldw = line.split()

        if ldw == "X":
            score += (RPS1.index(theirs)-1) % 3 + 1
        elif ldw == "Y":
            score += RPS1.index(theirs)+1 + 3
        else:
            score += (RPS1.index(theirs)+1) % 3 + 1 + 6

    
    print(score)

if __name__ == "__main__":
    #part1()
    part2()