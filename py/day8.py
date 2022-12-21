import numpy as np 


def part1():
    f = open("data/day08.txt")
    forest = []
    for line in f.readlines():
        forest.append(list(map(lambda x: [int(x), False], list(line.strip()))))

    # see which trees are visible along the rows
    for i, row in enumerate(forest):
        max_from_left = None
        max_from_right = None
        for j in range(len(row)):
            if max_from_left == None or forest[i][j][0] > max_from_left:
                max_from_left = forest[i][j][0]
                forest[i][j][1] = True

            if max_from_right == None or forest[i][-1 - j][0] > max_from_right:
                max_from_right = forest[i][-1 - j][0]
                forest[i][-1 - j][1] = True

    # see which trees are visible along the columns
    for j in range(len(forest[0])):
        max_from_top = None
        max_from_bottom = None
        for i in range(len(forest)):
            if max_from_top == None or forest[i][j][0] > max_from_top:
                max_from_top = forest[i][j][0]
                forest[i][j][1] = True

            if max_from_bottom == None or forest[-1 - i][j][0] > max_from_bottom:
                max_from_bottom = forest[-1 - i][j][0]
                forest[-1 - i][j][1] = True

    answer = 0

    for row in forest:
        answer += sum([1 for tree in row if tree[1]])

    print(answer)
    

def part2():

    def calc_score(m, i, j):
        if i == 0 or j == 0 or i == len(m) - 1 or j == len(m[0]) - 1:
            return 0

        origin_height = m[i][j][0]
        horizontal_left, horizontal_right = j - 1, j + 1
        vertical_top, vertical_bottom = i - 1, i + 1

        while m[i][horizontal_left][0] < origin_height and horizontal_left > 0:
            horizontal_left -= 1
        
        while m[i][horizontal_right][0] < origin_height and horizontal_right < len(m[0]) - 1:
            horizontal_right += 1

        while m[vertical_top][j][0] < origin_height and vertical_top > 0:
            vertical_top -= 1

        while m[vertical_bottom][j][0] < origin_height and vertical_bottom < len(m) - 1:
            vertical_bottom += 1

        return (j - horizontal_left) * (horizontal_right - j) * (i - vertical_top) * (vertical_bottom - i)


    f = open("data/day08.txt")
    forest = []
    for line in f.readlines():
        forest.append(list(map(lambda x: [int(x), 0], list(line.strip()))))

    max_score = 0

    for i, row in enumerate(forest):
        for j, _ in enumerate(range(len(row))):
            score = calc_score(forest, i, j)
            forest[i][j][1] = score
            max_score = score if score > max_score else max_score
            
    print(max_score)

if __name__ == "__main__":
    #part1()
    part2()