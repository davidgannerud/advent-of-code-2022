# input_file = 'test.txt'
input_file = 'input-day08.txt'
# Part 1
res = 0
forest = []

with open(input_file) as f:
    for line in f:
        line = line.strip()
        forest.append(list(map(int, list(line))))

forest_t = list(map(list, zip(*forest)))
row = 1
not_visible = 0
while row < len(forest) - 1:
    col = 1
    while col < len(forest[0]) - 1:
        tree = forest[row][col]
        left_of_tree = forest[row][:col]
        right_of_tree = forest[row][col + 1:]
        above_tree = forest_t[col][:row]
        below_tree = forest_t[col][row + 1:]
        if (tree <= max(left_of_tree) and 
            tree <= max(right_of_tree) and
            tree <= max(above_tree) and
            tree <= max(below_tree)):
            not_visible += 1
        col += 1
    row += 1

res = len(forest) * len(forest[0]) - not_visible

print("Part 1:", res)

# Part 2
scenic_score = 0
row = 1
while row < len(forest) - 1:
    col = 1
    while col < len(forest[0]) - 1:
        tree = forest[row][col]
        left_of_tree = forest[row][:col]
        right_of_tree = forest[row][col + 1:]
        above_tree = forest_t[col][:row]
        below_tree = forest_t[col][row + 1:]
        
        ss_left = 0
        ss_right = 0
        ss_above = 0
        ss_below = 0
        left_of_tree.reverse()
        for t in left_of_tree:
            if t == tree:
                ss_left += 1
                break;
            elif t < tree:
                ss_left += 1
            else:
                break;
        
        for t in right_of_tree:
            if t == tree:
                ss_right += 1
                break;
            elif t < tree:
                ss_right += 1
            else:
                break;
        
        above_tree.reverse()
        for t in above_tree:
            if t == tree:
                ss_above += 1
                break;
            elif t < tree:
                ss_above += 1
            else:
                break;
        
        for t in below_tree:
            if t == tree:
                ss_below += 1
                break;
            elif t < tree:
                ss_below += 1
            else:
                break;

        total = ss_left * ss_right * ss_above * ss_below
        if total > scenic_score:
            scenic_score = total

        col += 1
    row += 1

print("Part 2:", scenic_score)