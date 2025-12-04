import io
import numpy as np
from scipy import ndimage

data = []
with io.open("day_4/input.txt", "r") as file:
    for line in file:
        # Turn line to list
        line_list = list(line.strip().replace('.', '0').replace('@', '1'))
        # Turn list to int
        line_int = np.array([int(x) for x in line_list])
        data.append(line_int)

data = np.array(data)

# data = data[0:20, 0:20]

print(data)
print(f"Data shape: {data.shape}")

MASK = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

convoluted_array = ndimage.convolve(data, MASK, mode='constant', cval=0)

print(f"Convoluted array: \n{convoluted_array}")

convoluted_array_masked_with_rolls = convoluted_array * data

print(f"Convoluted array masked with rollers: \n{convoluted_array_masked_with_rolls}")

MAX_NEIGHBOURS = 4

temp_1d_array = convoluted_array_masked_with_rolls.reshape(-1,)
print(f"Temp 1d array shape: {temp_1d_array.shape}")

blocked_rolls = (temp_1d_array >= MAX_NEIGHBOURS).sum()
print(f"Blocked rolls: {blocked_rolls}")
# print(f"Temp 1d array: {temp_1d_array.tolist()}")

# filtered_1d_array = temp_1d_array * (temp_1d_array < MAX_NEIGHBOURS)

# print(f"Filtered 1d array: {filtered_1d_array.tolist()}")

# print((filtered_1d_array > 0).sum())

number_of_rolls = data.sum()

print(f"Number of rolls: {number_of_rolls}")

print(f"Result: {number_of_rolls - blocked_rolls}")