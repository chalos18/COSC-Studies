import math
from algorithms import *


def dfs_backtrack(candidate, input, destination, output, adj_list):
    if is_solution(candidate, destination):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate, adj_list):
            dfs_backtrack(child_candidate, input, destination, output, adj_list)


def is_solution(candidate, destination):
    return candidate[-1] == destination


def children(candidate, adj_list):
    last_vertex = candidate[-1]
    if last_vertex not in adj_list:
        return []

    children_vertices = []
    for neighbor in adj_list[last_vertex]:
        if neighbor not in candidate:
            children_vertices.append(
                candidate + [neighbor]
            )  # Append single element to list
    return children_vertices


def add_to_output(candidate, output):
    output.append(candidate)


def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack(
        [source], source, destination, solutions, adj_list
    )  # Pass source as a list
    return solutions


# Example usage:
triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list, _ = adjacency_list(triangle_graph_str)  # Unpack the tuple
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))

graph_str = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

adj_list, _ = adjacency_list(graph_str)  # Unpack the tuple
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))

graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

adj_list, _ = adjacency_list(graph_str)  # Unpack the tuple
print(sorted(all_paths(adj_list, 6, 3)))
