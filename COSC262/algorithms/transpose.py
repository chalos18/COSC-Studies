from algorithms import *
from tests import *


def transpose(adj_list):
    """
    The tranpose of a graph is one where every edge points to the opposite direction - for directed graphs
    For undirected graphs the output will be the same as input.
    """
    direction = adj_list[1]
    adjacency_list = adj_list[0]
    new_list = [[] for _ in range(len(adjacency_list))]
    if direction == "U":
        return adjacency_list
    else:
        index = 0
        for i_list in adjacency_list:
            # list_index = adjacency_list.index(i_list)
            for i_tuple in i_list:
                vert = i_tuple[0]
                new_tuple = (index, i_tuple[1])
                new_list[vert].append(new_tuple)
            index += 1
    return new_list


# Transpose
graph_string = """\
D 7
1 6
1 2
1 5
2 5
2 3
5 4
3 4
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))
