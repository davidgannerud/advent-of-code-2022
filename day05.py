crates_begin = [
['T','Z','B'],
['N' ,'D' ,'T' ,'H' ,'V'],
['D' ,'M' ,'F' ,'B'],
['L' ,'Q' ,'V' ,'W' ,'G' ,'J' ,'T'],
['M' ,'Q' ,'F' ,'V' ,'P' ,'G' ,'D' ,'W'],
['S' ,'F' ,'H' ,'G' ,'Q' ,'Z' ,'V'],
['W' ,'C' ,'T' ,'L' ,'R' ,'N' ,'S' ,'Z'],
['M' ,'R' ,'N' ,'J' ,'D' ,'W' ,'H' ,'Z'],
['S' ,'D' ,'F' ,'L' ,'Q' ,'M']]

input_file = 'input-day05.txt'
# input_file = 'test.txt'
# Part 1
crates = crates_begin
with open(input_file) as f:
    for line in f:
        line = line.strip()
        instruction = line.split()
        num_of_crate = int(instruction[0])
        src = int(instruction[1]) - 1
        dest = int(instruction[2]) - 1

        part = crates[src][:num_of_crate]
        part.reverse()
        crates[dest] = part + crates[dest]
        crates[src] = crates[src][num_of_crate:]

print("Part 1:", [i[0] for i in crates])

# Part 2
crates = crates_begin
with open(input_file) as f:
    for line in f:
        line = line.strip()
        instruction = line.split()
        num_of_crate = int(instruction[0])
        src = int(instruction[1]) - 1
        dest = int(instruction[2]) - 1

        part = crates[src][:num_of_crate]
        crates[dest] = part + crates[dest]
        crates[src] = crates[src][num_of_crate:]

print("Part 2:", [i[0] for i in crates])
