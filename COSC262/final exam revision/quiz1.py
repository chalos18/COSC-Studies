def concat_list(strings):
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concat_list(strings[1:])


# ans = concat_list(["a", "hot", "day"])
# print(ans)

# ans = concat_list(["x", "y", "z"])
# print(ans)

# print(concat_list([]))


def product(data):
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])


# print(product([1, 13, 9, -11]))


def backwards(s):
    if len(s) == 0:
        return ""
    else:
        return backwards(s[1:]) + s[0]


# print(backwards("Hi there!"))


def odds(data):
    if len(data) == 0:
        return []
    else:
        num = data[0]
        remaining = odds(data[1:])
        if num % 2 != 0:
            remaining.insert(0, num)
        return remaining


# print(odds([0, 1, 12, 13, 14, 9, -11, -20]))


def squares(data):
    if len(data) == 0:
        return []
    else:
        num = data[0]
        remaining = squares(data[1:])
        remaining.insert(0, num**2)
        return remaining


# print(squares([1, 13, 9, -11]))


def find(data, value):
    if len(data) == 0:
        return None
    elif data[0] == value:
        return 0
    else:
        first_occurence = find(data[1:], value)
        if first_occurence is None:
            return None
        else:
            return first_occurence + 1


# print(find(["hi", "there", "you", "there"], "there"))
# print(find([10, 20, 30], 0))


def sequence_length(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return sequence_length(n // 2) + 1
        else:
            return sequence_length((n * 3) + 1) + 1


# print(sequence_length(22))
# print(sequence_length(1))


def recursive_divide(x, y):
    if x == 0 or x < y:
        return 0
    else:
        x = x - y
        if x >= y:
            return recursive_divide(x, y) + 1
        else:
            return 1


# print(recursive_divide(8, 3))

import sys

sys.setrecursionlimit(100000)


def dumbo_func(data, index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if index >= len(data):
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, index + 1)
        else:
            return dumbo_func(data, index + 1)


# Simple test with short list.
# Original func works fine on this
data = [677, 90, 785, 875, 7, 90393, 10707]
# print(dumbo_func(data))


def my_enumerate(items, index=0):
    if index >= len(items):
        return []
    else:
        current_number = items[index]
        remaining = my_enumerate(items, index + 1)
        remaining.insert(0, (index, current_number))
        return remaining


ans = my_enumerate([10, 20, 30])
# print(ans)


def all_pairs_inner(list1, list2, index=0):
    if index >= len(list2):
        return []
    else:
        iterator = list2[index]
        return [()] + all_pairs_inner(list1[index], list2, index + 1)

def all_pairs_outer(list1, list2, index = 0):
    if index >= len(list2):
        return []
    else:
        all_pairs_inner()

print(all_pairs_outer([1, 2], [10, 20, 30]))
