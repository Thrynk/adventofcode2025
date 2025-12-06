import io
import re

# Read all lines preserving exact character positions
lines = []
operations = []
with open("day_6/input.txt", "r") as file:
    for line in file:
        stripped = line.rstrip('\n')
        if stripped and not re.search(r'[+\-*/]', stripped):
            lines.append(stripped)
        elif re.search(r'[+\-*/]', stripped):
            # Parse operations, preserving their positions
            ops_line = stripped
            operations = []
            for char in ops_line:
                if char in ['+', '*', '-', '/']:
                    operations.append(char)

# Find maximum line length
max_len = max(len(line) for line in lines) if lines else 0

# Pad all lines to same length
padded_lines = [line.ljust(max_len) for line in lines]
num_rows = len(padded_lines)

# Process columns from right to left
total_sum = 0
col = max_len - 1
numbers_to_operate_on = []
while col >= 0:
    # Skip separator columns (all spaces)
    if all(padded_lines[row][col] == ' ' for row in range(num_rows)):
        col -= 1
        continue

    # Collect numbers for this problem
    operation_numbers = []
    
    # Read columns right-to-left until we hit a separator
    while col >= 0:
        # Check if this is a separator column
        if all(padded_lines[row][col] == ' ' for row in range(num_rows)):
            numbers_to_operate_on.append(operation_numbers)
            break
        
        # Read this column top-to-bottom to extract the digit
        column_chars = [padded_lines[row][col] for row in range(num_rows)]

        numbers = int(''.join(column_chars))
        operation_numbers.append(numbers)
        if col - 1 == 0:
            numbers_to_operate_on.append(operation_numbers)
        col -= 1

for index, numbers in enumerate(numbers_to_operate_on):
    op = list(reversed(operations))[index]
    if op == '+':
        result = sum(numbers)
    elif op == '*':
        result = 1
        for n in numbers:
            result *= n
    total_sum += result
print(f"Grand total: {total_sum}")