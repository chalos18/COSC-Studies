from pprint import pprint
from collections import deque
import math


def undirected_adjaceny_list(u_list, edges, weighted=False):
    if weighted == True:
        for line in u_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            vert_two = int(vertices[1])
            edges[vert].append((int(vertices[1]), int(vertices[2])))
            edges[vert_two].append((int(vertices[0]), int(vertices[2])))
    else:
        for line in u_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            vert_two = int(vertices[1])
            edges[vert].append((int(vertices[1]), (None)))
            edges[vert_two].append((int(vertices[0]), (None)))

    return edges


def directed_adjacency_list(o_list, edges, weighted=False):
    if weighted == True:
        for line in o_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            edges[vert].append((int(vertices[1]), int(vertices[2])))
    else:
        for line in o_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            edges[vert].append((int(vertices[1]), (None)))

    return edges


def adjacency_list(graph_string):
    # Initialize variables to store graph information
    edges = []
    num_vertices = 0
    weighted = False

    lines = graph_string.strip().split("\n")
    direction = lines[0].split()[0]
    num_vertices = int(lines[0].split()[1])
    for _ in range(num_vertices):
        edges.append([])

    if "W" in lines[0]:
        weighted = True

    if direction == "U":
        result = undirected_adjaceny_list(lines, edges, weighted)
    else:
        result = directed_adjacency_list(lines, edges, weighted)

    return result, direction
    # return result


def undirected_adjacency_matrix(u_list, edges, num_vertices, weighted=False):
    if weighted == True:
        for lists in edges:
            for _ in range(num_vertices):
                lists.append(None)
        for line in u_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            position = int(vertices[1])
            weight = int(vertices[2])
            edges[vert][position] = weight
            edges[position][vert] = weight
    else:
        for lists in edges:
            for _ in range(num_vertices):
                lists.append(0)
        for line in u_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            position = int(vertices[1])
            edges[vert][position] = 1
            edges[position][vert] = 1

    return edges


def directed_adjacency_matrix(o_list, edges, num_vertices, weighted=False):
    if weighted == True:
        for lists in edges:
            for _ in range(num_vertices):
                lists.append(None)
        for line in o_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            position = int(vertices[1])
            weight = int(vertices[2])
            edges[vert][position] = weight
    else:
        for lists in edges:
            for _ in range(num_vertices):
                lists.append(0)
        for line in o_list[1:]:
            vertices = line.split()
            vert = int(vertices[0])
            position = int(vertices[1])
            print(edges[vert])
            edges[vert][position] = 1

    return edges


def adjacency_matrix(graph_string):
    # Initialize variables to store graph information
    edges = []
    num_vertices = 0
    weighted = False

    lines = graph_string.strip().split("\n")
    direction = lines[0].split()[0]
    num_vertices = int(lines[0].split()[1])
    for _ in range(num_vertices):
        edges.append([])

    if "W" in lines[0]:
        weighted = True

    if direction == "U":
        result = undirected_adjacency_matrix(lines, edges, num_vertices, weighted)
    else:
        result = directed_adjacency_matrix(lines, edges, num_vertices, weighted)

    return result


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


def next_vertex(in_tree, distance):
    min_distance = float("inf")
    min_vertex = None

    for i, dist in enumerate(distance):
        if not in_tree[i]:
            if dist < min_distance:
                min_distance = dist
                min_vertex = i
            elif min_vertex is None:
                min_vertex = i

    return min_vertex


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


def distance_matrix(adj_list):
    n = len(adj_list)
    matrix = [[math.inf] * n for _ in range(n)]
    iterator = 0
    for row in matrix:
        row[iterator] = 0
        iterator += 1

    for i, row in enumerate(adj_list):
        for edge in row:
            vertex, weight = edge[0], edge[1]
            matrix[i][vertex] = weight

    return matrix


def floyd(distance):
    n = len(distance)
    new_distance = [row[:] for row in distance]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if new_distance[i][j] > new_distance[i][k] + new_distance[k][j]:
                    new_distance[i][j] = new_distance[i][k] + new_distance[k][j]
    return new_distance


# graph_str = """\
# D 3 W
# 0 1 1
# 1 2 2
# 2 0 4
# """
# adj_graph = adjacency_list(graph_str)[0]
# matrix = distance_matrix(adj_graph)
# print("initial distance matrix:")
# print(matrix)
# print("Shortest path distances:")
# print(floyd(matrix))
# print("final distance matrix:")
# print(matrix)
# print("distance matrix should unchanged")


# graph_str = """\
# D 3 W
# 0 1 1
# 1 2 2
# 2 0 4
# """

# adj_list = adjacency_list(graph_str)[0]
# dist_matrix = distance_matrix(adj_list)
# print("Initial distance matrix:", dist_matrix)
# dist_matrix = floyd(dist_matrix)
# print("Shortest path distances:", dist_matrix)

graph_str = """\
U 3 W
0 1 5
2 1 7
"""

# adj_list = adjacency_list(graph_str)[0]
# print(adj_list)
# print(distance_matrix(adj_list))

# # more readable output (less readable code):
# print("\nEach row on a new line:")
# print("\n".join(str(lst) for lst in distance_matrix(adj_list)))


graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)[0]
# print(adj_list)
# print(distance_matrix(adj_list))
