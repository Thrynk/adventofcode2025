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
# print(lock_movements.tolist()[:DISPLAY_LENGTH])

cumulative_lock_movements = lock_movements.cumsum()

# print(cumulative_lock_movements.tolist()[:DISPLAY_LENGTH])

# Apply modulo 100 to the lock positions
lock_positions = cumulative_lock_movements % 100

# print(lock_positions.tolist()[:DISPLAY_LENGTH])

lock_crossing_times = (cumulative_lock_movements // 100)

# diff the lock crossing times
# print(lock_crossing_times.tolist()[:DISPLAY_LENGTH])
# print(np.diff(lock_crossing_times.tolist()[:DISPLAY_LENGTH]))

number_of_lock_crossing_zero = np.abs(np.diff(lock_crossing_times))
# print(number_of_lock_crossing_zero.sum())

print(list(zip(
    lock_movements.tolist()[:DISPLAY_LENGTH], 
    cumulative_lock_movements.tolist()[:DISPLAY_LENGTH], 
    lock_positions.tolist()[:DISPLAY_LENGTH], 
    # (cumulative_lock_movements - 100).tolist()[:DISPLAY_LENGTH], 
    # (np.sign(cumulative_lock_movements - 100)).tolist()[:DISPLAY_LENGTH],
    ((lock_positions + np.roll(lock_movements, -1) )).astype(int).tolist()[:DISPLAY_LENGTH],
    np.abs((lock_positions + np.roll(lock_movements, -1))).astype(int).tolist()[:DISPLAY_LENGTH],
    (np.abs((lock_positions + np.roll(lock_movements, -1))) // 100).astype(int).tolist()[:DISPLAY_LENGTH],
)))

lock_positions_on_zero = lock_positions == 0
print(f"lock_positions_on_zero: {lock_positions_on_zero.sum()}")
print(f"number_of_lock_crossing_zero: {(np.abs((lock_positions + np.roll(lock_movements, -1))) // 100).astype(int).sum()}")
print(f"Total: {lock_positions_on_zero.sum() + np.abs(np.diff((lock_positions + np.roll(lock_movements, -1) ) // 100)).astype(int).sum()}")