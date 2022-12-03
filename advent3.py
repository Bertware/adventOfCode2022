import time


def get_score(char: chr) -> int:
    if ord(char) > 96:
        return ord(char) - ord('a') + 1
    return 26 + (ord(char) - ord('A')) + 1


start = time.time()
score = 0
f = open("gen3.txt", "r")

for line in f:
    comp1 = line[0:len(line) // 2]
    comp2 = line[len(line) // 2:len(line) - 1]
    comp1 = {char for char in comp1}
    comp2 = {char for char in comp2}
    for char in comp1.intersection(comp2):
        scoreToAdd = get_score(char)
        score += scoreToAdd
del comp1
del comp2
print(score)
print(time.time() - start)

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