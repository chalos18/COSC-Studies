# Q2. Write an asymptotically most efficient implementation of the function compute(numbers) given bellow
import math
from collections import deque


def compute(numbers):
    n = len(numbers)
    output = [0] * n  # a list of length n filled with zeros
    for i in range(n):
        j = 0
        while j <= i:
            output[i] += numbers[j]
            j += 1
    return output


# Attempt 1
def compute_asym(numbers):
    n = len(numbers)
    output_list = []
    i = 0
    highest = 0
    while len(output_list) < n:
        highest += i
        output_list.append(highest)
        i += 1
    return output_list


result = compute_asym(list(range(10**2)))
expected = compute(list(range(10**2)))

assert result == expected

# This runs
# print(compute_asym(list(range(10**5))))


# Q6 Study Backtracking for these types of questions
def word_chains(words, min_length, max_length):
    """
    A word chain is:
    - every word in the sequence is from the given set of words;
    - no word in the sequence is repeated (i.e. a word appears at most once); and
    - for every two consecutive words in the sequence, the last letter of the first word is the same as the first letter of the next word.
    Returns a list of all the possible word chains of length greater than or equal to min_length and less than or equal to max_length
    """
    result = []
    words = list(words)  # Convert set to list to handle indexing

    def backtrack(current_chain):
        if min_length <= len(current_chain) <= max_length:
            result.append(current_chain[:])  # Add a copy of current chain to result

        if len(current_chain) < max_length:
            last_char = current_chain[-1][-1] if current_chain else None
            for word in words:
                if word not in current_chain and (
                    not current_chain or word[0] == last_char
                ):
                    current_chain.append(word)
                    backtrack(current_chain)
                    current_chain.pop()

    # Start backtracking with each word
    backtrack([])
    return result


words = {"apple", "banana", "apricot", "tab"}

output = word_chains(words, 0, 1)
# output.sort()
# print(output)

words = {"apple", "banana", "apricot", "tab"}

# for word_chain in sorted(word_chains(words, 2, 10)):
#     print(word_chain)


def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == "D"
    weighted = len(header) == 3 and header[2] == "W"
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list


# def next_vertex(in_tree, distance):
#     for vertex in enumerate(distance):
#         if vertex[1] != math.inf and in_tree[vertex[0]] != True:
#             lowest = vertex
#             if vertex[1] <= lowest[1]:
#                 lowest = vertex
#     return lowest[0]


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


# Using Dijkstra
def min_shipping_costs(adj_list, transit_cost, source):
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[source] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            transit_cost = list(transit_cost)
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    return parent, distance


graph_string = """\
U 3 W
0 1 1
1 2 2
"""

transit_cost = {0: 3, 1: 4, 2: 5}
# print(min_shipping_costs(adjacency_list(graph_string), transit_cost, 0))
# print(min_shipping_costs(adjacency_list(graph_string), transit_cost, 1))


class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity, n=None, cache=None):
    """
    Returns the maximum value achievable with the given list of items
    and a knapsack of the given capacity.
    fewer than 500 items and fewer than 500 capacity
    """
    if n is None:
        n = len(items)
    if cache is None:
        cache = {}
    if n == 0 or capacity == 0:
        return 0
    elif (n, capacity) in cache:
        return cache[(n, capacity)]
    elif items[n - 1].weight > capacity:
        return max_value(items, capacity, n - 1, cache)
    else:
        best = max(
            max_value(items, capacity, n - 1, cache),
            items[n - 1].value
            + max_value(items, capacity - (items[n - 1].weight), n - 1, cache),
        )
        cache[(n, capacity)] = best
        return best


def maximum_expertise(budget, candidates, n=None, cache=None):
    """
    Can allocate anyone to work part time at multiples of 10%
    """
    sorted_candidates = sorted(candidates)
    if n is None:
        n = len(candidates)
    if cache is None:
        cache = {}
    if n == 0 or budget == 0:
        return 0
    elif (n, budget) in cache:
        return cache[(n, budget)]
    # elif sorted_candidates[n - 1][1] > budget:
    #     return maximum_expertise(budget, sorted_candidates, n - 1, cache)
    else:
        # best = max(maximum_expertise(budget, sorted_candidates, n - 1, cache), sorted_candidates[
        #     n - 1
        # ][0] + maximum_expertise(
        #     budget - (sorted_candidates[n - 1][1]), sorted_candidates, n - 1, cache
        # ))
        # cache[(n, budget)] = best
        # return best
        best = maximum_expertise(budget, sorted_candidates, n - 1, cache)
        for percentage in range(10, 110, 10):
            fractional_salary = sorted_candidates[n - 1][1] * (percentage / 100)
            fractional_expertise = sorted_candidates[n - 1][0] * (percentage / 100)
            if budget >= fractional_salary:
                best = max(
                    best,
                    fractional_expertise
                    + maximum_expertise(
                        budget - fractional_salary, sorted_candidates, n - 1, cache
                    ),
                )
        cache[(n, budget)] = best
        return best


#                  (value, weight)
#               (expertise, salary)
# candidates = [(60, 50), (100, 50)]
# print(maximum_expertise(80, candidates))

# candidates = [(70, 30), (5000, 80), (80, 40)]
# print(maximum_expertise(7, candidates))

# # The example from the lecture notes
# items = [Item(45, 3), Item(45, 3), Item(80, 4), Item(80, 5), Item(100, 8)]

# print(max_value(items, 10))


def tupleise(value, items, index=0):
    if index >= len(items):
        return []
    else:
        first = items[index]
        iterator = tupleise(value, items, index + 1)
        return [(value, first)] + iterator


# print(tupleise(7, [10, 99, 35, 40]))


def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == "D"
    weighted = len(header) == 3 and header[2] == "W"
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list


def bfs_tree(adj, s):
    n = len(adj)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque([])
    state[s] = "D"
    Q.append(s)
    return bfs_loop(adj, Q, state, parent)


def bfs_loop(adj, Q, state, parent):
    while len(Q) != 0:
        u = deque.popleft(Q)
        for v in adj[u]:
            v = v[0]
            if state[v] == "U":
                state[v] = "D"
                parent[v] = u
                Q.append(v)
        state[u] = "P"
    return parent


# an undirected graph

adj_list = [[(1, None)], [(0, None), (2, None)], [(1, None)]]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


# a directed graph (note the asymmetrical adjacency list)

adj_list = [[(1, None)], []]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


graph_string = """\
D 2
0 1
"""

# print(bfs_tree(adjacency_list(graph_string), 0))


graph_string = """\
D 2
0 1
1 0
"""

# print(bfs_tree(adjacency_list(graph_string), 1))


# graph from the textbook example
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

# print(bfs_tree(adjacency_list(graph_string), 1))


graph_string = """\
D 2 W
0 1 99
"""

# print(bfs_tree(adjacency_list(graph_string), 0))


def path_length_1st_try(parent, start, end):
    if start == end:
        return 0
    elif parent[start] == None and parent[end] == None:
        return math.inf
    else:
        lowest_path = []
        for vertice, edge in enumerate(parent):
            if edge == None:
                parent[vertice + 1]
            else:
                parent[edge]


def path_length(parent, start, end):
    if start == end:
        return 0

    # Backtrack from the end vertex to the start vertex
    length = 0
    current = end

    while current is not None:
        if current == start:
            return length
        current = parent[current]
        length += 1

    return float("inf")


# print(path_length([None, 0, 1], 0, 2))
# print(path_length([None, None], 0, 0))
# print(path_length([None, None], 0, 1))


def itinerary_1st_try(adj_list, start, destination):
    """
    Returns an itinerary that achieves the travel in the minimum possible time assuming
    that we drive nonstop and at the speed limit
    """
    if start == destination:
        return [(0, 0)]
    cost = 0
    path = [(start, cost)]
    # backtrack
    current_vert = destination
    for vertice in range(start, destination, 1):
        best_edge = 0
        for edges in adj_list:
            best_edge = edges
            if edges <= best_edge:
                best_edge = edges

    while current_vert is not None:
        if current_vert == start:
            return path
        current_vert = adj_list[current_vert][0]
    return path


def itinerary_1st_try(adj_list, start, destination):
    """
    Returns an itinerary that achieves the travel in the minimum possible time assuming
    that we drive nonstop and at the speed limit
    """
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    shortest_distance = []
    for vertex, distances in enumerate(distance):
        if distances == math.inf:
            break
        else:
            shortest_distance.append((vertex, distances))

    return shortest_distance


# Using dijkstra
def itinerary(adj_list, start, destination):
    """
    Returns an itinerary that achieves the travel in the minimum possible time assuming
    that we drive nonstop and at the speed limit.
    """
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        if u is None:  # No more vertices are reachable
            break
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    # Construct the path from start to destination
    if distance[destination] == math.inf:
        return []

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    # Create the itinerary list
    itinerary_list = [(city, distance[city]) for city in path]

    return itinerary_list


map_graph_string = """\
U 4 W
0 1 4
1 2 5
"""

adj_list = adjacency_list(map_graph_string)

# print(itinerary(adj_list, 0, 2))
# print(itinerary(adj_list, 2, 1))
# print(itinerary(adj_list, 1, 1))
# print(itinerary(adj_list, 1, 3))


map_graph_string = """\
D 4 W
0 1 4
1 2 5
"""

adj_list = adjacency_list(map_graph_string)

# print(itinerary(adj_list, 0, 2))
# print(itinerary(adj_list, 2, 0))


import sys

sys.setrecursionlimit(100000)


def dumbo_func(data):
    """Takes a list of numbers and does weird stuff with it"""
    if len(data) == 0:
        return 0
    else:
        if (data[0] // 100) % 3 != 0:
            return 1 + dumbo_func(data[1:])
        else:
            return dumbo_func(data[1:])


def dumbo_func_better(data, index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if index >= len(data):
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func_better(data, index + 1)
        else:
            return dumbo_func_better(data, index + 1)


# import sys

# sys.setrecursionlimit(100000)

# Simple test with short list.
# Original func works fine on this
data = [677, 90, 785, 875, 7, 90393, 10707]
# print(dumbo_func_better(data))


def compute(numbers):
    n = len(numbers)
    output = [0] * n  # a list of length n filled with zeros
    for i in range(n):
        j = 0
        while j <= i:
            output[i] += numbers[j]
            j += 1
    return output


def compute_better(numbers):
    n = len(numbers)
    output = [0] * n  # a list of length n filled with zeros

    i = 0
    while len(numbers) < n:
        i += 1
        output.append(i)

    return output


def compute_asym(numbers):
    n = len(numbers)
    output_list = []
    i = 0
    highest = 0
    while len(output_list) < n:
        highest += i
        output_list.append(highest)
        i += 1
    return output_list


# Test to see if the function runs under one second.
# The output of the function is not printed.

# compute_better(list(range(10**5)))
# print("OK")

# compute_asym(list(range(10**5)))
# print("OK")


def calculate_sums(numbers):
    n = len(numbers)
    output = [0] * n  # a list of length n filled with zeros
    for i in range(n):
        for j in range(i + 1):
            output[i] += numbers[j]
    return output


def calculate_sums_asym(numbers):
    n = len(numbers)
    output = [0] * n  # a list of length n filled with zeros
    i = 0
    if n == 0:
        return output
    output[0] = numbers[0]
    for i in range(1, n):
        output[i] = output[i - 1] + numbers[i]

    return output


# calculate_sums_asym(list(range(10**5)))
# print("OK")


def aggregate(numbers):
    n = len(numbers)
    result = [0] * n  # a list of length n filled with zeros
    if n == 0:
        return result
    result[0] = numbers[0]
    for i in range(1, n):
        result[i] = result[i - 1] + result[i]


# aggregate(list(range(10**5)))
# print("OK")


# def next_vertex(in_tree, distance):
#     smallest = (0, distance[0])
#     for i, d in enumerate(distance):
#         if d < smallest[1] and in_tree[i] == False and d != math.inf:
#             smallest = (i, d)
#     return smallest[0]


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


in_tree = [False, False, False, True, True, False]
distance = [2, 3, 7, 4, 0, 8]
# print(next_vertex(in_tree, distance))


in_tree = [False, True, True, False, False]
distance = [math.inf, 0, 3, 12, 5]
# print(next_vertex(in_tree, distance))


in_tree = [False, False, False]
distance = [math.inf, 0, math.inf]
# print(next_vertex(in_tree, distance))


def dijkstra(adj, s, destination):
    n = len(adj)
    in_tree = [False for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        if u is None:  # No more vertices are reachable
            break
        in_tree[u] = True
        for v, weight in adj[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    # Construct the path from start to destination
    if distance[destination] == math.inf:
        return []

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    # Create the itinerary list
    itinerary_list = [(city, distance[city]) for city in path]

    return itinerary_list


map_graph_string = """\
U 4 W
0 1 4
1 2 5
"""

adj_list = adjacency_list(map_graph_string)

print(dijkstra(adj_list, 0, 2))
print(dijkstra(adj_list, 2, 1))
print(dijkstra(adj_list, 1, 1))
print(dijkstra(adj_list, 1, 3))
