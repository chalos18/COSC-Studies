from COSC367.graph_search import Graph, Arc, Frontier, generic_search, print_actions


class NumberGameGraph(Graph):
    def __init__(self, number_sequence, target):
        # sequence is [2, 4, 5, 1]
        self.number_sequence = number_sequence
        # target = 29
        self.target = target

    def starting_nodes(self):
        return [(0, self.number_sequence[0])]

    def outgoing_arcs(self, state):
        index, value = state
        arcs = []

        # Note: the following expression constructs an arc:
        # Arc(state, (next_index, next_value), operator_str, 1)
        # The argument operator_str is one of '+', '-', or '*'.
        # print(index, value)
        if index + 1 < len(self.number_sequence):
            arcs.append(
                Arc(state, (index + 1, value + self.number_sequence[index + 1]), "+", 1)
            )
            arcs.append(
                Arc(state, (index + 1, value - self.number_sequence[index + 1]), "-", 1)
            )
            arcs.append(
                Arc(state, (index + 1, value * self.number_sequence[index + 1]), "*", 1)
            )

        return arcs

    def is_goal(self, state):
        index, value = state
        return value == self.target and index == len(self.number_sequence) - 1


class DFSFrontier(Frontier):

    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        "Complete"
        "If there is nothing to return raise the following exception."
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration("There is no solution!")  # dont change this one


# sequence = [2, 4, 5, 1]
# target = 29

# graph = NumberGameGraph(sequence, target)
# solutions = generic_search(graph, DFSFrontier())

# while solution := next(solutions, None):
#     print_actions(solution)
#     print()


# sequence = [1, 1, 1]
# target = 4

# graph = NumberGameGraph(sequence, target)
# solutions = generic_search(graph, DFSFrontier())

# solution = next(solutions, None)
# print_actions(solution)


sequence = [1, 1, 1]
target = 2

graph = NumberGameGraph(sequence, target)
solutions = generic_search(graph, DFSFrontier())

while solution := next(solutions, None):
    print_actions(solution)
    print()



