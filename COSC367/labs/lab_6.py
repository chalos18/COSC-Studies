import itertools
import random

import numpy as np


def n_queens_neighbours(state: tuple):
    """
    Returns a sorted list of states that are neighbours of the current assignment -> does not allow repeated numbers in a sequence
    A neighbour is obtained by swapping the position of two numbers in the given permutation.
    state: tuple (permutations of 1 to n)
    Do not generate all possible permutations of n
    """
    # swap the elements in the given permutations
    # temporarily convert the tuples into a list to perform the swap
    # then convert them back to tuple
    states = []
    state_list = list(state)
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if i != j:
                swapped = state_list.copy()
                swapped[i], swapped[j] = swapped[j], swapped[i]
                states.append(tuple(swapped))
    return sorted(states)


# print(n_queens_neighbours((1, 2)))

# print(n_queens_neighbours((1, 3, 2)))

# print(n_queens_neighbours((1, 2, 3)))

# print(n_queens_neighbours((1,)))

# for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
#     print(neighbour)

# for neighbour in n_queens_neighbours((2, 3, 1, 4)):
#     print(neighbour)


def n_queens_cost(state):
    """
    Returns the number of conflicts for that state
    Number of conflicts is the number of unordered pairs of queens that threaten each other
    state: total assignment, entire board configuration, index of tuple = x, value of index = y
    """
    conflict = 0
    # Diagonals have a slope of 1 or -1
    queens = []
    for x, y in enumerate(state):
        # + 1 to match column row indexing
        queen_position = (x + 1, y)
        queens.append(queen_position)
    # print(queens)
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            dx = x1 - x2
            dy = y1 - y2
            if abs(dx) == abs(dy):
                conflict += 1
    return conflict


# print(n_queens_cost((1, 2)))

# print(n_queens_cost((1, 2)))

# print(n_queens_cost((1, 2, 3)))

# print(n_queens_cost((1,)))

# print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

# print(n_queens_cost((2, 3, 1, 4)))


def greedy_descent(initial_state, neighbours, cost):
    """
    Returns a list of states it goes through in the order they are encountered.
    initial_state: the state from which the search starts
    neighbours: a function that takes a state and returns a list of neighbours
    cost: a function that takes a state returns its cost (e.g. number of conflicts).
    """
    states_iter = [initial_state]
    initial_state_cost = cost(initial_state)
    while True:
        state_neighbours = neighbours(initial_state)
        if not state_neighbours:
            break

        neighbours_w_cost = [
            (cost(s_neighbour), s_neighbour) for s_neighbour in state_neighbours
        ]

        min_neighbour = min(neighbours_w_cost, key=lambda x: x[0])
        neighbour_cost, neighbour_state = min_neighbour

        if neighbour_cost < initial_state_cost:
            states_iter.append(neighbour_state)
            initial_state = neighbour_state
            initial_state_cost = cost(neighbour_state)
        else:
            break

    return states_iter


# def cost(x):
#     return x**2


# def neighbours(x):
#     return [x - 1, x + 1]


# for state in greedy_descent(4, neighbours, cost):
#     print(state)


# def cost(x):
#     return x**2


# def neighbours(x):
#     return [x - 1, x + 1]


# for state in greedy_descent(-6.75, neighbours, cost):
#     print(state)


# def cost(x):
#     return -x**2


# def neighbours(x):
#     return [x + 1, x - 1] if abs(x) < 5 else []


# for state in greedy_descent(0, neighbours, cost):
#     print(state)


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    """
    Uses greedy descent to find a solution
    """
    r_state = random_state()
    # print(r_state)
    # n_q_neighbours = n_queens_neighbours(r_state)
    # print(n_q_neighbours)
    while True:
        g_descent = greedy_descent(
            initial_state=r_state,
            neighbours=neighbours,
            cost=cost,
        )
        for descent in g_descent:
            print(descent)
        # a global minimum state has a cost of zero
        if cost(g_descent[-1]) != 0:
            print("RESTART")
            r_state = random_state()
        # if global minimum of zero is reached, algo stops
        else:
            break


# N = 6
# random.seed(0)


# def random_state():
#     return tuple(random.sample(range(1, N + 1), N))


# greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)


# N = 8
# random.seed(0)


# def random_state():
#     return tuple(random.sample(range(1, N + 1), N))


# greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)


def gradient_optimize(x0, gradient, step_factor, direction, iterations):
    for _ in range(iterations):
        if direction == -1:
            x0 = x0 - step_factor * gradient(x0)
        else:
            x0 = x0 + step_factor * gradient(x0)
    return x0


def f(x):
    return x**2


def f_prime(x):
    return 2 * x


# x0 = 2
# x_star = gradient_optimize(x0, f_prime, 0.1, -1, 250)
# print(f"x* = {x_star:.2f}, f(x*) = {f(x_star):.2f}")

# def f(x):
#     return 1 - x ** 2

# def f_prime(x):
#     return -2 * x

# x0 = 2
# x_star = gradient_optimize(x0, f_prime, 0.1, 1, 250)
# print(f"x* = {x_star:.2f}, f(x*) = {f(x_star):.2f}")

# # single maximum at x* = [1, -1] with f(x*) = 2
# def f(x):
#     return 2 - (1 - x[0])**2 - (x[1] + 1)**2

# def gradient_of_f(x):
#     return np.array([2 * (1 - x[0]), -2 * (x[1] + 1)])

# x_star = gradient_optimize(np.zeros(2), gradient_of_f, 0.1, 1, 250)

# print(np.all(np.isclose(x_star, np.array([1, -1]))), np.isclose(f(x_star), 2))


# def f(x): # This function has two minimums
#     return x**4 - x**3 - x**2 + 1

# def f_prime(x):
#     return 4 * x**3 - 3 * x**2 - 2 * x

# x0 = -1 # if x < 0 we get stuck in a local minimum
# x_star1 = gradient_optimize(-1, f_prime, 0.1, -1, 250)

# x0 = 1 # if x > 0 we should converge to the global minimum
# x_star2 = gradient_optimize(1, f_prime, 0.1, -1, 250)

# print(f"x0 = -1, x* = {x_star1:.4f}, f(x*) = {f(x_star1):.4f}")
# print(f"x0 = 1, x* = {x_star2:.4f}, f(x*) = {f(x_star2):.4f}")


def roulette_wheel_select(population, fitness, r):
    total_fitness = sum([fitness(individual) for individual in population])
    running_total = 0
    for individual in population:
        indv_fitness = fitness(individual)
        # compare against a normalised cumulative probability 
        running_total += indv_fitness / total_fitness
        if running_total >= r:
            return individual


population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))


# population = [0, 1, 2]

# def fitness(x):
#     return x

# for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
#     print(roulette_wheel_select(population, fitness, r))
