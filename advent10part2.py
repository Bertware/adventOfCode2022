# Part 2
f = open("advent10.txt", "r")

cycle = -1
register_x = 1
signal_strength = 0

for line in f:
    cycle += 1
    if register_x - 1 <= cycle % 40 <= register_x + 1:
        print('.', end='')
    else:
        print('#', end='')
    if cycle > 0 and cycle % 40 == 0:
        print()
    line = line.strip()
    command = line.split(' ')[0]

    if command == 'noop':
        continue
    if command == 'addx':
        value = int(line.split(' ')[1])
        cycle += 1
        if register_x - 1 <= cycle % 40 <= register_x + 1:
            print('.', end='')
        else:
            print('#', end='')
        if cycle > 0 and  cycle % 40 == 0:
            print()
        register_x += value

print(signal_strength)
