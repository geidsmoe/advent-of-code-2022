from collections import OrderedDict, Counter

def part1():
    f = open("data/day06.txt")

    input = f.readline()

    window = []

    for i, c in enumerate(input):
        if len(set(window)) == 4:
            return i, window           
        else:
            window.append(c)
        
        if len(window) > 4:
            window.pop(0)

def part2():
    f = open("data/day06.txt")

    input = f.readline()

    window = []

    for i, c in enumerate(input):
        if len(set(window)) == 14:
            return i, window           
        else:
            window.append(c)
        
        if len(window) > 14:
            window.pop(0)
            
if __name__ == "__main__":
    print(part2())