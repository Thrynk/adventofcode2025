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

print(fresh_ingredients_ranges)
print(ingredients)

number_of_fresh_ingredients = 0
for ingredient in ingredients:
    for fresh_ingredient_range in fresh_ingredients_ranges:
        if ingredient >= fresh_ingredient_range["start"] and ingredient <= fresh_ingredient_range["end"]:
            print(f"Ingredient {ingredient} is in range {fresh_ingredient_range}")
            number_of_fresh_ingredients += 1
            break
    else:
        print(f"Ingredient {ingredient} is not in any range")

print(f"Number of fresh ingredients: {number_of_fresh_ingredients}")