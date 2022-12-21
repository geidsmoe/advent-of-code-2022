class Monkey:

    def __init__(self) -> None:
        self.starting_items = []
        self.operand = None
        self.operator = None
        self.divisible_by = None
        self.next_monkeys = {True: -1, False: -1}
        self.items_inspected = 0

    def inspect(self, item):
        if self.operand == None:
            return self.operator(item, item)
        else:
            return self.operator(item, self.operand)

    def __str__(self):
        return f"{self.items_inspected}"

add = lambda x, y: x + y

multiply = lambda x, y: x * y

def part1(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.starting_items) > 0:
                item = monkey.starting_items.pop(0)
                item = monkey.inspect(item)
                item //= 3
                monkey.items_inspected += 1
                throw_to_monkey = monkey.next_monkeys[item % monkey.divisible_by == 0]
                monkeys[throw_to_monkey].starting_items.append(item)
    
    for monkey in monkeys:
        print(monkey)

from math import gcd
from functools import reduce

def lcm(a,b):
  return (a * b) // gcd(a,b)

def part2(monkeys):

    mod = reduce(lcm, [monkey.divisible_by for monkey in monkeys])

    for i in range(10000):
        for monkey in monkeys:
            while len(monkey.starting_items) > 0:
                item = monkey.starting_items.pop(0)
                item = monkey.inspect(item)
                item %= mod
                monkey.items_inspected += 1
                throw_to_monkey = monkey.next_monkeys[item % monkey.divisible_by == 0]
                monkeys[throw_to_monkey].starting_items.append(item)
    
    inspecteds = sorted([monkey.items_inspected for monkey in monkeys])
    print(inspecteds[-1] * inspecteds[-2], inspecteds)


if __name__ == "__main__":
    f = open("data/day11.txt")

    monkeys = []

    line = f.readline()

    while line != "":
        line = line.strip().split(":")
        if line[0].startswith("Monkey"):
            monkeys.append(Monkey())
        elif line[0] == "Starting items":
            monkeys[-1].starting_items += map(int, line[1].strip().split(", "))
        elif line[0] == "Operation":
            expression = line[1].strip().split("=")[1].strip().split()
            operator, operand = expression[1], expression[2]
            if operator == "+":
                monkeys[-1].operator = add
                if operand == "old":
                    monkeys[-1].operand = None
                else:
                    monkeys[-1].operand = int(operand)
            elif operator == "*":
                monkeys[-1].operator = multiply
                if operand == "old":
                    monkeys[-1].operand = None
                else:
                    monkeys[-1].operand = int(operand)
        elif line[0] == "Test":
            monkeys[-1].divisible_by = int(line[1].split()[-1])
            next_line = f.readline()
            monkeys[-1].next_monkeys[True] = int(next_line.split()[-1])
            next_line = f.readline()
            monkeys[-1].next_monkeys[False] = int(next_line.split()[-1])
        
        line = f.readline()

    for monkey in monkeys:
        print(monkey)

    print("----------------------")

    part2(monkeys)