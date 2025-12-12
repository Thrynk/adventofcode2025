import numpy as np
from typing import List, Tuple
import io
import re

Shape = List[str]

Region = Tuple[int, int, List[Tuple[int, int]]]

shapes = []
regions = []
with io.open("day_12/input.txt", "r") as file:
    for line in file:
        # If line starts with an index integer followed by :, following lines are the shape until the next index integer
        print(line)
        is_line_starting_with_index = re.match(r'\d+:', line)
        if is_line_starting_with_index:
            index = int(line.split(':')[0])
            shape = []
            for shape_line in file:
                if re.match(r'^\n$', shape_line):
                    break
                shape.append(shape_line.strip())
            shapes.append(shape)

        is_line_starting_with_region = re.match(r'\d+x\d+:', line)
        if is_line_starting_with_region:
            region = line.split(':')[0]
            region_size = region.split('x')
            region_width = int(region_size[0])
            region_height = int(region_size[1])
            region_presents = line.split(':')[1].strip().split(' ')
            region_presents = [(index, int(count)) for index, count in enumerate(region_presents) if count != '0']

            regions.append((region_width, region_height, region_presents))

print(shapes)
print(regions)

def get_shape_area(shape: Shape) -> int:
    return sum(shape_row.count('#') for shape_row in shape)

def get_total_area_for_shapes(shapes: List[Shape], counts: List[int]) -> int:
    return sum(get_shape_area(shape) * count for shape, count in zip(shapes, counts))

def get_region_area(width: int, height: int) -> int:
    return width * height

# The input is easier than the example given in simple_input.txt, so we can just check if the shapes area is greater than the region area
def solve():
    valid_count = 0
    for region_index, region in enumerate(regions[2:]):
        print(f"Region index: {region_index}")
        width, height, presents = region
        grid = [['.' for _ in range(width)] for _ in range(height)]
        shapes_area = get_total_area_for_shapes([shapes[shape_idx] for shape_idx, _ in presents], [count for _, count in presents])
        region_area = get_region_area(width, height)
        print(f"Shapes area: {shapes_area}, Region area: {region_area}")
        if shapes_area > region_area:
            print(f"Region {region_index} is too small to fit the shapes")
            continue
        else:
            valid_count += 1
    return valid_count

print(solve())