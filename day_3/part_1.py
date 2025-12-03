import io
import numpy as np

data = []
with io.open("day_3/simple_input.txt", "r") as file:
    for line in file:
        # Turn line to list
        line_list = list(line.strip())
        # Turn list to int
        line_int = np.array([int(x) for x in line_list])
        data.append(line_int)

# print(data)

battery_joltages = []
for row in data:
    tens_digit = unit_digit = 0
    maximum_index = np.argmax(row)
    print(f"Maximum index: {maximum_index}")
    tens_digit = row[maximum_index]
    print(f"First value: {tens_digit}")

    if maximum_index == len(row) - 1:
        new_row = row[:maximum_index]
    else:
        new_row = row[maximum_index + 1:]
    print(f"New row: {new_row}")

    second_maximum_index = np.argmax(new_row)
    print(f"Second maximum index: {second_maximum_index}")

    unit_digit = new_row[second_maximum_index]
    print(f"Second value: {unit_digit}")

    second_value_original_index_list = np.argwhere(row == unit_digit)
    print(f"Second value original index list: {second_value_original_index_list}")
    
    for index in second_value_original_index_list:
        if index > maximum_index:
            second_value_original_index = index[0]
            break
    else:
        second_value_original_index = second_value_original_index_list[0][0]

    print(f"Second value original index: {second_value_original_index}")

    if maximum_index < second_value_original_index:
        battery_joltage = int(str(tens_digit) + str(unit_digit))
    else:
        battery_joltage = int(str(unit_digit) + str(tens_digit))

    # battery_joltage = int(str(tens_digit) + str(unit_digit))

    battery_joltages.append(battery_joltage)

print(f"Battery joltage: {battery_joltages}")
print(f"Battery joltage sum: {sum(battery_joltages)}")