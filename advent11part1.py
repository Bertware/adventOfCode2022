from enum import Enum

f = open("advent11.txt", "r")


class Operation(Enum):
    ADD = 0
    MULTIPLY = 1


class Monkey:
    def __init__(self, number: int, starting_items, operation: Operation, operation_value: int, division_test: int,
                 receiver_true_id: int,
                 receiver_false_id: int):
        self.number = number
        self.items = starting_items
        self.operation = operation
        self.operation_value = operation_value
        self.division_test = division_test
        self.receiver_true_id = receiver_true_id
        self.receiver_false_id = receiver_false_id
        self.receiver_true = None
        self.receiver_false = None
        self.inspect_count = 0

    def set_receivers(self, on_true, on_false):
        self.receiver_true = on_true
        self.receiver_false = on_false

    def inspect_items(self):
        for index, value in enumerate(self.items):
            print(f"Inspect {value} at index {index}")
            self.inspect_count += 1
            if self.operation == Operation.ADD:
                if self.operation_value == -1:
                    value += value
                else:
                    value += self.operation_value
            elif self.operation == Operation.MULTIPLY:
                if self.operation_value == -1:
                    value *= value
                else:
                    value *= self.operation_value
            print(f"Became {value}")
            value //= 3
            print(f"Relief {value}")
            if value % self.division_test == 0:
                print(f"Throw to {self.receiver_true.number}")
                self.receiver_true.items.append(value)
            else:
                print(f"Throw to {self.receiver_false.number}")
                self.receiver_false.items.append(value)
        self.items = []


def parse_monkeys():
    monkey_number = 0
    monkeys = []
    items = []
    operation = None
    operation_value = 0
    module_requirement = 0
    receiver_true = 0
    receiver_false = 0
    for line in f:
        line = line.rstrip()
        if line.startswith('Monkey'):
            monkey_number = int(line[7:8])
            continue
        if line.startswith('  Operation: new = old + '):
            operation = Operation.ADD
            if line[25:] == 'old':
                operation_value = -1
            else:
                operation_value = int(line[25:])
            continue
        if line.startswith('  Operation: new = old * '):
            operation = Operation.MULTIPLY
            if line[25:] == 'old':
                operation_value = -1
            else:
                operation_value = int(line[25:])
            continue
        if line.startswith('  Starting items: '):
            items = [int(x) for x in line[18:].split(', ')]
            continue
        if line.startswith('  Test: divisible by '):
            module_requirement = int(line[21:])
            continue
        if line.startswith('    If true: throw to monkey '):
            receiver_true = int(line[29:])
            continue
        if line.startswith('    If false: throw to monkey '):
            receiver_false = int(line[30:])
            continue
        if line == '':
            monkeys.insert(monkey_number,
                Monkey(monkey_number, items, operation, operation_value, module_requirement, receiver_true,
                       receiver_false)
            )
            continue
    monkeys.append(
        Monkey(monkey_number, items, operation, operation_value, module_requirement, receiver_true, receiver_false)
    )

    for monkey in monkeys:
        monkey.set_receivers(monkeys[monkey.receiver_true_id], monkeys[monkey.receiver_false_id])

    return monkeys

monkeys = parse_monkeys()
for round in range(20):
    for monkey in monkeys:
        monkey.inspect_items()

inspect_counts = [monkey.inspect_count for monkey in monkeys]
inspect_counts.sort(reverse=True)
print(inspect_counts)
print(inspect_counts[0] * inspect_counts[1])
