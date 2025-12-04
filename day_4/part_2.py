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


print(data)
print(f"Data shape: {data.shape}")

MASK = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

MAX_NEIGHBOURS = 4

def get_accessible_rolls(data):
    convoluted_array = ndimage.convolve(data, MASK, mode='constant', cval=0)
    convoluted_array_masked_with_rolls = convoluted_array * data
    temp_1d_array = convoluted_array_masked_with_rolls.reshape(-1,)
    blocked_rolls = (temp_1d_array >= MAX_NEIGHBOURS).reshape(data.shape)

    # Remove the blocked rolls from the data
    accessible_rolls = data * (1 - blocked_rolls)
    return accessible_rolls

def remove_rolls(data, rolls):
    return data * (1 - rolls)

number_of_rolls = data.sum()

print(f"Number of rolls: {number_of_rolls}")

print(f"First round accessible rolls: {get_accessible_rolls(data).sum()}")

removable_rolls = get_accessible_rolls(data)
while removable_rolls.sum() > 0:
    data = remove_rolls(data, removable_rolls)
    removable_rolls = get_accessible_rolls(data)

remaining_rolls = data.sum()
print(f"Remaining rolls: {remaining_rolls}")

print(f"Result: {number_of_rolls - remaining_rolls}")