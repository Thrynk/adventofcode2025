import io
from typing import List, Set, Tuple
import numpy as np
from enum import Enum

from shapely.geometry import Point, Polygon

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

def do_lines_intersect(line_1: Tuple[Tuple[int, int], Tuple[int, int]], line_2: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[bool, Tuple[int, int]]:
    """
    Check if two line segments intersect using the parametric line equation method.
    Returns True if the segments intersect (including endpoints), False otherwise.
    """
    (x1, y1), (x2, y2) = line_1
    (x3, y3), (x4, y4) = line_2
    
    # Calculate direction vectors
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3
    
    # Calculate denominator
    denominator = dx1 * dy2 - dy1 * dx2
    
    # Lines are parallel
    if denominator == 0:
        # They're collinear and overlapping
        return {
            "intersection": False,
            "intersection_point": None
        }
    
    # Calculate parameters t and u
    t = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / denominator
    u = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / denominator

    # Calculate intersection point
    intersection_x = x1 + t * dx1
    intersection_y = y1 + t * dy1
    
    # Check if intersection point is within both segments
    return {
        "intersection": 0 <= t <= 1 and 0 <= u <= 1 and t != u,
        "intersection_point": (int(intersection_x), int(intersection_y))
    }

def point_in_polygon(point: Tuple[int, int], polygon: List[Tuple[int, int]]) -> bool:
    """
    Check if a point is inside a polygon using shapely library.
    Returns True if point is inside, False otherwise.
    """
    # Create shapely Point
    p = Point(point[X_INDEX], point[Y_INDEX])
    
    # Create shapely Polygon (note: shapely expects (x, y) format)
    # Convert polygon vertices to shapely format
    poly_coords = [(vertex[X_INDEX], vertex[Y_INDEX]) for vertex in polygon]
    poly = Polygon(poly_coords)
    
    # Check if point is inside polygon (touching boundary is considered inside)
    return poly.contains(p) or poly.touches(p)


def get_rectangle_corners(rectangle_tiles: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Get all corners of a rectangle from its opposite corners.
    """

    x_coordinates = [tile[X_INDEX] for tile in rectangle_tiles]
    y_coordinates = [tile[Y_INDEX] for tile in rectangle_tiles]

    # Calculate corners
    top_left_x = min(x_coordinates)
    top_left_y = min(y_coordinates)
    bottom_right_x = max(x_coordinates)
    bottom_right_y = max(y_coordinates)
    width = max(x_coordinates) - min(x_coordinates) + 1
    height = max(y_coordinates) - min(y_coordinates) + 1
    top_right_x = top_left_x
    top_right_y = top_left_y + height - 1
    bottom_left_x = top_left_x + width - 1
    bottom_left_y = top_left_y
    
    # Return the four edges
    return [
        (bottom_left_y, bottom_left_x),  # bottom edge
        (bottom_right_y, bottom_right_x),    # right edge
        (top_right_y, top_right_x),        # top edge
        (top_left_y, top_left_x)       # left edge
    ]

def get_rectangle_edges(rectangle_corners: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Get all edges of a rectangle from its corner points.
    """
    edges = []
    for corner in rectangle_corners:
        for other_corner in rectangle_corners:
            if corner == other_corner:
                continue
            edges.append((corner, other_corner))
    return edges


def polygon_edges(polygon: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Get all edges of a polygon from its vertices.
    """
    edges = []
    n = len(polygon)
    for i in range(n):
        edges.append((polygon[i], polygon[(i + 1) % n]))
    return edges


def is_rectangle_contained_in_polygon(rect_corners: List[Tuple[int, int]], polygon: List[Tuple[int, int]]) -> bool:
    """
    Check if a rectangle is completely contained inside a polygon.
    A rectangle is contained if:
    1. All corners of the rectangle are inside the polygon
    2. No edge of the rectangle intersects with any edge of the polygon
    """
    rectangle_corners = get_rectangle_corners(rect_corners)
    # All rectangle corners must be inside the polygon
    for corner in rectangle_corners:
        if not point_in_polygon(corner, polygon):
            return False
    
    # No rectangle edge should intersect with any polygon edge
    rect_edges = get_rectangle_edges(rect_corners)
    poly_edges = polygon_edges(polygon)
    
    for rect_edge in rect_edges:
        for poly_edge in poly_edges:
            intersection_result = do_lines_intersect(rect_edge, poly_edge)
            intersection = intersection_result["intersection"]
            intersection_point = intersection_result["intersection_point"]
            if intersection:
                (r1, r2) = rect_edge
                (p1, p2) = poly_edge
                
                # Check if intersection is at endpoints only
                if (r1 == p1 or r1 == p2 or r2 == p1 or r2 == p2) or intersection_point in polygon:
                    # Endpoint intersection is OK if the rectangle corner is on polygon point or the intersection point is in the polygon
                    continue
                else:
                    # Actual crossing intersection means rectangle is not contained
                    return False
    
    return True

# Example usage:
polygon = data  # Your polygon vertices

# Test with a rectangle
test_rect = [(9, 5), (2, 3)]  # Your test rectangle corners

if is_rectangle_contained_in_polygon(test_rect, polygon):
    print("Rectangle is contained in polygon!")
else:
    print("Rectangle is NOT contained in polygon")


max_rectangle_area = 0
max_rectangle_area_tiles = None
number_of_rectangles_tried = 0
for red_tile in data:
    for other_tile in data:
        if red_tile == other_tile:
            continue
        rectangle_area = calculate_rectangle_area([red_tile, other_tile])
        if rectangle_area > max_rectangle_area and is_rectangle_contained_in_polygon([red_tile, other_tile], polygon):
            max_rectangle_area = rectangle_area
            max_rectangle_area_tiles = [red_tile, other_tile]
        number_of_rectangles_tried += 1
        print(f"Number of rectangles tried: {number_of_rectangles_tried}")
print(f"Max rectangle area: {max_rectangle_area}")
print(f"Max rectangle area tiles: {max_rectangle_area_tiles}")