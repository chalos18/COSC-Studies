from search import *
import heapq
import itertools
import collections


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = itertools.count()
        # add more code if necessary

    def add(self, path):
        counter = next(self.counter)
        total_cost = sum(arc.cost for arc in path)

        heapq.heappush(self.container, (total_cost, counter, path))

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            total, counter, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration  # don't change this one


import collections


class BFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration  # don't change this one


class DFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = itertools.count()
        # add more code if necessary

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration  # don't change this one


# graph = ExplicitGraph(
#     nodes={"S", "A", "B", "G"},
#     edge_list=[
#         ("S", "A", 3),
#         ("S", "B", 1),
#         ("B", "A", 1),
#         ("A", "B", 1),
#         ("A", "G", 5),
#     ],
#     starting_nodes=["S"],
#     goal_nodes={"G"},
# )

# solution = next(generic_search(graph, LCFSFrontier()))
# print_actions(solution)


def select(population, error, max_error, r):
    total_fitness = sum([max_error - error(individual) for individual in population])
    running_total = 0
    for individual in population:
        indv_fit = max_error - error(individual)
        running_total += indv_fit / total_fitness
        if running_total >= r:
            return individual


# population = ["a", "b"]


# def error(x):
#     return {"a": 14, "b": 12}[x]


# max_error = 15

# for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
#     print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.


def roulette_wheel_select(population, fitness, r):
    """
    In the context of evolutionary computation, write a function roulette_wheel_select(population, fitness, r) that takes a list of individuals,
    a fitness function, and a floating-point random number r in the interval [0, 1), and selects and returns an individual from the population using the roulette wheel selection mechanism.
    The fitness function (provided as an argument) takes an individual and returns a non-negative number representing its fitness—the higher the fitness, the better.
    When constructing the roulette wheel, do not change the order of individuals in the population.
    """
    # get total fitness of population
    total_fitness = sum([fitness(individual) for individual in population])
    # set running total to 0 for for iteration
    running_total = 0
    # go through the population
    for individual in population:
        # get the individual fitness divided by total fitness and add it to running total
        indv_fitness = fitness(individual)
        running_total += indv_fitness / total_fitness
        # if that running total is greater or equal to r then return the individual
        if running_total >= r:
            return individual


# population = ['a', 'b']

# def fitness(x):
#     return 1 # everyone has the same fitness

# for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
#     print(roulette_wheel_select(population, fitness, r))

# population = [0, 1, 2]


# def fitness(x):
#     return x


# for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
#     print(roulette_wheel_select(population, fitness, r))

import math


def estimate(time, observations, k):
    # Compute distances as (distance, temperature)
    distances = [(abs(obs_time - time), temp) for obs_time, temp in observations]

    # Sort by distance
    distances.sort(key=lambda x: x[0])

    # If there are fewer than k observations, use all of them
    if k >= len(distances):
        return sum(temp for _, temp in distances) / len(distances)

    # Otherwise, take the first k
    selected = distances[:k]
    next_group = distances[k:]

    # Handle ties
    while next_group and next_group[0][0] == selected[-1][0]:
        selected.append(next_group.pop(0))

    # Average the selected temperatures
    return sum(temp for _, temp in selected) / len(selected)


# observations = [
#     (-1, 1),
#     (0, 0),
#     (-1, 1),
#     (5, 6),
#     (2, 0),
#     (2, 3),
# ]

# for time in [-1, 1, 3, 3.5, 6]:
#     print(estimate(time, observations, 2))


def select(population, error, max_error, r):
    total_fitness = sum(max_error - error(individual) for individual in population)
    running_total = 0
    for individual in population:
        indv_fitness = max_error - error(individual)
        running_total += indv_fitness / total_fitness
        if running_total >= r:
            return individual


population = ["a", "b"]


def error(x):
    return {"a": 14, "b": 12}[x]


# max_error = 15

# for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
#     print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.


def estimate(time, observations, k):
    distances = [
        (abs(x_time - time), temperature) for x_time, temperature in observations
    ]

    distances.sort(key=lambda x: x[0])

    selected = distances[:k]
    next_selection = distances[k:]

    # if k >= len(observations):
    #     return sum([])/

    while next_selection and selected[-1][0] == next_selection[0][0]:
        selected.append(next_selection.pop(0))

    return sum(pair[1] for pair in selected) / len(selected)


# observations = [
#     (-1, 1),
#     (0, 0),
#     (-1, 1),
#     (5, 6),
#     (2, 0),
#     (2, 3),
# ]

# for time in [-1, 1, 3, 3.5, 6]:
#     print(estimate(time, observations, 2))


from search import Graph, Arc, Frontier
import collections


class WordChainGraph(Graph):
    def __init__(self, words, start_words, goal):
        self.words = words
        self.start_words = start_words
        self.goal = goal

    def starting_nodes(self):
        return self.start_words

    def outgoing_arcs(self, state):
        arcs = []

        for word in self.words:
            if state[-1] == word[0] and state != word:
                arcs.append(Arc(tail=state, head=word, action=word, cost=1))

        return arcs

    def is_goal(self, state):
        return state == self.goal


class BFSFrontier(Frontier):
    def __init__(self):
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        # Dequeue and return the next path in FIFO order.
        # If empty, raise StopIteration.
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration


# 'level' can self-loop (l...l), but a shorter path exists to goal.
# words = ["ab", "ba", "level", "alps", "salt", "tuba"]
# start_words = ["ab"]
# goal = "tuba"

# graph = WordChainGraph(words, start_words, goal)
# solutions = generic_search(graph, BFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)

# words = ["owl", "lion", "newt", "tiger", "rat", "tar", "rhino", "eel", "goat"]
# start_words = ["owl"]
# goal = "rat"

# graph = WordChainGraph(words, start_words, goal)
# solutions = generic_search(graph, BFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)


# words = ["apple", "eel", "egg", "grape"]
# start_words = ["eel", "apple"]
# goal = "egg"

# # solution transition: apple -> egg

# graph = WordChainGraph(words, start_words, goal)
# solutions = generic_search(graph, BFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)

# words = ["cat", "dog", "ant"]
# start_words = ["dog"]
# goal = "cat"

# graph = WordChainGraph(words, start_words, goal)
# solutions = generic_search(graph, BFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)


def estimate(time, observations, k):
    distance = [
        (abs(x_time - time), temperature) for x_time, temperature in observations
    ]

    distance.sort(key=lambda x: x[0])

    selected = distance[:k]
    next_selected = distance[k:]

    if k >= len(observations):
        return sum(temperature for time, temperature in selected) / len(selected)

    while next_selected and selected[-1][0] == next_selected[0][0]:
        selected.append(next_selected.pop(0))

    return sum(temperature for time, temperature in selected) / len(selected)


# observations = [
#     (-1, 1),
#     (0, 0),
#     (-1, 1),
#     (5, 6),
#     (2, 0),
#     (2, 3),
# ]

# for time in [-1, 1, 3, 3.5, 6]:
#     print(estimate(time, observations, 2))


def select(population, error, max_error, r):
    total_fitness = sum(max_error - error(individual) for individual in population)
    running_total = 0
    for individual in population:
        indv_fitness = max_error - error(individual)
        running_total += indv_fitness / total_fitness
        if running_total >= r:
            return individual


# population = ["a", "b"]

# def error(x):
#     return {"a": 14, "b": 12}[x]

# max_error = 15

# for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
#     print(select(population, error, max_error, r))

# # since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# # for r's below 0.25 we get 'a', for r's above it we get 'b'.


def select(population, error, max_error, r):
    total_fitness = sum([max_error - error(individual) for individual in population])
    running_total = 0
    for individual in population:
        indv_fitness = max_error - error(individual)
        running_total += indv_fitness / total_fitness
        if running_total >= r:
            return individual


def estimate(time, observations, k):
    distance = [
        (abs(time - x_time), temperature) for x_time, temperature in observations
    ]

    distance.sort(key=lambda x: x[0])

    if k >= len(distance):
        return sum([time for time, temperature in distance]) / len(distance)

    selected = distance[:k]
    next_selected = distance[k:]

    while next_selected and selected[-1][0] == next_selected[0][0]:
        selected.append(next_selected.pop(0))

    return sum([temperature for time, temperature in selected]) / len(selected)


observations = [
    (-1, 1),
    (0, 0),
    (-1, 1),
    (5, 6),
    (2, 0),
    (2, 3),
]

for time in [-1, 1, 3, 3.5, 6]:
    print(estimate(time, observations, 2))


from search import *
import heapq
import itertools
import collections


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        # add more code if necessary
        self.counter = itertools.count()

    def add(self, path):
        counter = next(self.counter)
        total = sum([arc.cost for arc in path])

        heapq.heappush(self.container, (total, counter, path))

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            counter, total, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration  # don't change this one


def select(population, error, max_error, r):
    total_fitness = sum(max_error - error(individual) for individual in population)
    running_total = 0
    for individual in population:
        indv_fitnesss = max_error - error(individual)
        running_total+=indv_fitnesss/total_fitness
        if running_total>=r:
            return individual


def estimate(time, observations, k):
    distances = [(abs(x_time - time), temperature) for x_time, temperature in observations]

    distances.sort(key=lambda x: x[0])

    selected = distances[:k]
    next_selected = distances[k:]

    while selected and selected[-1][0] == next_selected[0][0]:
        selected.append(next_selected.pop(0))

    return sum(temperature for time, temperature in selected)/len(selected)
