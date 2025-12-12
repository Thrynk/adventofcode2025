import io
from collections import deque

data = {}
with io.open("day_11/input.txt", "r") as file:
    for line in file:
        parent = line.split(":")[0].strip()
        children = line.split(":")[1].strip().split(" ")
        data[parent] = children

print(data)

# Find parent with "you"
starting_parent = None
for parent, children in data.items():
    if parent == "you":
        starting_parent = parent
        break

print(starting_parent)

# Traverse graph from "you" to "out"
def traverse_graph(starting_parent):
    number_of_visits = {parent: 0 for parent in data.keys()}
    number_of_visits["out"] = 0
    number_of_visits[starting_parent] = 1

    queue = deque()
    queue.append((starting_parent, 1))

    while queue:
        parent, count = queue.popleft()
        print(f"Parent: {parent}, Count: {count}")
        for child in data[parent]:
            print(f"Child: {child}")
            if child != "out":
                queue.append((child, count + 1))
            number_of_visits[child] += 1
        print(f"Number of visits: {number_of_visits}")
        # else:
        #     number_of_visits[parent]

    return number_of_visits["out"]

print(traverse_graph(starting_parent))