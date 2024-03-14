def epsilon_closure(state, nfa, visited=None):
    """
    Returns a set of all the states in the epsilon closure of the given state of the given nfa with epsilon transitions
    """
    if visited is None:
        visited = set()  # Keep track of visited states to avoid infinite recursion

    closure = {state}  # Initialize the closure set with the current state

    # Mark the current state as visited
    visited.add(state)

    # Check for epsilon transitions
    if "_" in nfa[state]:
        for epsilon_state in nfa[state]["_"]:
            # If the epsilon transition leads to an unvisited state
            if epsilon_state not in visited:
                # Recursively find epsilon closure of the epsilon_state
                closure |= epsilon_closure(epsilon_state, nfa, visited)

    return closure


# Example usage:
nfa = {
    0: {"_": {1}, "a": {1, 2}, "b": {2}},
    1: {"_": {2}, "a": {1}, "b": {0}},
    2: {"a": {1}, "b": {2}},
}

# for i in range(3):
#     print(f"Epsilon closure for q{i}: {sorted(epsilon_closure(i, nfa))}")

# These epsilon transitions form a loop - be sure to keep track of where you've been!
loopy_nfa = {
    0: {"_": {1}, "a": {1}, "b": {2}},
    1: {"_": {2}, "a": {1}, "b": {0}},
    2: {"_": {0}, "a": {1}, "b": {2}},
}
# for i in range(3):
#     print(f"Epsilon closure for q{i}: {sorted(epsilon_closure(i, loopy_nfa))}")

# NFA with multiple epsilon transitions from the same state
multi_transition_nfa = {
    0: {"_": {2, 1}, "a": {1}, "b": {2}},
    1: {"a": {1}, "b": {0}},
    2: {"_": {3, 1}, "a": {1}, "b": {2}},
    3: {"a": {2}},
}
# for i in range(4):
    # print(
    #     f"Epsilon closure for q{i}: {sorted(epsilon_closure(i, multi_transition_nfa))}"
    # )
