import io
import networkx as nx

data = {}
with io.open("day_11/input.txt", "r") as file:
    for line in file:
        parent = line.split(":")[0].strip()
        children = line.split(":")[1].strip().split(" ")
        data[parent] = children

# print(data)

STARTING_NODE = "svr"
ENDING_NODE = "fft"

print(STARTING_NODE)
print(ENDING_NODE)

# Define graph using NetworkX
graph = nx.DiGraph()
for parent, children in data.items():
    for child in children:
        graph.add_edge(parent, child)

paths = nx.all_simple_paths(graph, STARTING_NODE, ENDING_NODE, cutoff=12)
print(len(list(paths)))

# Calculate paths until choke points, then add or multiply the number of paths
# Choke points are visually identifiable on the graph.
# A cutoff of 12 has been chosen to speed up the process and allow for limited search after some choke points.
# I tried to increase it for svr->fft to check that we were not missing any paths. Seemed to be enough.
# Example: dac to out
# dac -> you -> out = 3*448
# dac -> daz -> out = 1*480
# dac -> ngs -> out = 3*505
# dac -> tml -> out = 4*835
# dac -> out = 3*448 + 1*480 + 3*505 + 4*835 = 6679

# Let's continue:
# fft to dac = fft->gxv->dac + fft->fhz->dac + fft->qzp->dac
# (Each of those were decomposed using the same method with nodes mdm, sdo, cjm, jmk and xhu).
# fft->gxv->dac = 9*(39*1916+59*899+40*1625+42*1037+51*1271) = 2_710_260
# fft->fhz->dac = 6*(33*1916+31*899+31*1625+38*1037+41*1271) = 1_397_934
# fft->qzp->dac = 7*(63*1916+84*899+59*1625+79*1037+88*1271) = 3_401_090

# svr->fft = 11_030
# svr->fft->dac = 11_030 * (2_710_260 + 1_397_934 + 3_401_090) = 82_827_402_520

# svr -> fft -> dac -> out = 82_827_402_520 * 6679 = 553_204_221_431_080
# Answer: 553204221431080