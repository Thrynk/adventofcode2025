import io
from typing import List, Set, Tuple
import numpy as np
from enum import Enum

data = []
with io.open("day_9/simple_input.txt", "r") as file:
    for line in file:
        coordinates = line.strip().split(',')
        data.append(tuple(int(x) for x in coordinates))

print(data)

def calculate_rectangle_area(coordinates: List[Tuple[int, int]]) -> int:
    x_coordinates = [coordinate[0] for coordinate in coordinates]
    y_coordinates = [coordinate[1] for coordinate in coordinates]
    return (max(x_coordinates) - min(x_coordinates) + 1) * (max(y_coordinates) - min(y_coordinates) + 1)

X_INDEX = 1
Y_INDEX = 0

print("Rectangle area Test: ")
print(calculate_rectangle_area(data[:2]))

max_x_coordinate = max(data, key=lambda x: x[X_INDEX])[X_INDEX]
max_y_coordinate = max(data, key=lambda x: x[Y_INDEX])[Y_INDEX]
min_x_coordinate = min(data, key=lambda x: x[X_INDEX])[X_INDEX]
min_y_coordinate = min(data, key=lambda x: x[Y_INDEX])[Y_INDEX]

print(f"Max x coordinate: {max_x_coordinate}")
print(f"Max y coordinate: {max_y_coordinate}")
print(f"Min x coordinate: {min_x_coordinate}")
print(f"Min y coordinate: {min_y_coordinate}")

class TileColor(Enum):
    OTHER = 0
    RED = 1
    GREEN = 2

PADDING = 2
area_width = max_x_coordinate + PADDING
area_height = max_y_coordinate + PADDING

area = np.zeros((area_width, area_height))
for tile in data:
    area[tile[X_INDEX], tile[Y_INDEX]] = TileColor.RED.value
print(area)

def fill_in_between_tiles(
    area: np.array,
    area_width: int,
    area_height: int,
    tile_colors_to_check: List[TileColor],
    fill_color: TileColor
) -> np.array:
    tile_colors_to_check_values = [color.value for color in tile_colors_to_check]
    # Fill in the green tiles for rows
    for row_index in range(area_width):
        last_red_tile_index = None
        for col_index in range(area_height):
            if area[row_index, col_index] in tile_colors_to_check_values:
                if last_red_tile_index is not None:
                    area[row_index, last_red_tile_index[1]+1:col_index] = fill_color.value
                last_red_tile_index = (row_index, col_index)
            
    # Fill in the green tiles for columns
    for col_index in range(area_height):
        last_red_tile_index = None
        for row_index in range(area_width):
            if area[row_index, col_index] in tile_colors_to_check_values:
                if last_red_tile_index is not None:
                    area[last_red_tile_index[0]+1:row_index, col_index] = fill_color.value
                last_red_tile_index = (row_index, col_index)
    return area

area = fill_in_between_tiles(area, area_width, area_height, [TileColor.RED], TileColor.GREEN)
print("After filling in between red tiles with green: ")
# print(area)

area = fill_in_between_tiles(area, area_width, area_height, [TileColor.GREEN, TileColor.RED], TileColor.GREEN)
print("After filling in between tiles with green: ")
# print(area)

def validate_rectangle_filled_with_correct_tiles(rectangle_tiles: List[Tuple[int, int]], tile_colors_to_check: List[TileColor]) -> bool:
    tile_colors_to_check_values = [color.value for color in tile_colors_to_check]
    x_coordinates = [tile[X_INDEX] for tile in rectangle_tiles]
    y_coordinates = [tile[Y_INDEX] for tile in rectangle_tiles]
    for row_index in range(min(x_coordinates), max(x_coordinates) + 1):
        for col_index in range(min(y_coordinates), max(y_coordinates) + 1):
            if area[row_index, col_index] not in tile_colors_to_check_values:
                print(f"Tile {row_index, col_index} is not in {tile_colors_to_check_values}")
                return False
    return True

max_rectangle_area = 0
max_rectangle_area_tiles = None
for red_tile in data:
    for other_tile in data:
        if red_tile == other_tile:
            continue
        rectangle_area = calculate_rectangle_area([red_tile, other_tile])
        print(f"Validating rectangle {red_tile, other_tile} with area {rectangle_area}")
        print(validate_rectangle_filled_with_correct_tiles([red_tile, other_tile], [TileColor.GREEN, TileColor.RED]))
        if rectangle_area > max_rectangle_area and validate_rectangle_filled_with_correct_tiles([red_tile, other_tile], [TileColor.GREEN, TileColor.RED]):
            max_rectangle_area = rectangle_area
            max_rectangle_area_tiles = [red_tile, other_tile]
print(f"Max rectangle area: {max_rectangle_area}")
print(f"Max rectangle area tiles: {max_rectangle_area_tiles}")