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


def min_capacity(city_map, depot_position):
    """
    The city_map is the textual representation of an undirected weighted graph.
    There is a vertex for each location in the city. There is an edge for each segment of road.
    All roads are two-way. The length of the road segment is the weight of the edge.
    The parameter depot_position is a location in the city where the depot is located.

    The function must return an integer that is the minimum capacity required for the battery.
    """
    no_inf = []
    city_map = adjacency_list(city_map)
    shortest_distances = dijkstra(city_map, depot_position)[1]
    for a in shortest_distances:
        if a != math.inf:
            no_inf.append(a)
    max_distance = max(no_inf)
    min_capacity = ((max_distance * 2) * 3 // 2) * 4 // 3

    return min_capacity