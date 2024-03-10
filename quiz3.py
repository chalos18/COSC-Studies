from pprint import pprint


def undirected_list(u_list, edges, weighted=False):
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


def directed_list(o_list, edges, weighted=False):
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
        result = undirected_list(lines, edges, weighted)
    else:
        result = directed_list(lines, edges, weighted)

    return result


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


def undirected_list(u_list, edges, num_vertices, weighted=False):
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


def directed_list(o_list, edges, num_vertices, weighted=False):
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
        result = undirected_list(lines, edges, num_vertices, weighted)
    else:
        result = directed_list(lines, edges, num_vertices, weighted)

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
