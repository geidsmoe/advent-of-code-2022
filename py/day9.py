def move_head(head_x, head_y, direction):
    if direction == "R":
        head_x += 1
    elif direction == "L":
        head_x -= 1
    elif direction == "U":
        head_y += 1
    elif direction == "D":
        head_y -= 1

    return head_x, head_y

def calculate_point_movement(p1_x, p1_y, p2_x, p2_y):
    diff_x = abs(p1_x - p2_x)
    diff_y = abs(p1_y - p2_y)

    if diff_x <= 1 and diff_y <= 1:
        pass
    elif diff_x > diff_y:
        p2_x = p2_x + 1 if p1_x > p2_x else p2_x - 1
        if diff_y > 0:
            p2_y = p2_y + 1 if p1_y > p2_y else p2_y - 1
    elif diff_y > diff_x:
        p2_y = p2_y + 1 if p1_y > p2_y else p2_y - 1
        if diff_x > 0:
            p2_x = p2_x + 1 if p1_x > p2_x else p2_x - 1
    else:
        p2_x = p2_x + 1 if p1_x > p2_x else p2_x - 1
        p2_y = p2_y + 1 if p1_y > p2_y else p2_y - 1

    return p2_x, p2_y

def part1():
    f = open("data/day09.txt")
    lines = f.readlines()

    positions = set()

    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    for line in lines:
        direction, moves = line.strip().split()
        moves = int(moves)
        
        while moves > 0:
            head_x, head_y = move_head(head_x, head_y, direction)
            tail_x, tail_y = calculate_point_movement(head_x, head_y, tail_x, tail_y)
            positions.add((tail_x, tail_y))
            moves -= 1
            

    print(len(positions))

    for y in range(4, -1, -1):
        s = ""
        for x in range(6):
            if (x, y) in positions:
                s += "#"
            else:
                s += "."
        print(s)

def part2():
    f = open("data/day09.txt")
    lines = f.readlines()

    tail = lambda xs: xs[-1]

    positions = set()

    rope = [[0, 0] for _ in range(10)]

    for line in lines:
        direction, moves = line.strip().split()
        moves = int(moves)
        
        while moves > 0:
            rope[0][0], rope[0][1] = move_head(rope[0][0], rope[0][1], direction)

            for i in range(1, len(rope)):
                rope[i][0], rope[i][1] = calculate_point_movement(rope[i - 1][0], rope[i - 1][1], rope[i][0], rope[i][1])

            positions.add((tail(rope)[0], tail(rope)[1]))

            moves -= 1

    print(len(positions))

if __name__ == "__main__":
    #part1()
    part2()
    #print(list(yield_test()))