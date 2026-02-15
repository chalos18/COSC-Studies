from collections import deque


def directed_adjacency_list(o_list, edges):
    for line in o_list[1:]:
        vertices = line.split()
        vert = int(vertices[0])
        edges[vert].append(int(vertices[1]))
    return edges


def adjacency_list(graph_string):
    lines = graph_string.strip().split("\n")
    num_vertices = int(lines[0].split()[1])
    edges = [[] for _ in range(num_vertices)]
    return directed_adjacency_list(lines, edges)


def bfs_loop(adj_list, queue, state, parent, source_format, destination_format):
    while queue:
        path = queue.popleft()
        current_format = path[-1]
        if current_format == destination_format:
            return path
        for neighbor in adj_list[current_format]:
            if state[neighbor] == "U":
                state[neighbor] = "D"
                parent[neighbor] = current_format
                queue.append(path + [neighbor])
        state[current_format] = "P"
    return "No solution!"


def bfs_tree(adj_list, source_format, destination_format):
    """
    performs BFS and returns the parent array at the end of the search
    the elements of the parent array must be inialised to None at the beggining of the search
    """
    # n of vertices
    n = len(adj_list)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    state[source_format] = "D"
    queue = deque([[source_format]])

    return (
        bfs_loop(adj_list, queue, state, parent, source_format, destination_format),
        state,
    )


def format_sequence(converters_info, source_format, destination_format):
    """
    Returns the shortest sequence of formats(and therefore converters) required in order to convert a video from the source to the destination format
    1. Input -
    converters_info: string representation of a directed graph, each vertex is a video format. The number of vertices is the number of possible video formats.
    For each converter that is available to the producer, there is an edge from the input format of the converter to the output format of the converter
    source_format: a natural number that specifies the format of the original video
    destination_format: a natural number that specifies the desired format
    """
    adj_list = adjacency_list(converters_info)
    path, state = bfs_tree(adj_list, source_format, destination_format)
    if path == "No solution!":
        return path
    else:
        return path


# converters_info_str = """\
# D 5
# 0 1
# 0 2
# 1 2
# 2 3
# 1 3
# 3 0
# """

# print(format_sequence(converters_info_str, 1, 0))
# print(format_sequence(converters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
# print(format_sequence(converters_info_str, 4, 4))
# print(format_sequence(converters_info_str, 3, 3))
# print(format_sequence(converters_info_str, 3, 2))
# print(format_sequence(converters_info_str, 3, 4))


# converters_info_str = """\
# D 2
# 0 1
# """

# source_format = 0
# destination_format = 1

# a = format_sequence(converters_info_str, source_format, destination_format)
# print(a)
# assert a == [0, 1]

# converters_info_str = """\
# D 2
# 0 1
# """

# b = format_sequence(converters_info_str, 1, 1)
# print(b)
# assert b == [1]

# converters_info_str = """\
# D 2
# 0 1
# """

# c = format_sequence(converters_info_str, 1, 0)
# print(c)
# assert c == "No solution!"

# converters_info_str = """\
# D 5
# 1 0
# 0 2
# 2 3
# 1 2
# """

# d = format_sequence(converters_info_str, 1, 2)
# print(d)
# assert d == [1, 2]

# converters_info_str = """\
# D 1
# """

# e = format_sequence(converters_info_str, 0, 0)
# print(e)
# assert e == [0]
