def score(character):
    if ord(character) >= 97:
        return ord(character) - 96
    else:
        return ord(character) - 38

    f = open("data/day03.txt")
def part1():

    answer = 0

    for sack in f.readlines():
        sack = sack[:len(sack)-1] # remove newline
        s = set()
        
        middle = int(len(sack)/2)
        for c in sack[:middle]:
            s.add(c)
        for c in sack[middle:]:
            if c in s:
                answer += score(c)
                break

    print(answer)

from collections import Counter

def part2():
    f = open("data/day03.txt")

    answer = 0
    elf_num = 0
    counter = Counter()

    for sack in f.readlines():
        sack = sack[:len(sack)-1] # remove newline

        if elf_num >= 3:
            elf_num = 0
            counter = Counter()

        for c in set(sack):
            if counter[c] == 2 and elf_num == 2:
                answer += score(c)
                break
            else:
                counter[c] += 1

        elf_num += 1
    print(answer)

if __name__ == "__main__":
    #part1()
    part2()