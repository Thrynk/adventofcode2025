import io
import numpy as np

data = []
with io.open("day_7/input.txt", "r") as file:
    for line in file:
        # Turn line to list
        line_list = list(line.strip())
        data.append(line_list)

beams = set()
beam_hits = 0
for row_index, row in enumerate(data):
    for col_index, char in enumerate(row):
        
        if char == 'S':
            start = col_index
            beams.add(start)
        if char == '^' and col_index in beams:
            beam_hits += 1
            beams.add(col_index-1)
            beams.add(col_index+1)
            beams.remove(col_index)

print(beams)

print(f"Beam hits: {beam_hits}")