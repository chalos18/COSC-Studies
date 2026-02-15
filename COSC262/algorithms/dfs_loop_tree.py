from algorithms import *
from tests import *


def dfs_loop(adj_list, u, state, parent):
    for v in adj_list[u]:
        v = v[0]
        if state[v] == "U":
            state[v] = "D"
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)
    state[u] = "P"


def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    state[start] = "D"
    dfs_loop(adj_list, start, state, parent)

    return parent


# an undirected graph

adj_list = [[(1, None), (2, None)], [(0, None), (2, None)], [(0, None), (1, None)]]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))
