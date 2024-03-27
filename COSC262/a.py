import math

def distance_matrix(adj_list):
    n = len(adj_list)
    matrix = [[math.inf] * n for _ in range(n)]
    iterator = 0
    for row in matrix:
        row[iterator] = 0
        iterator += 1

    for i, row in enumerate(adj_list):
        for edge in row:
            vertex, weight = edge[0], edge[1]
            matrix[i][vertex] = weight

    return matrix
