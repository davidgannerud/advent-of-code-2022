# input_file = 'test.txt'
input_file = 'input-day06.txt'
# Part 1
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        for i in range(len(line) - 4):
            start_of_packet = line[i:i + 4]
            start_of_packet = "".join(set(start_of_packet))
            if len(start_of_packet) == 4:
                res = i + 4
                break

print("Part 1:", res)

# Part 2
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        for i in range(len(line) - 14):
            start_of_message = line[i:i + 14]
            start_of_message = "".join(set(start_of_message))
            if len(start_of_message) == 14:
                res = i + 14
                break

print("Part 2:", res)