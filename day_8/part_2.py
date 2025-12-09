import io
from typing import List, Set, Tuple

data = []
with io.open("day_8/input.txt", "r") as file:
    for line in file:
        numbers = line.strip().split(',')
        data.append(tuple([int(x) for x in numbers]))

print(data)
print("\n")

def euclidean_distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

# Compute all pairwise distances for all junkboxes
pairwise_distances: List[Tuple[Tuple[int, int, int], Tuple[int, int, int], float]] = []
for junkbox in data:
    for other_junkbox in data:
        if junkbox == other_junkbox:
            continue
        distance = euclidean_distance(junkbox[0], junkbox[1], junkbox[2], other_junkbox[0], other_junkbox[1], other_junkbox[2])
        pairwise_distances.append((junkbox, other_junkbox, distance))
# Sort pairwise distances by distance
pairwise_distances.sort(key=lambda x: x[2])

NUMBER_OF_SHORTEST_CONNECTIONS = 1000
PAIRWISE_EFFECT = 2
print("Pairwise distances: ", pairwise_distances[:NUMBER_OF_SHORTEST_CONNECTIONS*PAIRWISE_EFFECT])

# Init circuits
circuits: List[Set[Tuple[int, int, int]]] = []
for junkbox in data:
    circuits.append(set([junkbox]))

def get_circuits_index_containing_junkboxes(junkbox):
    for circuit_index, circuit in enumerate(circuits):
        if junkbox in circuit:
            return circuit_index
    return None

while len(circuits) > 2:
    for i in range(0, len(pairwise_distances), PAIRWISE_EFFECT):
        print(pairwise_distances[i])
        # Merge circuits of pairwise_distance[0] and pairwise_distance[1]
        circuit_containing_first_junkbox = get_circuits_index_containing_junkboxes(pairwise_distances[i][0])
        circuit_containing_second_junkbox = get_circuits_index_containing_junkboxes(pairwise_distances[i][1])
        if circuit_containing_first_junkbox is not None and circuit_containing_second_junkbox is not None and circuit_containing_first_junkbox != circuit_containing_second_junkbox:
            circuits[circuit_containing_first_junkbox].update(circuits[circuit_containing_second_junkbox])
            circuits.pop(circuit_containing_second_junkbox)
        if len(circuits) == 2:
            print("Found two circuits, stopping")
            break

first_circuit = circuits[0]
second_circuit = circuits[1]

minimum_distance = float('inf')
minimum_distance_junkboxes = None
for junkbox in first_circuit:
    for other_junkbox in second_circuit:
        distance = euclidean_distance(junkbox[0], junkbox[1], junkbox[2], other_junkbox[0], other_junkbox[1], other_junkbox[2])
        if distance < minimum_distance:
            minimum_distance = distance
            minimum_distance_junkboxes = (junkbox, other_junkbox)
print("Minimum distance: ", minimum_distance)
print("Minimum distance junkboxes: ", minimum_distance_junkboxes)

print("Answer: ", minimum_distance_junkboxes[0][0] * minimum_distance_junkboxes[1][0])