f = open("advent1.txt", "r")
results = list()
current = 0
for line in f:
    if line == "\n":
        results.append(current)
        current = 0
        continue
    current += int(line)

results.sort(reverse=True)
print(results.__getitem__(0))
print(results.__getitem__(0) + results.__getitem__(1) + results.__getitem__(2))

