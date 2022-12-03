input_file = 'input-day03.txt'
# Part 1
res = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        length = len(line)
        half = int(length / 2)
        comp1 = line[0:half]
        comp2 = line[half:length]

        comp1 = "".join(set(comp1))
        comp2 = "".join(set(comp2))

        for c in comp1:
            if comp2.find(c) != -1:
                
                value = ord(c)
                print("found ", c, value)
                if (value > 96):
                    value = value - 96
                else:
                    value = value - 64 + 26
                print(value)
                res += value


    print("Part 1:", res)
    print("\n")
# # Part 2
res = 0
with open(input_file) as f:
    index = 0
    group = []
    for line in f:
        line = line.strip()
        line = "".join(set(line))
        group.append(line)
        if index < 2:
            index += 1
            continue

        index = 0
        for c in group[0]:
            if group[1].find(c) != -1 and group[2].find(c) != -1 :
                value = ord(c)
                print("found ", c, value)
                if (value > 96):
                    value = value - 96
                else:
                    value = value - 64 + 26
                print(value)
                res += value

        group.clear()

print("Part 2:", res)