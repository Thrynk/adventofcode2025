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

        joltages_part = line.split("{")[1].split("}")[0].strip()
        parsed_joltages = []
        for joltage in joltages_part.split(","):
            parsed_joltages.append(int(joltage))

        data.append({
            "target_state": parsed_target_state,
            "buttons": parsed_buttons,
            "joltages": parsed_joltages,
        })

def state_to_bitmask(state):
    """Converts a state list to a bitmask integer."""
    return "".join(map(str, state))

def bitmask_to_state(mask):
    """Converts a bitmask to a state list."""
    return [int(x) for x in mask]

def transition_state(state, button):
    new_state = [digit for digit in state]
    for position in button:
        # Toggle the light
        new_state[position] +=1
    return new_state

def breadth_first_search(initial_state, target_state, buttons):
    initial_mask = state_to_bitmask(initial_state)
    print(f"Initial mask: {initial_mask}")
    target_mask = state_to_bitmask(target_state)
    print(f"Target mask: {target_mask}")

    # BFS setup
    queue = deque()
    # Add the initial state to the queue
    queue.append((initial_state, 0))
    # print(f"Initial state: {initial_state}")
    # Add the initial state to the visited set
    visited = set()
    visited.add(initial_mask)
    # print(f"Visited: {visited}")

    n = 0
    current_state = initial_state
    current_mask = state_to_bitmask(current_state)
    integer_current_state = int("".join(map(str, current_state)))
    # print(f"Integer initial state: {integer_current_state}")
    # return None
    # max_integer_state = int("".join(map(str, target_state)))
    max_state = [str(joltage) for joltage in target_state]
    print(f"Max state: {max_state}")
    max_integer_state = int("".join(max_state))
    print(f"Max integer state: {max_integer_state}")
    # return None
    # While the queue is not empty
    while queue:
        n += 1
        # Pop the first state from the queue
        current_state, presses = queue.popleft()
        integer_current_state = int("".join(map(str, current_state)))
        # print(f"Integer current state: {integer_current_state}")
        # print(f"Current state: {current_state}")
        current_mask = state_to_bitmask(current_state)
        # print(f"Current mask: {current_mask}")

        # Check if we've reached the target
        # print(f"Target mask: {target_mask}")
        if current_mask == target_mask:
            # print(f"Reached target")
            return presses

        # Try pressing each button
        for button in buttons:
            # print(f"Button: {button}")
            new_state = transition_state(current_state, button)
            print(f"New state: {new_state}")
            new_mask = state_to_bitmask(new_state)
            # print(f"New mask: {new_mask}")
            # print(f"Visited: {visited}")
            are_each_joltage_below_max = all(new_state[joltage] <= int(max_state[joltage]) for joltage in range(len(new_state)))
            if new_mask not in visited and are_each_joltage_below_max:
                # print(f"Integer new mask: {int(new_mask)}")
                # print(f"Adding new state to visited")
                visited.add(new_mask)
                queue.append((new_state, presses + 1))

# print(data)

total_presses = 0
for entry in data:
    initial_state = [0] * len(entry["joltages"])
    print("Joltages: ", entry["joltages"])
    entry_minimal_presses = breadth_first_search(initial_state, entry["joltages"], entry["buttons"])
    print(f"Entry minimal presses: {entry_minimal_presses}")
    total_presses += entry_minimal_presses

print(f"Total presses: {total_presses}")