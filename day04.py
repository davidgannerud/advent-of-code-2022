import re

input_file = 'input-day04.txt'
# input_file = 'test.txt'

# Part 1
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        pairs = re.split('[,-]', line)
        pairs = list(map(int, pairs))

        if ((pairs[0] <= pairs[2]) and (pairs[1] >= pairs[3])):
            print("Hit 1:", pairs)
            res += 1
        elif (pairs[2] <= pairs[0] and pairs[3] >= pairs[1]):
            res += 1
            print("Hit 2:", pairs)

print("Part 1:", res)
print("\n")

# Part 2
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        pairs = re.split('[,-]', line)
        pairs = list(map(int, pairs))

        if ((pairs[0] >= pairs[2]) and (pairs[0] <= pairs[3])):
            print("Hit 1:", pairs)
            res += 1
        elif (pairs[1] >= pairs[2] and pairs[1] <= pairs[3]):
            res += 1
            print("Hit 2:", pairs)
        elif (pairs[2] >= pairs[0] and pairs[2] <= pairs[1]):
            res += 1
            print("Hit 3:", pairs)
        elif (pairs[3] >= pairs[0] and pairs[3] <= pairs[1]):
            res += 1
            print("Hit 4:", pairs)

print("Part 2:", res)