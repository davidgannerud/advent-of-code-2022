# input_file = 'test.txt'
input_file = 'input-day10.txt'

# Part 1
cycles = 0
measure_point = 20
signal_strength = []
x = [1]
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if (line.find("noop") != -1):
            cycles += 1
            instructions = 0
        else:
            instructions = int(line[5:])
            cycles += 2
        
        if cycles >= measure_point:
            signal_strength.append(sum(x) * measure_point)
            measure_point += 40

        x.append(instructions)

print("Part 1:", signal_strength, "sum:", sum(signal_strength))

# Part 2
res = 0
cycles = 0
crt = [ [ '.' for i in range(40) ] for j in range(6) ]
x2 = 1
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if (line.find("noop") != -1):
            instructions = 0
        else:
            instructions = int(line[5:])
            cycles += 1
        
        row = int(cycles / 40)
        pos = (cycles - 1) % 40
        if ((x2 - 1) <= pos and (x2 + 1) >= pos):
            crt[row][pos] = '#'
        
        cycles += 1
        row = int(cycles / 40)
        pos = (cycles - 1) % 40
        if ((x2 - 1) <= pos and (x2 + 1) >= pos):
            crt[row][pos] = '#'
        
        x2 += instructions

print("Part 2:")
for crt_row in crt:
    print(''.join(crt_row))