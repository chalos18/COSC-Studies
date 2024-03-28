from pprint import pprint
from algorithms import *


def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False


def is_solution(candidate, input_data):
    """Returns True if the candidate is a complete solution"""
    return len(candidate) == len(input_data)


def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    diff = input_data - set(candidate)
    return [candidate + (element,) for element in diff]


# print(sorted(permutations({1, 2, 3})))

# print(sorted(permutations({"a"})))

# perms = permutations(set())
# print(len(perms) == 0 or list(perms) == [()])


def dfs_backtrack(candidate, input, output):
    if is_solution(candidate, input):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, input, output)


def is_solution(candidate, desired_length):
    return len(candidate) == desired_length


def children(candidate):
    return [candidate + "0", candidate + "1"]


def add_to_output(candidate, output):
    output.append(candidate)


def binary_numbers(desired_length):
    solutions = []
    dfs_backtrack("", desired_length, solutions)
    return solutions


# print(binary_numbers(4))
# print(binary_numbers(3))

# print(sorted(permutations({"a"})))

# perms = permutations(set())
# print(len(perms) == 0 or list(perms) == [()])


def dfs_backtrack(candidate, input, output):
    if is_solution(candidate, input):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, input, output)


def is_solution(candidate, desired_length):
    return len(candidate) == desired_length


def children(candidate):
    return [candidate + "0", candidate + "1"]


def add_to_output(candidate, output):
    output.append(candidate)


def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((), source, destination, solutions)
    return solutions




triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)[0]
# print(adj_list)
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

# adj_list = adjacency_list(graph_str)
# print(sorted(all_paths(adj_list, 0, 1)))


# graph used in tracing bfs and dfs
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

# adj_list = adjacency_list(graph_str)
# pprint(sorted(all_paths(adj_list, 6, 3)))
