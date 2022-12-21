import re

def part1():
    f = open("data/day05.txt")
    
    lines = f.readlines()

    stacks = [[] for _ in range(len(lines[0]) // 4)]

    for line in lines:       
        if line[0] == '\n' or re.search("^ \d", line):
            continue
        elif line[0] == "m":
            _, quantity, _, source, _, destination = line.split()
            quantity, source, destination = int(quantity), int(source) - 1, int(destination) - 1
            for _ in range(quantity):
                crate = stacks[source].pop()
                stacks[destination].append(crate)
        else:
            begin, end = 0, 4
            while end <= len(line):
                crate = line[begin:end]
                
                if crate[0] == "[":
                    stacks[begin // 4].insert(0, crate[1])
                
                begin = end
                end += 4

    print("".join([stack[-1] for stack in stacks]))


def part2():
    f = open("data/day05.txt")
    
    lines = f.readlines()

    stacks = [[] for _ in range(len(lines[0]) // 4)]

    for line in lines:       
        if line[0] == '\n' or re.search("^ \d", line):
            continue
        elif line[0] == "m":
            _, quantity, _, source, _, destination = line.split()
            quantity, source, destination = int(quantity), int(source) - 1, int(destination) - 1
            new_len = len(stacks[source]) - quantity
            for _ in range(quantity):
                crate = stacks[source].pop(new_len)
                stacks[destination].append(crate)
        else:
            begin, end = 0, 4
            while end <= len(line):
                crate = line[begin:end]
                
                if crate[0] == "[":
                    stacks[begin // 4].insert(0, crate[1])
                
                begin = end
                end += 4

    print("".join([stack[-1] for stack in stacks]))

if __name__ == "__main__":
    #part1()
    part2()