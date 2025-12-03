import io
import numpy as np

data = []
with io.open("day_3/input.txt", "r") as file:
    for line in file:
        # Turn line to list
        line_list = list(line.strip())
        # Turn list to int
        line_int = np.array([int(x) for x in line_list])
        data.append(line_int)

# print(data)

REQUIRED_BATTERY_SIZE = 12

battery_joltages = []
for row in data:
    battery_joltages_row = []
    discarded_digits = []
    max_iterations = 0
    while len(battery_joltages_row) < REQUIRED_BATTERY_SIZE and max_iterations < 50:
        max_iterations += 1
        if max_iterations > 50:
            print(f"Iteration limit reached")
            break
        row_size = len(row)
        print(f"Row size: {row_size}")
        maximum_index = np.argmax(row)
        print(f"Maximum index: {maximum_index}")
        maximum_digit = row[maximum_index]
        print(f"Maximum digit: {maximum_digit}")
        battery_joltages_row.append(maximum_digit)
        print(f"row[maximum_index + 1:]: {row[maximum_index + 1:]}")
        print(f"discarded_digits: {discarded_digits}")
        remaining_row = np.concatenate((row[maximum_index + 1:], np.array(discarded_digits, dtype=int)))
        print(f"Remaining row: {remaining_row}")
        print(f"len(remaining_row): {len(remaining_row)}", REQUIRED_BATTERY_SIZE, "-", len(battery_joltages_row), "=", REQUIRED_BATTERY_SIZE - len(battery_joltages_row))
        if len(remaining_row) < REQUIRED_BATTERY_SIZE - len(battery_joltages_row):
            print(f"Discarding maximum digit: {maximum_digit}")
            battery_joltages_row.pop()
            row = np.delete(row, maximum_index)
            discarded_digits.append(maximum_digit)
        else:
            print(f"Keeping maximum digit: {maximum_digit}")
            row = remaining_row

        print(f"Battery joltage row: {[int(x) for x in battery_joltages_row]}")



    # if maximum_index == len(row) - 1:
    #     new_row = row[:maximum_index]
    # else:
    #     new_row = row[maximum_index + 1:]
    # print(f"New row: {new_row}")

    # second_maximum_index = np.argmax(new_row)
    # print(f"Second maximum index: {second_maximum_index}")

    # unit_digit = new_row[second_maximum_index]
    # print(f"Second value: {unit_digit}")

    # second_value_original_index_list = np.argwhere(row == unit_digit)
    # print(f"Second value original index list: {second_value_original_index_list}")
    
    # for index in second_value_original_index_list:
    #     if index > maximum_index:
    #         second_value_original_index = index[0]
    #         break
    # else:
    #     second_value_original_index = second_value_original_index_list[0][0]

    # print(f"Second value original index: {second_value_original_index}")

    # if maximum_index < second_value_original_index:
    #     battery_joltage = int(str(tens_digit) + str(unit_digit))
    # else:
    #     battery_joltage = int(str(unit_digit) + str(tens_digit))

    # # battery_joltage = int(str(tens_digit) + str(unit_digit))

    battery_joltage = int("".join(map(str, battery_joltages_row)))
    print(f"Battery joltage: {battery_joltage}")

    battery_joltages.append(battery_joltage)

print(f"Battery joltages: {battery_joltages}")
print(f"Battery joltage sum: {sum(battery_joltages)}")