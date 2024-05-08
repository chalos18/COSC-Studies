from algorithms import *

# Adjacency list

graph_string = """\
D 3
0 1
1 0
0 2
"""
# print(adjacency_list(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
# print(adjacency_list(graph_string))

# undirected graph in the textbook example
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

# pprint(adjacency_list(graph_string))

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

# pprint(adjacency_list(graph_string))

graph_string = """\
U 17 W
1 2 3
1 15 5
1 6 4
12 13 2
2 15 6
13 4 7
4 5 8
"""

# pprint(adjacency_list(graph_string))

# Adjacency_matrix
graph_string = """\
D 3
0 1
1 0
0 2
"""

# print(adjacency_matrix(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
# print(adjacency_matrix(graph_string))

graph_string = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""

# pprint(adjacency_matrix(graph_string))

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

# result = pprint(adjacency_matrix(graph_string))

#  BFS tree
# an undirected graph
# adj_list = [[(1, None)], [(0, None), (2, None)], [(1, None)]]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


# a directed graph (note the asymmetrical adjacency list)

# adj_list = [[(1, None)], []]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))


# graph_string = """\
# D 2
# 0 1
# """

# print(bfs_tree(adjacency_list(graph_string), 0))


# graph_string = """\
# D 2
# 0 1
# 1 0
# """

# print(bfs_tree(adjacency_list(graph_string), 1))


# graph from the textbook example
# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# print(bfs_tree(adjacency_list(graph_string), 1))


# graph_string = """\
# D 2 W
# 0 1 99
# """

# print(bfs_tree(adjacency_list(graph_string), 0))


# an undirected graph

# adj_list = [[(1, None), (2, None)], [(0, None), (2, None)], [(0, None), (1, None)]]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))
# print(dfs_tree(adj_list, 2))


# Transpose
# graph_string = """\
# D 7
# 1 6
# 1 2
# 1 5
# 2 5
# 2 3
# 5 4
# 3 4
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# graph_string = """\
# D 3 W
# 0 1 7
# 1 0 -2
# 0 2 0
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# It should also work undirected graphs.
# The output will be the same as input.

# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# print(graph_adj_list)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# graph_string = """\
# U 17
# 1 2
# 1 15
# 1 6
# 12 13
# 2 15
# 13 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))


# # Strongly connected
# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """
# b, direction = adjacency_list(graph_string)
# print(b)
# print(is_strongly_connected(adjacency_list(graph_string)))

# graph_string = """\
# D 3
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))


# graph_string = """\
# D 4
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))


# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

# print(is_strongly_connected(adjacency_list(graph_string)))


# Next vertex

# failing edge case
# in_tree = [True, False, False, True]
# distance = [3, 5, 3, 0]
# print(next_vertex(in_tree, distance))

# failing edge case - not failing
# in_tree = [True, True, True, False, True]
# distance = [math.inf, 0, math.inf, math.inf, math.inf]
# print(next_vertex(in_tree, distance))

# in_tree = [False, True, True, False, False]
# distance = [math.inf, 0, 3, 12, 5]
# print(next_vertex(in_tree, distance))


# in_tree = [False, False, False]
# distance = [math.inf, 0, math.inf]
# print(next_vertex(in_tree, distance))


# in_tree = [False, True, False, False]
# distance = [math.inf, 0, math.inf, 1_000_000]
# print(next_vertex(in_tree, distance))


# in_tree = [True, True, True, False, True]
# distance = [math.inf, 0, math.inf, math.inf, math.inf]
# print(next_vertex(in_tree, distance))

# in_tree = [False, True, True, False, False]
# distance = [math.inf, 0, 3, 12, 5]
# print(next_vertex(in_tree, distance))

# in_tree = [False, True, True, False, False, True, False]
# distance = [0, 5, 7, 4, 2, 3, 2]
# print(next_vertex(in_tree, distance))


# in_tree = [True, False, False, False, False, False, False]
# distance = [0, 5, 7, 12, math.inf, math.inf, math.inf]
# print(next_vertex(in_tree, distance))


# Dijkstra
# graph_string = """\
# D 3 W
# 1 0 3
# 2 0 1
# 1 2 1
# """

# dijkstra(adjacency_list(graph_string), 1)

# print(dijkstra(adjacency_list(graph_string), 1))
# print(dijkstra(adjacency_list(graph_string), 2))


# graph_string = """\
# U 4 W
# 0 2 5
# 0 3 2
# 3 2 2
# """

# print(dijkstra(adjacency_list(graph_string), 0))
# print(dijkstra(adjacency_list(graph_string), 2))


def coins_reqd(value, coinage):
    """Minimum number of coins to represent value.
    Assumes there is a 1-unit coin."""
    num_coins = [0] * (value + 1)
    for amt in range(1, value + 1):
        num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if c <= amt)

    print(num_coins)
    # The value of the num_coins array is displayed at this point.
    return num_coins[value]


# print(coins_reqd(19, [1,5,7,11]))
# coinage = [1, 10, 25]
# amount = 30
# answer = coins_reqd(amount, coinage)

# print(answer)


def coins_reqd(value, coinage):
    """A version that keeps track of the coinage used"""
    num_coins = [0] * (value + 1)
    coinage_used = [[] for _ in range(value + 1)]

    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[
                    amt - c
                ]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    coinage_used[amt] = coinage_used[amt - c] + [c]
        num_coins[amt] = 1 + minimum

    # print(coinage_used)
    coin_counts = {}
    for coin in coinage_used[value]:
        coin_counts[coin] = coin_counts.get(coin, 0) + 1

    return sorted(coin_counts.items(), reverse=True)


# For example, a call to coins_reqd(32, [1, 10, 25]) should return [(10, 3), (1, 2)].
coinage = [1, 10, 25]
amount = 32
# answer = coins_reqd(amount, coinage)

# print(answer)

"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float("inf")  # Same as math.inf


def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
    The file must consist of n lines of m space-separated integers.
    n and m are inferred from the file contents.
    Returns the grid as an n element list of m element lists.
    THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
    grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    cache = {}

    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            cost = grid[row][col]
            # print(row)
            if (row, col) in cache:
                return cache[(row, col)]
            if row != 0:
                cost += min(
                    cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2)
                )
                cache[(row, col)] = cost
            # print(cache)
            return cost

    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
    weights read from the given file
    """
    return grid_cost(read_grid(filename))


# 3
# print(file_cost("COSC262/checkerboard_trivial.txt"))

# 8
# print(file_cost("COSC262/checkerboard_small.txt"))


"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""

INFINITY = float("inf")


def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
    The file must consist of n lines of m space-separated integers.
    n and m are inferred from the file contents.
    Returns the grid as an n element list of m element lists.
    THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
    integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    # Create a DP table to store the minimum costs
    dp = [[0] * n_cols for _ in range(n_rows)]

    # Fill in the base case: the cost of the first row is just the grid itself
    dp[0] = grid[0]
    print(grid)
    print(dp[0])

    # Build up the DP table iteratively
    for row in range(1, n_rows):
        for col in range(n_cols):
            # The cost of reaching this cell is the cost of the cell itself
            # plus the minimum cost of reaching the cell from the above row
            # considering all possible moves
            dp[row][col] = grid[row][col] + min(
                dp[row - 1][col + delta_col]
                for delta_col in range(-1, 2)
                if 0 <= col + delta_col < n_cols
            )

    # The best cost is the minimum cost of reaching the last row
    best = min(dp[n_rows - 1])
    return best


def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
    weights read from the given file
    """
    return grid_cost(read_grid(filename))


# print(file_cost("COSC262/checkerboard_trivial.txt"))

# print(file_cost("COSC262/checkerboard_small.txt"))

# print(file_cost("COSC262/checkerboard_medium.txt"))

# print(file_cost("COSC262/checkerboard_large.txt"))
