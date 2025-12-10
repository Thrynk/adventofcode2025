import io
from typing import List, Set, Tuple

data = []
with io.open("day_9/input.txt", "r") as file:
    for line in file:
        coordinates = line.strip().split(',')
        data.append(tuple(int(x) for x in coordinates))

print(data)

def calculate_rectangle_area(coordinates: List[Tuple[int, int]]) -> int:
    x_coordinates = [coordinate[0] for coordinate in coordinates]
    y_coordinates = [coordinate[1] for coordinate in coordinates]
    return (max(x_coordinates) - min(x_coordinates) + 1) * (max(y_coordinates) - min(y_coordinates) + 1)

print("Rectangle area Test: ")
print(calculate_rectangle_area(data[:2]))

max_rectangle_area = 0
max_rectangle_area_tiles = None
number_of_rectangles_tried = 0
for red_tile in data:
    for other_tile in data:
        if red_tile == other_tile:
            continue
        rectangle_area = calculate_rectangle_area([red_tile, other_tile])
        if rectangle_area > max_rectangle_area:
            max_rectangle_area = rectangle_area
            max_rectangle_area_tiles = [red_tile, other_tile]
        number_of_rectangles_tried += 1
        print(f"Number of rectangles tried: {number_of_rectangles_tried}")
print(f"Max rectangle area: {max_rectangle_area}")
print(f"Max rectangle area tiles: {max_rectangle_area_tiles}")