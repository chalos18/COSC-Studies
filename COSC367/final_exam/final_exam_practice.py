from search import *
import heapq
import itertools


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = itertools.count()

    def add(self, path):
        total_cost = sum(arc.cost for arc in path)
        counter = next(self.counter)

        heapq.heappush(self.container, (total_cost, counter, path))

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            _, _, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration  # don't change this one


from search import *

graph = ExplicitGraph(
    nodes={"S", "A", "B", "G"},
    edge_list=[
        ("S", "A", 3),
        ("S", "B", 1),
        ("B", "A", 1),
        ("A", "B", 1),
        ("A", "G", 5),
    ],
    starting_nodes=["S"],
    goal_nodes={"G"},
)

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

import itertools
import heapq
import collections

class DFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

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

import heapq
import itertools
import collections

class BFSFrontier(Frontier):
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

