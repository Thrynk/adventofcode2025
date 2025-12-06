import io
import re
import numpy as np

data = []
with io.open("day_6/input.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()
        numbers = re.findall(r'\d+', stripped_line)
        print(len(numbers))
        
        if len(numbers) == 0:
            operations = re.findall(r'[+\-*/]', stripped_line)
        else:
            numbers = [int(number) for number in numbers]
            data.append(numbers)
print(data, operations)

transposed_data = np.array(data).T

total_sum = 0
for index, row in enumerate(transposed_data):
    if operations[index] == '+':
        print(row.sum())
        total_sum += row.sum()
    elif operations[index] == '*':
        print(row.prod())
        total_sum += row.prod()

print(f"Total sum: {total_sum}")