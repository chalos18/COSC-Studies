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

    result = directed_adjacency_list(lines, edges, weighted)

    return result


graph_string = """\
D 3
0 1
1 0
0 2
"""
# print(adjacency_list(graph_string))


def build_order(dependencies):
    """
    Takes a description of the dependencies between a number of programs and returns a valid order for the build process.
    The input is a string representation of a directed graph.
    The number of vertices, n, is the number of programs of interest.
    When there is a directed edge from one program to another, the former should be built before the latter.
    Return a list of length n of programs in a valid order build process (from left to right). If there are multiple solutions, any one of them is acceptable.
    """
    adj_list = adjacency_list(dependencies)
    n = len(adj_list)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = []

    # Perform DFS from each vertex
    for u in range(n):
        if state[u] == "U":
            dfs_loop(adj_list, u, state, parent, stack)

    return stack[::-1]


def dfs_loop(adj_list, u, state, parent, stack):
    for v in adj_list[u]:
        v = v[0]
        if state[v] == "U":
            state[v] = "D"
            parent[v] = u
            dfs_loop(adj_list, v, state, parent, stack)
    state[u] = "P"
    stack.append(u)


# Failed test case - Passing
dependencies = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""
# result = build_order(dependencies)
# print(result)
# assert result == [6, 0, 1, 2, 5, 4, 3]


dependencies = """\
D 2
0 1
"""

result = build_order(dependencies)
# assert result == [0, 1]
# print(result)


dependencies = """\
D 3
1 2
0 2
"""

result = build_order(dependencies) in [[0, 1, 2], [1, 0, 2]]
# result = build_order(dependencies)
# print(result)
# assert result == True

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
# solution = build_order(dependencies)
# if solution is None:
#     print("Wrong answer!")
# else:
#     result = sorted(solution)
# print(result)

# assert result == [0, 1, 2]
