import io

fresh_ingredients_ranges = []
finished_to_read_ranges = False
ingredients = []
with io.open("day_5/input.txt", "r") as file:
    for line in file:
        line_stripped = line.strip()
        if line_stripped == "":
            finished_to_read_ranges = True
            continue
        if not finished_to_read_ranges:
            digits_range_data = {
                "start": int(line_stripped.split("-")[0]),
                "end": int(line_stripped.split("-")[1])
            }
            fresh_ingredients_ranges.append(digits_range_data)
        else:
            ingredient = int(line_stripped)
            ingredients.append(ingredient)

def merge_ranges(ranges: list[dict]) -> list[dict]:
    sorted_ranges = sorted(ranges, key=lambda x: x["start"])

    merged_ranges = [sorted_ranges[0].copy()]

    for current_range in sorted_ranges[1:]:
        last_merged_range = merged_ranges[-1]
        if current_range["start"] <= last_merged_range["end"]:
            last_merged_range["end"] = max(last_merged_range["end"], current_range["end"])
        else:
            merged_ranges.append(current_range.copy())

    return merged_ranges

print(merge_ranges(fresh_ingredients_ranges))

total_number_of_ingredients = 0
for range in merge_ranges(fresh_ingredients_ranges):
    number_of_ingredients_in_range = range["end"] - range["start"] + 1
    print(f"Number of ingredients in range {range}: {number_of_ingredients_in_range}")
    total_number_of_ingredients += number_of_ingredients_in_range

print(f"Total number of ingredients: {total_number_of_ingredients}")
