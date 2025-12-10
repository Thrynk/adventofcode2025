# This problem looks like a graph problem.
# We have an inital state and a target state.
# Each state should be a node in the graph. It should be smartly represented as a bitmask.
# Each button should be an edge in the graph.
# We need to find the shortest path from the initial state to the target state.
# As presses are always adding 1, this graph is unweighted.
# Size of the state space is 2^11 = 2048. Not too big.
# Google Search for "Shortest path in an unweighted graph" to find the algorithm to use.
# Result:https://www.geeksforgeeks.org/dsa/shortest-path-unweighted-graph/
# It is called Breadth-First Search (BFS).

import io
from collections import deque

data = []
with io.open("day_10/input.txt", "r") as file:
    for line in file:
        # Parse target state
        target_state = line.split("[")[1].split("]")[0]
        parsed_target_state = []
        for char in target_state:
            if char == "#":
                parsed_target_state.append(1)
            else:
                parsed_target_state.append(0)

        buttons_part = line.split("]")[1].split("{")[0].strip()
        parsed_buttons = []
        for button in buttons_part.split(" "):
            parsed_buttons.append(tuple([int(x) for x in button[1:-1].split(",")]))

        data.append({
            "target_state": parsed_target_state,
            "buttons": parsed_buttons,
            "joltages": None,
        })

def state_to_bitmask(state):
    """Converts a state list to a bitmask integer."""
    mask = 0
    for i, light in enumerate(state):
        if light:
            mask |= (1 << i)
    return mask

def transition_state(mask, button):
    new_mask = mask
    for light in button:
        # Toggle the light
        new_mask ^= (1 << light)
    return new_mask

def breadth_first_search(initial_state, target_state, buttons):
    initial_mask = state_to_bitmask(initial_state)
    target_mask = state_to_bitmask(target_state)

    # BFS setup
    queue = deque()
    # Add the initial state to the queue
    queue.append((initial_mask, 0))
    # Add the initial state to the visited set
    visited = set()
    visited.add(initial_mask)

    # While the queue is not empty
    while queue:
        # Pop the first state from the queue
        current_mask, presses = queue.popleft()

        # Check if we've reached the target
        if current_mask == target_mask:
            return presses

        # Try pressing each button
        for button in buttons:
            new_mask = transition_state(current_mask, button)
            if new_mask not in visited:
                visited.add(new_mask)
                queue.append((new_mask, presses + 1))

print(data)

total_presses = 0
for entry in data:
    initial_state = [0] * len(entry["target_state"])
    entry_minimal_presses = breadth_first_search(initial_state, entry["target_state"], entry["buttons"])
    print(f"Entry minimal presses: {entry_minimal_presses}")
    total_presses += entry_minimal_presses

print(f"Total presses: {total_presses}")