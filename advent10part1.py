# Part 1
f = open("advent10.txt", "r")

cycle = 0
register_x = 1
signal_strength = 0

for line in f:
    cycle += 1
    if (cycle - 20) % 40 == 0:
        print(register_x)
        signal_strength += cycle * register_x
    line = line.strip()
    command = line.split(' ')[0]

    if command == 'noop':
        continue
    if command == 'addx':
        value = int(line.split(' ')[1])
        print(f"{cycle} START ADD " + str(value))
        cycle += 1
        if (cycle - 20) % 40 == 0:
            print(register_x)
            signal_strength += cycle * register_x
        register_x += value

print(signal_strength)
