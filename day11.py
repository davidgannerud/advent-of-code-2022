import re

# input_file = 'test.txt'
input_file = 'input-day11.txt'

class Monkey:
    items = []
    operation_sign = ""
    operation_value = 0
    test_value = 0
    test_output_true = 0
    test_output_false = 0
    inspections = 0

    def calc_worry_level(self, item):
        if self.operation_value == -1:
            op_value = item
        else:
            op_value = self.operation_value

        if (self.operation_sign == "*"):
            worry_level = item * op_value
        elif (self.operation_sign == "+"):
            worry_level = item + op_value
        else:
            print("ERROR: Not supported!")

        return int(worry_level / worry_level_divider)

    def throw_item(self, level):
        if (level % self.test_value):
            monkeys[self.test_output_false].items.append(level)
        else:
            monkeys[self.test_output_true].items.append(level)
    
    def turn(self):
        for item in self.items:
            if worry_level_divider == 1:
                worry_level = item
            else:
                worry_level = self.calc_worry_level(item)
            self.throw_item(level=worry_level)
            self.inspections +=  1

        self.items = []

def parse_input():
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line.find("Monkey") != -1:
                m = Monkey()
                monkeys.append(m)
            elif line.find("Starting items") != -1:
                values = re.split('[,]', line[16:])
                monkeys[-1].items = list(map(int, values))
            elif line.find("Operation") != -1:
                monkeys[-1].operation_sign = line[21]
                if line[22:].find("old") != -1:
                    value = -1
                else:
                    value = int(line[22:])
                monkeys[-1].operation_value = value
            elif line.find("Test") != -1:
                monkeys[-1].test_value = int(line[19:])
            elif line.find("If true") != -1:
                monkeys[-1].test_output_true = int(line[24:])
            elif line.find("If false") != -1:
                monkeys[-1].test_output_false = int(line[25:])

# Part 1
worry_level_divider = 3
monkeys = []

parse_input()
for i in range(20):
    for monkey in monkeys:
        monkey.turn()

inspections = []
for i in range(len(monkeys)):
    print("Monkey", i, "inspected items ", monkeys[i].inspections," times.")
    inspections.append(monkeys[i].inspections)

inspections.sort(reverse=True)
res = inspections[0] * inspections[1]
print("Part 1:", res)

