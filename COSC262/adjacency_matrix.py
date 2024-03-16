from algorithms import *
from tests import *


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


# Adjacency_matrix
graph_string = """\
D 3
0 1
1 0
0 2
"""

print(adjacency_matrix(graph_string))
