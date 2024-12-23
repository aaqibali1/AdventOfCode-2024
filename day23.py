from collections import defaultdict
from itertools import combinations

# Read input file name
INPUT_FILE = "input.txt"

def read_input(file_name):
    """Reads the input file and parses the connections."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def build_graph(connections):
    """Builds a graph (adjacency list) from the connections."""
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triads_with_t(graph):
    """Finds all triads and filters those with at least one 't'-starting name."""
    triads_with_t = 0
    for node in graph:
        neighbors = graph[node]
        for n1, n2 in combinations(neighbors, 2):
            if n2 in graph[n1]:
                if node.startswith('t') or n1.startswith('t') or n2.startswith('t'):
                    triads_with_t += 1
    return triads_with_t

def find_largest_clique(graph):
    """Finds the largest clique in the graph using a greedy approach."""
    max_clique = []
    for node in graph:
        clique = {node}
        candidates = graph[node]
        for neighbor in candidates:
            if all(neighbor in graph[n] for n in clique):
                clique.add(neighbor)
        if len(clique) > len(max_clique):
            max_clique = list(clique)
    return sorted(max_clique)

def main():
    # Read and process input
    connections = read_input(INPUT_FILE)
    graph = build_graph(connections)

    # Find triads with at least one 't'-starting name
    triads_with_t_count = find_triads_with_t(graph)

    # Find the largest clique
    largest_clique = find_largest_clique(graph)

    # Compute the password
    password = ",".join(largest_clique)

    # Output the results
    print(f"Total triads with at least one 't': {triads_with_t_count}")
    print(f"Password to get into the LAN party: {password}")

if __name__ == "__main__":
    main()
