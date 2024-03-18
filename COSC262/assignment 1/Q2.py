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
    return parent, state


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


def connected_components(adj_list):
    n = len(adj_list)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    start_state = []
    for i in enumerate(state, 0):
        start_state.append(i)

    Q = deque()
    components = []
    for i in range(n):
        if state[i] == "U":
            previous_state = state[:]
            state[i] = "D"
            Q.append(i)
            bfs_loop(adj_list, Q, state, parent)
            new_components = []
            for i in range(len(previous_state)):
                if state[i] != previous_state[i]:
                    new_components.append(i)
            components.append(set(new_components))

    return components


def bubbles(physical_contact_info):
    """
    1. Takes physical contact information about a group of people and determines the bubbles
    2. Only undirected graphs
    3. Each vertex corresponds to one person. If and only if two people have physical contact,
    there is an edge between the corresponsing vertices
    4. The function must return a list, the order does not matter.
    5. The number of elements int he list must be equal to the number of bubbles
    6. Each element of the list is a set of people who are part of the same bubble(use a set or a list, order does not matter)
    """
    adj_list, _ = adjacency_list(physical_contact_info)
    components = connected_components(adj_list)
    return components


# physical_contact_info = """\
# U 2
# 0 1
# """

# # bubbles(physical_contact_info)
# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

# physical_contact_info = """\
# U 2
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


# physical_contact_info = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


# physical_contact_info = """\
# U 0
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


# physical_contact_info = """\
# U 1
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
