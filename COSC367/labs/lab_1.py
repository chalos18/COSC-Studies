import collections
from itertools import dropwhile
from COSC367.graph_search import *
import copy


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

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
        """Selects, removes, and returns a path on the frontier if there is
        any. Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration # dont change this one 


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first 
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

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
            return self.container.popleft()
        else:
            raise StopIteration  # dont change this one

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs(always two arcs in this problem)"""
        return [Arc(tail_node, tail_node-1, action="1down", cost=1), 
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
    
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the sequence always has one element."""
        return [self.starting_number]
    
    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0


BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state) # the size of the puzzle

        # Find i and j such that state[i][j] == BLANK
        i, j = next((r,c) for r, row in enumerate(state) for c, val in enumerate(row) if val == BLANK)

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            # COMPLETE (repeat the same pattern with some modifications)
            action = "Move {} left".format(state[i][j+1])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""

        size = len(state)
        goal = []
        count = 1
        for r in range(size):
            row = []
            for c in range(size):
                if r == 0 and c == 0:
                    row.append(' ')
                else:
                    row.append(count)
                    count += 1
            goal.append(row)
        return state == goal


def main():
    # --------------------  SlidingPuzzleGraph tests ------------------------
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, ' ']])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    # graph = SlidingPuzzleGraph([[3,' '],
    #                         [1, 2]])

    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))

    # graph = SlidingPuzzleGraph([[1, ' ', 2],
    #                         [6,  4,  3],
    #                         [7,  8,  5]])

    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))
    # --------------------  FunkyNumericGraph tests ------------------------
    # graph = FunkyNumericGraph(4)
    # for node in graph.starting_nodes():
    #     print(node)

    # graph = FunkyNumericGraph(4)
    # for arc in graph.outgoing_arcs(7):
    #     print(arc)

    # graph = FunkyNumericGraph(3)
    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))
    # print()
    # print_actions(next(solutions))

    # graph = FunkyNumericGraph(3)
    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))
# --------------------  DFS tests ------------------------
# # Example 1:
# graph = ExplicitGraph(
#     nodes=set("SAG"),
#     edge_list=[("S", "A"), ("S", "G"), ("A", "G")],
#     starting_nodes=["S"],
#     goal_nodes={"G"},
# )
# solutions = generic_search(
#     graph, DFSFrontier()
# )  # Creates a generator object, no search has happened yet
# # This means:
# # Run the generic_search function until it yields the first solution,
# # or return None if nothing is found
# # This means we are only getting one solution path here, not all solutions
# solution = next(solutions, None)  # Starts the search, runs until first 'yield path'
# print_actions(solution)           # Displays the solution
# # expected:
# # Actions:
# #   S->G.
# # Total cost: 1

# # Example 2
# graph = ExplicitGraph(
#     nodes=set("SAG"),
#     edge_list=[("S", "G"), ("S", "A"), ("A", "G")],
#     starting_nodes=["S"],
#     goal_nodes={"G"},
# )
# solutions = generic_search(graph, DFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)
# # expected:
# # Actions:
# #   S->A,
# #   A->G.
# # Total cost: 2

# available_flights = ExplicitGraph(
#     nodes=["Christchurch", "Auckland", "Wellington", "Gold Coast"],
#     edge_list=[
#         ("Christchurch", "Gold Coast"),
#         ("Christchurch", "Auckland"),
#         ("Christchurch", "Wellington"),
#         ("Wellington", "Gold Coast"),
#         ("Wellington", "Auckland"),
#         ("Auckland", "Gold Coast"),
#     ],
#     starting_nodes=["Christchurch"],
#     goal_nodes={"Gold Coast"},
# )

# my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
# print_actions(my_itinerary)

# --------------------  BFS tests ------------------------
# graph = ExplicitGraph(
#     nodes=set("SAG"),
#     edge_list=[("S", "A"), ("S", "G"), ("A", "G")],
#     starting_nodes=["S"],
#     goal_nodes={"G"},
# )

# solutions = generic_search(graph, BFSFrontier())
# solution = next(solutions, None)
# print_actions(solution)

# flights = ExplicitGraph(
#     nodes=["Christchurch", "Auckland", "Wellington", "Gold Coast"],
#     edge_list=[
#         ("Christchurch", "Gold Coast"),
#         ("Christchurch", "Auckland"),
#         ("Christchurch", "Wellington"),
#         ("Wellington", "Gold Coast"),
#         ("Wellington", "Auckland"),
#         ("Auckland", "Gold Coast"),
#     ],
#     starting_nodes=["Christchurch"],
#     goal_nodes={"Gold Coast"},
# )

# my_itinerary = next(generic_search(flights, BFSFrontier()), None)
# print_actions(my_itinerary)

    """Python's if __name__ == "__main__" idiom is used when code should be 
    executed only when a file is run as a script rather than imported as a module
    This ensures that what is in main isnot called by the module code and not
    executed when the module is imported
    """
if __name__ == "__main__": 
    main()
