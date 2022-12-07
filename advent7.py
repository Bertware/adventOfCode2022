# Part 1
import queue

def get_directory_sizes():
    f = open("advent7.txt", "r")
    stack = queue.LifoQueue()
    path = ""
    sizes = {}
    for line in f:
        line = line.strip()
        if line == "$ cd /":
            path = "/"
            stack.put('/')
            sizes["/"] = 0
            continue
        if line == "$ ls":
            continue
        if line.startswith('dir'):
            continue
        if line == "$ cd ..":
            print("Move up")
            print(f"Path {path} has size {sizes[path]}")
            stack.get()  # Remove the current path
            path = stack.get()  # Get the previous path
            stack.put(path)  # re-insert the now current path
            print("Moved up to " + path)
            continue
        if line.startswith('$ cd'):
            print("Move down to  '" + path + line[5:] + "/'")
            stack.put(path + line[5:] + "/")
            path += line[5:] + "/"
            sizes[path] = 0
            continue
        file_size = int(line.split(' ')[0])
        print(f"File {file_size}")
        active_paths = list(stack.queue)
        for active_path in active_paths:
            sizes[active_path] += file_size
    while stack.qsize() > 1:
        print("Move up, finished")
        print(f"Path {path} has size {sizes[path]}")
        stack.get()  # Remove the current path
        path = stack.get_nowait()  # Get the previous path
        stack.put(path)  # re-insert the now current path
    return sizes


sizes = get_directory_sizes()
result = 0
for path in sizes.keys():
    if sizes[path] < 100000:
        result += sizes[path]

print(result)

result = 70000000  # Start really large so we can find the smallest value
disk_size = 70000000
disk_usage = sizes['/']
free_space = disk_size - disk_usage
free_space_requirement = 30000000
minimum_removal_size = free_space_requirement - free_space

for path in sizes.keys():
    if minimum_removal_size < sizes[path] < result:
        result = sizes[path]  # Start really large so we can find the smallest value

print(result)
