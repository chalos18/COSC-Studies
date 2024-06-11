# Q2. Write an asymptotically most efficient implementation of the function compute(numbers) given bellow
import math


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
print(min_shipping_costs(adjacency_list(graph_string), transit_cost, 0))
# print(min_shipping_costs(adjacency_list(graph_string), transit_cost, 1))
