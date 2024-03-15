from pprint import pprint
from collections import deque


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


graph_string = """\
D 3
0 1
1 0
0 2
"""
# print(adjacency_list(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
# print(adjacency_list(graph_string))

# undirected graph in the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

# pprint(adjacency_list(graph_string))

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

# pprint(adjacency_list(graph_string))

graph_string = """\
U 17 W
1 2 3
1 15 5
1 6 4
12 13 2
2 15 6
13 4 7
4 5 8
"""

# pprint(adjacency_list(graph_string))


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


graph_string = """\
D 3
0 1
1 0
0 2
"""

# print(adjacency_matrix(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
# print(adjacency_matrix(graph_string))

graph_string = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""

# pprint(adjacency_matrix(graph_string))

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

# result = pprint(adjacency_matrix(graph_string))


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


# an undirected graph
# adj_list = [[(1, None)], [(0, None), (2, None)], [(1, None)]]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


# a directed graph (note the asymmetrical adjacency list)

# adj_list = [[(1, None)], []]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


# graph_string = """\
# D 2
# 0 1
# """

# print(bfs_tree(adjacency_list(graph_string), 0))


# graph_string = """\
# D 2
# 0 1
# 1 0
# """

# print(bfs_tree(adjacency_list(graph_string), 1))


# graph from the textbook example
# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# print(bfs_tree(adjacency_list(graph_string), 1))


# graph_string = """\
# D 2 W
# 0 1 99
# """

# print(bfs_tree(adjacency_list(graph_string), 0))


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

# adj_list = [[(1, None), (2, None)], [(0, None), (2, None)], [(0, None), (1, None)]]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))
# print(dfs_tree(adj_list, 2))


# def adjacency_list():
#     pass


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


# graph_string = """\
# D 7
# 1 6
# 1 2
# 1 5
# 2 5
# 2 3
# 5 4
# 3 4
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# graph_string = """\
# D 3 W
# 0 1 7
# 1 0 -2
# 0 2 0
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# It should also work undirected graphs.
# The output will be the same as input.

# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# print(graph_adj_list)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# graph_string = """\
# U 17
# 1 2
# 1 15
# 1 6
# 12 13
# 2 15
# 13 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


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


# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """
# b, direction = adjacency_list(graph_string)
# # print(b)
# print(is_strongly_connected(adjacency_list(graph_string)))

# graph_string = """\
# D 3
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))


# graph_string = """\
# D 4
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))


# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))
