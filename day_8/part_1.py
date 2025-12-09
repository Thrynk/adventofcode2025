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

for i in range(0, NUMBER_OF_SHORTEST_CONNECTIONS*PAIRWISE_EFFECT, PAIRWISE_EFFECT):
    print(pairwise_distances[i])
    # Merge circuits of pairwise_distance[0] and pairwise_distance[1]
    circuit_containing_first_junkbox = get_circuits_index_containing_junkboxes(pairwise_distances[i][0])
    circuit_containing_second_junkbox = get_circuits_index_containing_junkboxes(pairwise_distances[i][1])
    if circuit_containing_first_junkbox is not None and circuit_containing_second_junkbox is not None and circuit_containing_first_junkbox != circuit_containing_second_junkbox:
        circuits[circuit_containing_first_junkbox].update(circuits[circuit_containing_second_junkbox])
        circuits.pop(circuit_containing_second_junkbox)

# Sort circuits by size
circuits.sort(key=lambda x: len(x), reverse=True)
print("Circuits: ", circuits)

NUMBER_OF_LARGEST_CIRCUITS = 3
multiplication_of_n_largest_circuits = 1
for circuit in circuits[:NUMBER_OF_LARGEST_CIRCUITS]:
    multiplication_of_n_largest_circuits *= len(circuit)
print("Multiplication of n largest circuits: ", multiplication_of_n_largest_circuits)
