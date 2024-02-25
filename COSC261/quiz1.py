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
# print(sorted(all_strings({0, 1}, 3)))
# print(sorted(all_strings({"a", "b"}, 2)))
# print(len(all_strings({"a", "b", "c"}, 2)))


# Python3 Program to DFA that accepts string ending
# with 01 or 10.


# End position is checked using the string
# length value.
# q0 is the starting state.
# q1 and q2 are intermediate states.
# q3 and q4 are final states.
def q1(s, i):

    print("q1->", end="")

    if i == len(s):
        print("NO")
        return

    # state transitions
    # 0 takes to q1, 1 takes to q3
    if s[i] == "0":
        q1(s, i + 1)
    else:
        q3(s, i + 1)


def q2(s, i):

    print("q2->", end="")
    if i == len(s):
        print("NO")
        return

    # state transitions
    # 0 takes to q4, 1 takes to q2
    if s[i] == "0":
        q4(s, i + 1)
    else:
        q2(s, i + 1)


def q3(s, i):

    print("q3->", end="")
    if i == len(s):
        print("YES")
        return

    # state transitions
    # 0 takes to q4, 1 takes to q2
    if s[i] == "0":
        q4(s, i + 1)
    else:
        q2(s, i + 1)


def q4(s, i):

    print("q4->", end="")
    if i == len(s):
        print("YES")
        return

    # state transitions
    # 0 takes to q1, 1 takes to q3
    if s[i] == "0":
        q1(s, i + 1)
    else:
        q3(s, i + 1)


def q0(s, i):

    print("q0->", end="")
    if i == len(s):
        print("NO")
        return

    # state transitions
    # 0 takes to q1, 1 takes to q2
    if s[i] == "0":
        q1(s, i + 1)
    else:
        q2(s, i + 1)


# Driver Code
if __name__ == "__main__":
    s = "101"

    # all state transitions are printed.
    # if string is accpetable, YES is printed.
    # else NO is printed
    print("State transitions are", end=" ")
    q0(s, 0)
