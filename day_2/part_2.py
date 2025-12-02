import io

data = []
with io.open("day_2/input.txt", "r") as file:
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
    start_value = range_data["start"]
    end_value = range_data["end"]
    number_of_digits_to_repeat = number_of_digits_that_should_repeat(start_value)
    for number_of_repetitions in range(2, len(str(start_value)) + 1):
        print(f"Number of repetitions: {number_of_repetitions}")
        number_of_digits_to_repeat = len(str(start_value)) // number_of_repetitions
        print(f"Number of digits to repeat: {number_of_digits_to_repeat}")
        first_digits_of_start_value = str(start_value)[:number_of_digits_to_repeat]
        print(f"First digits of start value: {first_digits_of_start_value}")
        first_digits_of_end_value = str(end_value)[:number_of_digits_to_repeat]
        print(f"First digits of end value: {first_digits_of_end_value}")
        values_to_check.extend(generate_potential_candidates(int(first_digits_of_start_value), int(first_digits_of_end_value), number_of_repetitions))

    # first_digits_of_start_value = str(start_value)[:number_of_digits_that_should_repeat(start_value)]
    # first_digits_of_end_value = str(end_value)[:number_of_digits_that_should_repeat(end_value)]

    # values_to_check.extend(generate_potential_candidates(int(first_digits_of_start_value), int(first_digits_of_end_value)))

    return values_to_check

def generate_potential_candidate_from_subinterval(interval_value: int) -> list[int]:
    values_to_check = []
    number_of_digits_to_repeat = number_of_digits_that_should_repeat(interval_value)
    print(f"Number of digits to repeat: {number_of_digits_to_repeat}")
    first_digits_of_number = str(interval_value)[:number_of_digits_to_repeat]
    print(f"First digits of number: {first_digits_of_number}")

    start_of_subinterval = 10 ** (len(first_digits_of_number) - 1)
    print(f"Start of subinterval: {start_of_subinterval}")
    end_of_subinterval = 10 ** (len(first_digits_of_number))
    print(f"End of subinterval: {end_of_subinterval}")

    max_digits_to_repeat = maximum_number_of_digits_that_should_repeat(start_of_subinterval)
    print(f"number of digits to repeat {list(range(2, len(str(interval_value)) + 1))}")
    for number_of_repetitions in range(2, len(str(interval_value)) + 1):
        print(f"Number of repetitions: {number_of_repetitions}")
        start_of_subinterval = 10 ** (len(first_digits_of_number) - 1)
        end_of_subinterval = 10 ** (len(first_digits_of_number)) - 1
        number_of_digits_to_repeat = len(str(interval_value)) // number_of_repetitions
        print(f"Number of digits to repeat: {number_of_digits_to_repeat}")
        first_digits_of_start_number = str(start_of_subinterval)[:number_of_digits_to_repeat]
        print(f"First digits of start number: {first_digits_of_start_number}")
        first_digits_of_end_number = str(end_of_subinterval)[:number_of_digits_to_repeat]
        print(f"First digits of end number: {first_digits_of_end_number}")
        values_to_check.extend(generate_potential_candidates(int(first_digits_of_start_number), int(first_digits_of_end_number), number_of_repetitions))

    return values_to_check

def generate_potential_candidates(start_value: int, end_value: int, number_of_digits_to_repeat: int) -> list[int]:
    values_to_check = []
    print(f"Generating potential candidates for {start_value} to {end_value}")
    for number in range(start_value, end_value + 1):
            number_to_check = int(str(number) * number_of_digits_to_repeat)
            print(f"Number to check: {number_to_check}")
            values_to_check.append(number_to_check)
    return values_to_check

def number_of_digits_that_should_repeat(interval_value: int):
    if len(str(interval_value)) == 1:
        return 1
    return len(str(interval_value)) // 2

def maximum_number_of_digits_that_should_repeat(interval_value: int) -> int:
    if len(str(interval_value)) == 1:
        return 1
    return len(str(interval_value)) // 2

count = 0
invalid_numbers = []
# data = [{
#         "start": 969,
#         "end": 1469
#     }]
for range_data in data:
    values_to_check = []

    start_has_odd_number_of_digits = has_odd_number_of_digits_for_part(range_data["start"])
    end_has_odd_number_of_digits = has_odd_number_of_digits_for_part(range_data["end"])
    start_and_end_have_the_same_number_of_digits = does_start_and_end_have_the_same_number_of_digits(range_data)

    # if not (start_and_end_have_the_same_number_of_digits and start_has_odd_number_of_digits and end_has_odd_number_of_digits):
    print(f"Range {range_data} to try")
    if start_and_end_have_the_same_number_of_digits:
        print(f"Try together, starting from {range_data['start']} and ending at {range_data['end']}")
        values_to_check.extend(generate_potential_candidates_from_full_interval(range_data))
    else:
        # if not start_has_odd_number_of_digits:
        print(f"Try interval {range_data['start']}")
        values_to_check.extend(generate_potential_candidate_from_subinterval(range_data['start']))
        # if not end_has_odd_number_of_digits:
        print(f"Try interval {range_data['end']}")
        values_to_check.extend(generate_potential_candidate_from_subinterval(range_data['end']))

    print(f"Range {range_data} values to check: {values_to_check}")

    for value in values_to_check:
        if value >= range_data["start"] and value <= range_data["end"]:
            invalid_numbers.append(value)
            count += 1

print(f"Count: {count}")
print(f"Invalid numbers: {invalid_numbers}")
unique_invalid_numbers = sorted(list(set(invalid_numbers)))
print(f"Unique invalid numbers: {unique_invalid_numbers}")
print(f"Unique invalid numbers length: {len(unique_invalid_numbers)}")
print(f"Unique invalid numbers sum: {sum(unique_invalid_numbers)}")
