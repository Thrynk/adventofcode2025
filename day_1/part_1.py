import io
import numpy as np

LOCK_STARTING_POSITION = 50

DISPLAY_LENGTH = 100

data = []
with io.open("day_1/input.txt", "r") as file:
    for line in file:
        data.append(int(line.strip().replace("L", "-").replace("R", "+")))

lock_movements = np.insert(np.array(data), 0, LOCK_STARTING_POSITION)
# print(data)

print(lock_movements.tolist()[:DISPLAY_LENGTH])

cumulative_lock_movements = lock_movements.cumsum()

print(cumulative_lock_movements.tolist()[:DISPLAY_LENGTH])

# Apply modulo 100 to the lock positions
lock_positions = cumulative_lock_movements % 100

print(lock_positions.tolist()[:DISPLAY_LENGTH])

lock_crossing_times = (cumulative_lock_movements // 100)

# diff the lock crossing times
print(lock_crossing_times.tolist()[:DISPLAY_LENGTH])
print(np.diff(lock_crossing_times.tolist()[:DISPLAY_LENGTH]))

number_of_lock_crossing_zero = np.diff(lock_crossing_times) >= 1
print(number_of_lock_crossing_zero.sum())

# lock_positions_on_zero = lock_positions == 0
# print(lock_positions_on_zero)
# print(lock_positions_on_zero.sum())