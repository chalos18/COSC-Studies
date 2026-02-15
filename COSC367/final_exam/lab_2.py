from search import Arc, Graph
from math import sqrt


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        x1, y1 = self.location[tail]
        arcs = []
        for position in self.location:
            if position != tail:
                head = self.location[position]
                x2, y2 = head
                euclid_dist = sqrt(((x2-x1)**2) + ((y2-y1)**2))
                if euclid_dist <= self.radius:
                    arcs.append(Arc(tail=tail, head=position, action=f"{tail}->{position}", cost=euclid_dist))
        return sorted(arcs)

from search import Frontier
import itertools
import heapq

class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = itertools.count()

    def add(self, path):
        counter = next(self.counter)
        total = sum(arc.cost for arc in path)
        heapq.heappush(self.container, (total, counter, path))

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


frontier = LCFSFrontier()
frontier.add((Arc(None, None, None, 17),))
frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

for path in frontier:
    print(path)
