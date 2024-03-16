from algorithms import *
from tests import *


def dijkstra(adj_list, start):
    """
    Takes the adjacency list of a weighted (D or U) graph
    Then runs Dijkstra's shortest path algorithm starting from vertex start
    Then returns a par (parent, distance) that contains the parent and distance arrays
    """
    adjacency_list, _ = adj_list[0], adj_list[1]
    n = len(adjacency_list)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adjacency_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    return parent, distance


# Dijkstra
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

dijkstra(adjacency_list(graph_string), 1)

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))
