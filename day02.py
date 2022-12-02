score = 0

# Rock A X 1 lose
# Paper B Y 2 draw
# Scissors C Z 3 win

with open('input-day02.txt') as f:
    for line in f:
        line = line.strip()
        if (line == "A X"):
            score += 1 + 3
        elif (line == "A Y"):
            score += 2 + 6
        elif (line == "A Z"):
            score += 3 + 0
        elif (line == "B X"):
            score += 1 + 0
        elif (line == "B Y"):
            score += 2 + 3
        elif (line == "B Z"):
            score += 3 + 6
        elif (line == "C X"):
            score += 1 + 6
        elif (line == "C Y"):
            score += 2 + 0
        elif (line == "C Z"):
            score += 3 + 3

print(score)

score = 0
with open('input-day02.txt') as f:
    for line in f:
        line = line.strip()
        if (line == "A X"):
            score += 0 + 3
        elif (line == "A Y"):
            score += 3 + 1
        elif (line == "A Z"):
            score += 6 + 2
        elif (line == "B X"):
            score += 0 + 1
        elif (line == "B Y"):
            score += 3 + 2
        elif (line == "B Z"):
            score += 6 + 3
        elif (line == "C X"):
            score += 0 + 2
        elif (line == "C Y"):
            score += 3 + 3
        elif (line == "C Z"):
            score += 6 + 1

print(score)