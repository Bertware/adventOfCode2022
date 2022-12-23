# Part 1
f = open("advent9.txt", "r")


def print_positions(hx, hy, tx, ty):
    print(f"Head ({hx},{hy}), Tail ({tx},{ty})")
    for y in range(5, -1, -1):
        for x in range(0, 6, 1):
            if hx == x and hy == y:
                print("H", end='')
            elif tx == x and ty == y:
                print("T", end='')
            else:
                print(".", end='')
        print()
    print()


head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
visited_positions = set()

visited_positions.add((tail_x, tail_y))

for line in f:
    line = line.strip()

    direction = line.split(' ')[0]
    steps = int(line.split(' ')[1])
    for step in range(steps):
        # print_positions(head_x, head_y, tail_x, tail_y)
        match direction:
            case 'U':
                head_y += 1
            case 'D':
                head_y -= 1
            case 'L':
                head_x -= 1
            case 'R':
                head_x += 1

        if tail_x == head_x:
            if tail_y == head_y - 2:
                tail_y += 1
            elif tail_y == head_y + 2:
                tail_y -= 1
        elif tail_y == head_y:
            if tail_x == head_x - 2:
                tail_x += 1
            elif tail_x == head_x + 2:
                tail_x -= 1
        elif abs(tail_x - head_x) + abs(tail_y - head_y) > 2:
            # Diagonal!
            if head_x > tail_x:
                tail_x += 1
            elif head_x < tail_x:
                tail_x -= 1
            if head_y > tail_y:
                tail_y += 1
            elif head_y < tail_y:
                tail_y -= 1
        visited_positions.add((tail_x, tail_y))
print(len(visited_positions))
