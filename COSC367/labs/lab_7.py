import math

"""
A game tree is either a number that represents the utility (payoff) of a terminal (end-game) state or
A list of one or more game trees

The root of the following game tree has three children. 
The first child is a leaf node with a utility of 1. 
The second child has two children (leaf nodes with utilities 2 and 3). 
The third child of the root has a single child, which itself has a single child (a leaf node with a utility of 4).

game_tree = [1, [2, 3], [[4]]]
"""


def utility(state):
    """
    Gives numerical value of the terminal state
    """
    # print(f"Utility: {state}")
    return state


def terminal_test(state):
    """Is the game finished? True if state is a leaf, false otherwise"""
    # a leaf node is an integer
    # a non leaf node is a list containing one or more subtrees

    # if int then its a leaf, if list then its a subtree
    return isinstance(state, int)


def sucessors(state):
    """
    Similar to outgoing arcs.
    Returns a list of pairs of action-state(a, s) that can be reached from the given state
    """
    action_state = []
    for a, s in enumerate(state):
        action_state.append((a, s))
    return action_state


def max_value(tree):
    if terminal_test(tree):
        return utility(tree)
    v = -math.inf
    for a, s in sucessors(tree):
        v = max(v, min_value(s))
    return v


def min_value(tree):
    if terminal_test(tree):
        return utility(tree)
    v = math.inf
    for a, s in sucessors(tree):
        v = min(v, max_value(s))
    return v


# TODO: game_tree should receive the action and the state now? So that is why its failing when passing between functions
def max_action_value(game_tree):
    if terminal_test(game_tree):
        return None, utility(game_tree)
    action, v = None, -math.inf
    for a, s in sucessors(game_tree):
        min_a, min_v = min_action_value(s)
        if min_v > v:
            action, v = a, min_v
    return action, v


def min_action_value(game_tree):
    if terminal_test(game_tree):
        return None, utility(game_tree)
    action, v = None, math.inf
    for a, s in sucessors(game_tree):
        max_a, max_v = max_action_value(s)
        if max_v < v:
            action, v = a, max_v
    return action, v


# Q2 ---------------------------------------------------------------------------------------------------

# game_tree = [2, [-3, 1], 4, 1]
game_tree = [0, [-1, 1], [1, -1, 1]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


# game_tree = 3

# action, value = min_action_value(game_tree)
# print("Best action if playing min:", action)
# print("Best guaranteed utility:", value)
# print()
# action, value = max_action_value(game_tree)
# print("Best action if playing max:", action)
# print("Best guaranteed utility:", value)


# game_tree = [1, 2, [3]]

# action, value = min_action_value(game_tree)
# print("Best action if playing min:", action)
# print("Best guaranteed utility:", value)
# print()
# action, value = max_action_value(game_tree)
# print("Best action if playing max:", action)
# print("Best guaranteed utility:", value)

# Q1 ---------------------------------------------------------------------------------------------------

# game_tree = 3

# print("Root utility for minimiser:", min_value(game_tree))
# print("Root utility for maximiser:", max_value(game_tree))


# game_tree = [1, 2, 3]

# print("Root utility for minimiser:", min_value(game_tree))
# print("Root utility for maximiser:", max_value(game_tree))


# game_tree = [1, 2, [3]]

# print(min_value(game_tree))
# print(max_value(game_tree))

# game_tree = [2, [-3, 1], 4, 1]
# game_tree = [[1, 2], [3]]

# print(min_value(game_tree))
# print(max_value(game_tree))
