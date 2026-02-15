from COSC367.graph_search import Frontier, generic_search, print_actions

import collections
import heapq
import itertools


class DFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        "If there is nothing to return raise the following exception."
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration


class BFSFrontier(Frontier):
    def __init__(self):
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        "If there is nothing to return raise the following exception."
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration


class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []
        self.counter = itertools.count()

    def add(self, path):
        """
            LCFS requires the heap to stay balanced,
            so it has to uses a counter to identify the order in which items are added,
            it removes however the node with the least cost
        """
        total_cost = sum(arc.cost for arc in path)
        count = next(self.counter)

        heapq.heappush(self.container, (total_cost, count, path))

    def __iter__(self):
        return self

    def __next__(self):
        "If there is nothing to return raise the following exception."
        if len(self.container) > 0:
            return heapq.heappop(self.container)
        raise StopIteration


class AStarFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        """
            Whereas LCFS uses a counter to stabilise the queue
            A Start Frontier depends on some sort of priority system to be able
            to stabilise it, this usually involves a heuristic function to 
            estimate the cost from the last node to the head to add to the total cost of the path        
        """
        total_cost = sum(arc.cost for arc in path)
        head = path[-1].head

        # last_node_estimate = estimated_cost_to_goal(head)
        # priority = total_cost + last_node_estimate

        # heapq.heappush(self.container, (priority, path))

    def __iter__(self):
        return self

    def __next__(self):
        "If there is nothing to return raise the following exception."
        if len(self.container) > 0:
            return heapq.heappop(self.container)
        raise StopIteration


from COSC367.graph_search import Graph, Arc, Frontier


class NumberGameGraph(Graph):
    def __init__(self, number_sequence, target):
        self.number_sequence = number_sequence
        self.target = target

    def starting_nodes(self):
        return [(0, self.number_sequence[0])]

    def outgoing_arcs(self, state):
        index, value = state
        arcs = []

        # Note: the following expression constructs an arc:
        # Arc(state, (next_index, next_value), operator_str, 1)
        # The argument operator_str is one of '+', '-', or '*'.
        if index + 1 < len(self.number_sequence):
            arcs.append(Arc(state, (index + 1, value + self.number_sequence[index + 1]), "+", 1))
            arcs.append(Arc(state, (index + 1, value - self.number_sequence[index + 1]), "-", 1))
            arcs.append(Arc(state, (index + 1, value * self.number_sequence[index + 1]), "*", 1))

        return arcs

    def is_goal(self, state):
        index, value = state
        return value == self.target and index == len(self.number_sequence) -1


class DFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        "Complete"
        "If there is nothing to rturen raise the following exception."
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration


sequence = [2, 4, 5, 1]
target = 29

graph = NumberGameGraph(sequence, target)
solutions = generic_search(graph, DFSFrontier())

while solution := next(solutions, None):
    print_actions(solution)
    print()
