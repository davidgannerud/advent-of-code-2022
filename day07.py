import re
# input_file = 'test.txt'
input_file = 'input-day07.txt'
# Part 1
res = 0
dirs = {}
dir_hierarchy = []
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line.find('$ cd') >= 0:
            if line.find('..') >= 0:
                dir_hierarchy.pop()
            else:
                full_path = ' '.join(dir_hierarchy) + line[5:]
                dir_hierarchy.append(full_path)
                dirs[full_path] = 0
        else:
            if line[0].isdigit():
                file_size = int(line[:line.find(' ')])
                for d in dir_hierarchy:
                    dirs[d] += int(file_size)

for value in dirs.values():
    if value <= 100000:
        res += value

print("Part 1:", res)

# Part 2
res = 0
size_to_delete = abs(70000000 - dirs['/'] - 30000000)

candidates = []
for value in dirs.values():
    if value >= size_to_delete:
        candidates.append(value)

candidates.sort()
res = candidates[0]

print("Part 2:", res)