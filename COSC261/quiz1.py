def all_strings_01(alpha, length):
    """
    Returns a list containing all strings of the given length over the alphabet alpha
    """
    patterns = []
    length_of_alpha = len(alpha)
    combinations = length_of_alpha**length
    print(combinations)

    for n in alpha:
        patterns.append(f"{n}" * length)
        for j in alpha:
            pattern = f"{j}" + f"{n}" * length
            if pattern not in patterns:
                patterns.append(pattern)
            else:
                patterns.append(pattern)

    return patterns

def all_strings_recursively(alpha, length):
    if length == 0:
        return [""]
    else:
        strings = []
        for symbol in alpha:
            for string in all_strings_recursively(alpha, length - 1):
                strings.append(str(symbol) + string)
        return strings


# Example usage:
# print(sorted(all_strings_recursively({0, 1}, 3)))
# print(sorted(all_strings_recursively({"a", "b"}, 2)))
# print(len(all_strings_recursively({"a", "b", "c"}, 2)))


def all_strings(alpha, length):
    if length == 0:
        return [""]

    result = [""]
    for _ in range(length):
        new_result = []
        for string in result:
            for symbol in alpha:
                new_string = string + str(symbol)
                print(new_string)
                new_result.append(new_string)
        result = new_result

    return result


# Example usage:
print(sorted(all_strings({0, 1}, 3)))
print(sorted(all_strings({"a", "b"}, 2)))
print(len(all_strings({"a", "b", "c"}, 2)))
