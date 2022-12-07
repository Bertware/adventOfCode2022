def find_unique_sequence(line, preamble_size):
    letter_count_within_window = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        letter_count_within_window[char] = 0
    line_length = len(line)
    i = 0
    while i < line_length:
        letter_count_within_window[line[i]] += 1
        if i >= preamble_size:  # Only start removing indata after the right number of characters
            letter_count_within_window[line[i - preamble_size]] -= 1
            if max(letter_count_within_window.values()) < 2:
                return i + 1
        i += 1
    return -1


print(find_unique_sequence('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjwaaaaaaa', 14))  # 26
print(find_unique_sequence('nppdvjthqldpwncqszvftbrmjlhg', 14))  # 23

# Part 1
f = open("advent6.txt", "r")
for line in f:
    i = find_unique_sequence(line.strip(), 4)
    print(i)
    print(line[i - 3] + line[i - 2] + line[i - 1] + line[i])  # Output to verify

# Part 2
f = open("advent6.txt", "r")
for line in f:
    i = find_unique_sequence(line.strip(), 14)
    print(i)
