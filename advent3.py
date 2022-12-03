import time


def get_score(char: chr) -> int:
    if ord(char) > 96:
        return ord(char) - ord('a') + 1
    return 26 + (ord(char) - ord('A')) + 1


def part1_mergesort(f):
    score = 0
    for line in f:
        comp1 = line[0:len(line) // 2]
        comp2 = line[len(line) // 2:len(line) - 1]
        comp1 = {char for char in comp1}
        comp1 = list(comp1)
        comp1.sort()
        comp2 = {char for char in comp2}
        comp2 = list(comp2)
        comp2.sort()
        j = 0
        for i in range(0, len(comp1)):
            while j < len(comp2) and comp1[i] > comp2[j]:
                j += 1
            if j < len(comp2) and comp1[i] == comp2[j]:
                score += get_score(comp1[i])
    return score


def part1_intersect(f):
    score = 0
    for line in f:
        comp1 = line[0:len(line) // 2]
        comp2 = line[len(line) // 2:len(line) - 1]
        comp1 = {char for char in comp1}
        comp2 = {char for char in comp2}
        for char in comp1.intersection(comp2):
            score += get_score(char)
    return score

# PArt 1 using merge sort
start = time.time()
for x in range(0, 5):
    f = open("gen3.txt", "r")
    score = part1_mergesort(f)
    print(score)
print((time.time() - start) / 5)

# Part 1 using set intersect
start = time.time()
for x in range(0, 5):
    f = open("gen3.txt", "r")
    score = part1_intersect(f)
    print(score)
print((time.time() - start) / 5)

# Part 2
start = time.time()
score = 0
f = open("gen3.txt", "r")
lines = []
for line in f:
    lines.append(line.strip())
    if len(lines) != 3:
        continue
    comp1 = {char for char in lines[0]}
    comp2 = {char for char in lines[1]}
    comp3 = {char for char in lines[2]}
    for char in comp1.intersection(comp2).intersection(comp3):
        scoreToAdd = get_score(char)
        score += scoreToAdd
    lines = []

print(score)
print(time.time() - start)
