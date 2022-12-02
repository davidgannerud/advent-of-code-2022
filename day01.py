calories = 0
elf_list = []
elf = 0
max_cal_elf = 0
max_cal = 0

with open('input-day01.txt') as f:
    for line in f:
        if (line == "\n"):
            print(calories)
            if calories > max_cal:
                max_cal_elf = elf
                max_cal = calories

            elf_list.append(calories)
            elf += 1
            calories = 0
        else:
            calories += int(line)

print(calories)
if calories > max_cal:
    max_cal_elf = elf
    max_cal = calories
elf_list.append(calories)

calories = 0
max_elf = 0
top_3 = 0
for i in range(3):
    for elf_cal in elf_list:
        if elf_cal > calories:
            calories = elf_cal
    top_3 += calories
    elf_list.remove(calories)
    calories = 0


print("Elf with most calories: ", max_cal_elf +1, max_cal)

print(top_3)

