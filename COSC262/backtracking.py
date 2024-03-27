def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False


def is_solution(candidate, input_data):
    """Returns True if the candidate is a complete solution"""
    desired_length = len(input_data)
    return len(candidate) == desired_length


def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    # print(candidate)
    # print(input_data)

    diff = set(candidate) - input_data
    print(diff)
    return diff
    # if iterator not in candidate:
    #     return candidate.append(input_data[0])

    # return [candidate + "0", candidate + "1"]


print(sorted(permutations({1, 2, 3})))

# print(sorted(permutations({"a"})))

# perms = permutations(set())
# print(len(perms) == 0 or list(perms) == [()])
