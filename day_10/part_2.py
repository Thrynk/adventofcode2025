import io
import numpy as np
from ortools.linear_solver import pywraplp

data = []
with io.open("day_10/input.txt", "r") as file:
    for line in file:
        # Parse target state
        target_state = line.split("[")[1].split("]")[0]
        parsed_target_state = []
        for char in target_state:
            if char == "#":
                parsed_target_state.append(1)
            else:
                parsed_target_state.append(0)

        buttons_part = line.split("]")[1].split("{")[0].strip()
        parsed_buttons = []
        for button in buttons_part.split(" "):
            parsed_buttons.append(tuple([int(x) for x in button[1:-1].split(",")]))

        joltages_part = line.split("{")[1].split("}")[0].strip()
        parsed_joltages = []
        for joltage in joltages_part.split(","):
            parsed_joltages.append(int(joltage))

        data.append({
            "target_state": parsed_target_state,
            "buttons": parsed_buttons,
            "joltages": parsed_joltages,
        })

def vector_encode(button, vector_size):
    """Encodes a button as a vector."""
    vector = np.zeros(vector_size)
    for position in list(button):
        vector[position] = 1
    return vector

solver: pywraplp.Solver = pywraplp.Solver.CreateSolver('SCIP')

total_presses = 0
for entry in data:
    vector_encoded_buttons = []
    for button in entry["buttons"]:
        vector_encoded_button = vector_encode(button, len(entry["target_state"]))
        vector_encoded_buttons.append(vector_encoded_button)

    # For each button, create a variable for the number of clicks of that button
    button_variables = []
    for i, button in enumerate(entry["buttons"]):
        button_variables.append(solver.IntVar(0, solver.infinity(), f"button_{i}"))

    # For each position of the statem add ortools constraints that joltage = sum of all vector_encoded_buttons[position]
    for position in range(len(entry["joltages"])):
        constraint = solver.Add(sum([button_variables[i] * vector_encoded_buttons[i][position] for i in range(len(button_variables))]) == entry["joltages"][position])

    # Set objective to minimize the sum of the button variables
    solver.Minimize(sum(button_variables))

    # Solve the problem
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Solution: {solver.Objective().Value()}")
        total_presses += solver.Objective().Value()
    else:
        print("No solution found")

print(f"Total presses: {total_presses}")