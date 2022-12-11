import numpy
# input_file = 'test.txt'
input_file = 'input-day09.txt'
# Part 1
res = 0
grid = numpy.zeros([1000,1000], dtype=int)
x = 500
y = 500
grid[y][x] = 1
head_x = x
head_y = y
tail_x = x
tail_y = y
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line.find("R") != -1:
            steps = int(line[2:])
            for i in range(0, steps):
                head_x += 1
                if abs(head_x - tail_x) > 1:
                    tail_x = head_x - 1
                    grid[head_y][tail_x] = 1
                    tail_y = head_y
        elif line.find("L") != -1:
            steps = int(line[2:])
            for i in range(0, steps):
                head_x -= 1
                if abs(head_x - tail_x) > 1:
                    tail_x = head_x + 1
                    grid[head_y][tail_x] = 1
                    tail_y = head_y
        elif line.find("U") != -1:
            steps = int(line[2:])
            for i in range(0, steps):
                head_y -= 1
                if abs(head_y - tail_y) > 1:
                    tail_y = head_y + 1
                    grid[tail_y][head_x] = 1
                    tail_x = head_x
        elif line.find("D") != -1:
            steps = int(line[2:])
            for i in range(0, steps):
                head_y += 1
                if abs(head_y - tail_y) > 1:
                    tail_y = head_y - 1
                    grid[tail_y][head_x] = 1
                    tail_x = head_x
        else:
            print("ERROR")

# print(grid)
print("Part 1:", grid.sum())

# Part 2
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()

print("Part 2:", res)