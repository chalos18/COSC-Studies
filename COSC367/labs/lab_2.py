import itertools
from COSC367.graph_search import Arc, ExplicitGraph, Frontier, Graph, generic_search, print_actions
from math import sqrt
import heapq

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location  # the key are strings representing the nodes of the graphs 'A': (0 x, 0 y)
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        """
        Outgoing arcs to all other nodes that lie within the given radius
        The action field of each arc should be of the form "A->B", where A is the tail node and B is the head node.
        The cost of each arc should be the straigh line (euclidean) distance between the two nodes
        The outgoing arcs from each node must be sorted alphabetically by the head node's name
        """
        # on a 2D plane, two points are within a radius of each other if (and only if)
        # the Euclidean distance between them is less than or equal to r

        # Euclidean distance in 2D is D = (( x2 − x1 )**2 + ( y2 − y1 )**2) ** 0.5

        coordinates2 = self.location[tail]

        arcs = []
        for node, coordinates in self.location.items():
            if node == tail:
                continue
            # x1, y1 = tail x,y
            euclidean_distance = (
                (coordinates[0] - coordinates2[0]) ** 2
                + (coordinates[1] - coordinates2[1]) ** 2
            ) ** 0.5
            if euclidean_distance <= self.radius:
                arcs.append(
                    Arc(tail, node, str(tail) + "->" + str(node), euclidean_distance)
                )
        return sorted(arcs)


class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for LCFS search"""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = itertools.count()

    def add(self, path):
        total_cost = sum(arc.cost for arc in path)
        count = next(self.counter)
        # "A solution to the first two challenges is to store entries as 3-element list 
        # including the priority, an entry count, and the task"
        heapq.heappush(self.container, (total_cost, count, path))

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.container) > 0:
            _, _, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration # dont change this one 


def main():
    frontier = LCFSFrontier()
    frontier.add((Arc(None, None, None, 17),))
    frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

    for path in frontier:
        print(path)

    # ---------------------------------------------------------
    graph = LocationGraph(
    location={'A': (25, 7),
              'B': (1, 7),
              'C': (13, 2),
              'D': (37, 2)},
    radius=15,
    starting_nodes=['B'],
    goal_nodes={'D'}
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    # ---------------------------------------------------------
    graph = ExplicitGraph(
        nodes=set("ABCD"),
        edge_list=[("A", "D", 7), ("A", "B", 2), ("B", "C", 3), ("C", "D", 1)],
        starting_nodes=["A"],
        goal_nodes={"D"},
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
# ---------------------------------------------------------
# graph = LocationGraph(
#     location={
#         "A": (0, 0),
#         "B": (3, 0),
#         "C": (3, 4),
#         "D": (7, 0),
#     },
#     radius=5,
#     starting_nodes=["A"],
#     goal_nodes={"C"},
# )

# for node in graph.starting_nodes():
#     print(node)

# print()

# for arc in graph.outgoing_arcs("A"):
#     print(arc)

# print()

# for arc in graph.outgoing_arcs("B"):
#     print(arc)

# print()

# for arc in graph.outgoing_arcs("C"):
#     print(arc)

# ---------------------------------------------------------

# graph = LocationGraph(
#     location={"SW": (-2, -2), "NW": (-2, 2), "NE": (2, 2), "SE": (2, -2)},
#     radius=5,
#     starting_nodes=["NE"],
#     goal_nodes={"SW"},
# )

# for arc in graph.outgoing_arcs("NE"):
#     print(arc)

# print()

# for arc in graph.outgoing_arcs("NW"):
#     print(arc)

# print()

# for arc in graph.outgoing_arcs("SW"):
#     print(arc)

# print()

# for arc in graph.outgoing_arcs("SE"):
#     print(arc)


if __name__ == "__main__":
    main()
