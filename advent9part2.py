# Part 1
f = open("advent9.sample2.txt", "r")


def print_positions(px, py):
    for y in range(10, -10, -1):
        for x in range(-6, 20, 1):
            is_position = False
            for position in range(9,-1,-1):
                if not is_position and px[position] == x and py[position] == y:
                    is_position = True
                    print(position, end='')
            if not is_position:
                print(".", end='')
        print()
    print()


positions_x = [0 for i in range(10)]
positions_y = [0 for i in range(10)]
visited_positions = set()

visited_positions.add((0, 0))

for line in f:
    line = line.strip()

    direction = line.split(' ')[0]
    steps = int(line.split(' ')[1])
    for step in range(steps):
        print_positions(positions_x, positions_y)
        for position in range(9):
            match direction:
                case 'U':
                    positions_y[position] += 1
                case 'D':
                    positions_y[position] -= 1
                case 'L':
                    positions_x[position] -= 1
                case 'R':
                    positions_x[position] += 1

            if positions_x[position+1] == positions_x[position] \
                    and positions_y[position+1] == positions_y[position]:
                continue
            if positions_x[position + 1] == positions_x[position]:
                if positions_y[position + 1] == positions_y[position] - 2:
                    positions_y[position + 1] += 1
                elif positions_y[position + 1] == positions_y[position] + 2:
                    positions_y[position + 1] -= 1
            elif positions_y[position + 1] == positions_y[position]:
                if positions_x[position + 1] == positions_x[position] - 2:
                    positions_x[position + 1] += 1
                elif positions_x[position + 1] == positions_x[position] + 2:
                    positions_x[position + 1] -= 1
            elif abs(positions_x[position + 1] - positions_x[position]) + abs(
                    positions_y[position + 1] - positions_y[position]) > 2:
                # Diagonal!
                if positions_x[position] > positions_x[position + 1]:
                    positions_x[position + 1] += 1
                elif positions_x[position] < positions_x[position + 1]:
                    positions_x[position + 1] -= 1
                if positions_y[position] > positions_y[position + 1]:
                    positions_y[position + 1] += 1
                elif positions_y[position] < positions_y[position + 1]:
                    positions_y[position + 1] -= 1
        visited_positions.add((positions_x[9], positions_y[9]))
print(len(visited_positions))
