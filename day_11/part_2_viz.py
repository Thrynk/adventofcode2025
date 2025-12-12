import io
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

data = {}
with io.open("day_11/input.txt", "r") as file:
    for line in file:
        parent = line.split(":")[0].strip()
        children = line.split(":")[1].strip().split(" ")
        data[parent] = children

print(data)

STARTING_NODE = "svr"
ENDING_NODE = "out"

print(STARTING_NODE)

# Define graph using NetworkX
graph = nx.DiGraph()
for parent, children in data.items():
    for child in children:
        graph.add_edge(parent, child)

# Set up the visualization
plt.figure(figsize=(16, 12))

# Use a hierarchical layout for directed graphs
pos = nx.spring_layout(graph, k=3, iterations=100)

# Draw nodes
nx.draw_networkx_nodes(graph, pos, node_color='lightblue', 
                       node_size=10, alpha=0.9)

# Draw edges
nx.draw_networkx_edges(graph, pos, edge_color='gray', 
                       arrows=True, arrowsize=20, alpha=0.6,
                       connectionstyle='arc3,rad=0.1')

# Draw labels
nx.draw_networkx_labels(graph, pos, font_size=8, font_weight='bold')

if STARTING_NODE in graph:
    nx.draw_networkx_nodes(graph, pos, nodelist=[STARTING_NODE], 
                          node_color='green', node_size=1500, alpha=0.8)
if ENDING_NODE in graph:
    nx.draw_networkx_nodes(graph, pos, nodelist=[ENDING_NODE], 
                          node_color='red', node_size=1500, alpha=0.8)

TARGET_NODES = ["fft", "dac"]
for target_node in TARGET_NODES:
    if target_node in graph:
        nx.draw_networkx_nodes(graph, pos, nodelist=[target_node], 
                              node_color='yellow', node_size=500, alpha=0.8)

plt.title("Graph Visualization", size=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

# Print some graph statistics
print(f"\nGraph Statistics:")
print(f"Number of nodes: {graph.number_of_nodes()}")
print(f"Number of edges: {graph.number_of_edges()}")
print(f"Starting node: {STARTING_NODE}")
print(f"Ending node: {ENDING_NODE}")
