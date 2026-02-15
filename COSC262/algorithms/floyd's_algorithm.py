print("he")

def distance_matrix(adj_list):
    pass

graph_str = """\
U 3 W
0 1 5
2 1 7
"""

adj_list = adjacency_list(graph_str)
print(adj_list)
print(distance_matrix(adj_list))

# more readable output (less readable code):
# print("\nEach row on a new line:")
# print("\n".join(str(lst) for lst in distance_matrix(adj_list)))