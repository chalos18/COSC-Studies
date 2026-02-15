from collections import deque
from algorithms import *
from tests import *


def bfs_loop(adj_list, Q, state, parent):
    while len(Q) != 0:
        u = deque.popleft(Q)
        for v in adj_list[u]:
            v = v[0]
            if state[v] == "U":
                state[v] = "D"
                parent[v] = u
                Q.append(v)
        state[u] = "P"
    return parent


def bfs_tree(adj_list, start_index):
    """
    performs BFS and returns the parent array at the end of the search
    the elements of the parent array must be inialised to None at the beggining of the search
    """
    # n of vertices
    n = len(adj_list)

    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]

    Q = deque([])
    state[start_index] = "D"
    Q.append(start_index)

    return bfs_loop(adj_list, Q, state, parent), state

converters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""
a = adjacency_list(converters_info_str)
b = bfs_tree(a[0], 3)
print(b)

#  BFS tree
# an undirected graph
# adj_list = [[(1, None)], [(0, None), (2, None)], [(1, None)]]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))
