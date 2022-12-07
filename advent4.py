f = open("advent4.txt", "r")
complete_overlap = 0
for line in f:
    parts = line.split(',')
    start_stop_1 = parts[0].strip().split('-')
    start_stop_2 = parts[1].strip().split('-')
    if int(start_stop_1[0]) <= int(start_stop_2[0]) and int(start_stop_1[1]) >= int(start_stop_2[1]):
        complete_overlap += 1
    elif int(start_stop_1[0]) >= int(start_stop_2[0]) and int(start_stop_1[1]) <= int(start_stop_2[1]):
        complete_overlap += 1
print(complete_overlap)

f = open("advent4.txt", "r")
overlap = 0
for line in f:
    parts = line.split(',')
    start_stop_1 = parts[0].strip().split('-')
    start_stop_2 = parts[1].strip().split('-')
    if int(start_stop_1[0]) <= int(start_stop_2[0]) <= int(start_stop_1[1]):
        overlap += 1
    elif int(start_stop_2[0]) <= int(start_stop_1[0]) <= int(start_stop_2[1]):
        overlap += 1
print(overlap)
