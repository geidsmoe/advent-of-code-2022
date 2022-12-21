def part1():
    f = open("data/day01.txt")

    current_sum = 0
    current_max = 0

    for l in f.readlines():
        if l != "\n":
            current_sum += int(l)
            current_max = current_sum if current_sum > current_max else current_max
        else:
            current_sum = 0
    
    print(current_max)

def part2():
    f = open("data/day01.txt")

    sums = [0]

    for l in f.readlines():
        if l != "\n":
            sums[-1] += int(l)
        else:
            sums.append(0)

    sums = sorted(sums, reverse=True)

    print(sum(sums[:3]))



if __name__ == "__main__":
    #part1()
    part2()