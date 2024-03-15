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

