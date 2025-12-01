import io
import numpy as np

LOCK_STARTING_POSITION = 50

DISPLAY_LENGTH = 100

data = []
with io.open("day_1/input.txt", "r") as file:
    for line in file:
        data.append(int(line.strip().replace("L", "-").replace("R", "+")))

lock_movements = np.array(data)

def calculate_lock_crossing_zero(starting_position, movement) -> int:
    if movement == 0:
        return 0
    
    ending_position = starting_position + movement

    if movement > 0:
        # Moving right: count multiples of 100 in (starting_position, ending_position]
        first_multiple_index = (starting_position // 100) + 1
        last_multiple_index = ending_position // 100

        if first_multiple_index > last_multiple_index:
            return 0
        
        return last_multiple_index - first_multiple_index + 1
    else:
        # Moving left: count multiples of 100 in [ending_position, starting_position)
        first_multiple_index = (ending_position + 99) // 100
        last_multiple_index = (starting_position - 1) // 100

        if first_multiple_index > last_multiple_index:
            return 0

        return last_multiple_index - first_multiple_index + 1

lock_at_zero = 0
lock_crossing_zero = 0
lock_position = LOCK_STARTING_POSITION
for movement in lock_movements:
    print(f"lock_position: {lock_position}")
    print(f"movement: {movement}")
    # Count the number of times the lock crosses zero
    lock_crossing_zero += calculate_lock_crossing_zero(lock_position, movement)

    # Update the lock position
    lock_position += movement
    lock_position = lock_position % 100

    # Count the number of times the lock is at zero
    if lock_position == 0:
        lock_at_zero += 1

print(f"lock_at_zero: {lock_at_zero}")
print(f"lock_crossing_zero: {lock_crossing_zero}")