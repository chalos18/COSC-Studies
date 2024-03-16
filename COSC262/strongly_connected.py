from algorithms import *
from tests import *


def is_strongly_connected(adj_list):
    """
    Takes the adjacency list of a graph which has at least one vertex
    and returns true if the graph is strongly connected, false otherwise
    """
    adjacency_list, _ = adj_list[0], adj_list[1]

    #  Bfs tree starting on vertex 0
    len_adjacency_list = len(adjacency_list)
    for i in range(len_adjacency_list):
        _, state = bfs_tree(adjacency_list, i)
        if "U" in state:
            return False
        else:
            tranpose_list = transpose(adj_list)
            _, state = bfs_tree(tranpose_list, i)
            if "U" in state:
                return False
    return True


# # Strongly connected
graph_string = """\
D 3
0 1
1 0
0 2
"""
b, direction = adjacency_list(graph_string)
# print(b)
print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 3
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))
