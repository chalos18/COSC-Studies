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


def which_segments(city_map):
    """
    Takes the map of the city and returns the list of road segments that
    must be cleared so that there is a clear path between any two locations and the total
    length of the cleaned-up road segments is minimised

    Undirectted weighted graph, each vertex is one location in the city.
    Each two way road segment is represented as an edge which connects two locations together
    and the weight of the edge is the length of road segment

    The given city has at least one location
    There is a path between any two locations

    The output is a list of orad segments that must be cleared
    Each segment is a tuple of two lcoation numbers
    The smaller number should appear first.
    If the solution is not unique, it does not matter which solution is returned by the function
    """
    adj_list, _ = adjacency_list(city_map)
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[0] = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u

    # road_segments= []
    # print(parent)
    # print(distance)
    # for i in range(len(distance)):
    #     if parent[i] != None:
    #         road_segments.append((parent[i], i))

    # return road_segments

    road_segments = []
    for i, p in enumerate(parent):
        if p is not None:
            road_segments.append((p, i) if p < i else (i, p))
    return road_segments


# city_map = """\
# U 4 W
# 0 1 5
# 1 3 5
# 3 2 3
# 2 0 5
# 0 3 2
# 1 2 1
# """

# print(sorted(which_segments(city_map)))


# city_map = """\
# U 3 W
# 0 1 1
# 2 1 2
# 2 0 4
# """

# city_map = """\
# U 4 W
# 0 2 5
# 0 3 2
# 3 2 1
# """

# a = which_segments(city_map)
# print(a)


# city_map = """\
# U 1 W
# """

# print(sorted(which_segments(city_map)))
