import io

data = []
with io.open("day_2/simple_input.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for digits_range in ranges:
            digits_range_data = {
                "start": int(digits_range.split("-")[0]),
                "end": int(digits_range.split("-")[1])
            }
            data.append(digits_range_data)

def does_start_and_end_have_the_same_number_of_digits(range_data) -> bool:
    return len(str(range_data["start"])) == len(str(range_data["end"]))

def has_odd_number_of_digits_for_part(number: int) -> bool:
    return len(str(number)) % 2 == 1

def generate_potential_candidates_from_full_interval(range_data: dict) -> list[int]:
    values_to_check = []
    start_value = range_data["start"]
    end_value = range_data["end"]
    first_digits_of_start_value = str(start_value)[:number_of_digits_that_should_repeat(start_value)]
    first_digits_of_end_value = str(end_value)[:number_of_digits_that_should_repeat(end_value)]
    for number in range(int(first_digits_of_start_value), int(first_digits_of_end_value) + 1):
        number_to_check = int(str(number) + str(number))
        values_to_check.append(number_to_check)

    return values_to_check

def generate_potential_candidate_from_subinterval(interval_value: int) -> list[int]:
    values_to_check = []
    number_of_digits_to_repeat = number_of_digits_that_should_repeat(interval_value)
    first_digits_of_number = str(interval_value)[:number_of_digits_to_repeat]

    start_of_subinterval = 10 ** (len(first_digits_of_number) - 1)
    end_of_subinterval = 10 ** (len(first_digits_of_number))
    for number in range(start_of_subinterval, end_of_subinterval):
        number_to_check = int(str(number) + str(number))
        values_to_check.append(number_to_check)
    
    return values_to_check

def number_of_digits_that_should_repeat(interval_value: int):
    if len(str(interval_value)) == 1:
        return 1
    return len(str(interval_value)) // 2

count = 0
invalid_numbers = []
# data = [{
#         "start": 969,
#         "end": 1469
#     }]
for range_data in data[:3]:
    values_to_check = []

    start_has_odd_number_of_digits = has_odd_number_of_digits_for_part(range_data["start"])
    end_has_odd_number_of_digits = has_odd_number_of_digits_for_part(range_data["end"])
    start_and_end_have_the_same_number_of_digits = does_start_and_end_have_the_same_number_of_digits(range_data)

    if not (start_and_end_have_the_same_number_of_digits and start_has_odd_number_of_digits and end_has_odd_number_of_digits):
        print(f"Range {range_data} to try")
        if start_and_end_have_the_same_number_of_digits:
            print(f"Try together, starting from {range_data['start']} and ending at {range_data['end']}")
            values_to_check.extend(generate_potential_candidates_from_full_interval(range_data))
        else:
            if not start_has_odd_number_of_digits:
                print(f"Try interval {range_data['start']}")
                values_to_check.extend(generate_potential_candidate_from_subinterval(range_data['start']))
            if not end_has_odd_number_of_digits:
                print(f"Try interval {range_data['end']}")
                values_to_check.extend(generate_potential_candidate_from_subinterval(range_data['end']))

    print(f"Range {range_data} values to check: {values_to_check}")

    for value in values_to_check:
        if value >= range_data["start"] and value <= range_data["end"]:
            invalid_numbers.append(value)
            count += 1

print(f"Count: {count}")
print(f"Invalid numbers: {invalid_numbers}")
print(f"Invalid numbers length: {len(invalid_numbers)}")
print(f"Invalid numbers set length: {len(set(invalid_numbers))}")
print(f"Invalid numbers sum: {sum(invalid_numbers)}")
