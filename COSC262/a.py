def get_all_connected_groups(graph):
    already_seen = set()
    result = []
    for node in graph:
        if node not in already_seen:
            connected_group, already_seen = get_connected_group(node, already_seen)
            result.append(connected_group)
    return result


def get_connected_group(node, already_seen):
    result = []
    nodes = set([node])
    while nodes:
        node = nodes.pop()
        already_seen.add(node)
        nodes = nodes or graph[node] - already_seen
        result.append(node)
    return result, already_seen


graph = {
    0: {0, 1, 2, 3},
    1: set(),
    2: {1, 2},
    3: {3, 4, 5},
    4: {3, 4, 5},
    5: {3, 4, 5, 7},
    6: {6, 8},
    7: set(),
    8: {8, 9},
    9: set(),
}

components = get_all_connected_groups(graph)
print(components)
