def sequence_length(n):
    """Computes the Collatz sequence length of a given positive integer
    The Collatz sequence-length of n is the number of numbers generated in the Collatz
    sequence starting from n up to 1(including n and 1)
    """
    # Take any natural number n
    # if n is even, divide by 2 to get n/2
    # If n is odd, multiply by 3 and add 1 to obtain 3n + 1
    # No matter what number you start with you will always eventuallly reach 1
    if n == 1:
        return 1  # Return 1 when n is 1, as it's the only element in the sequence
    else:
        if n % 2 == 0:
            return 1 + sequence_length(n // 2)  # Recursively call sequence_length
        else:
            return 1 + sequence_length(3 * n + 1)  # Recursively call sequence_length


# print(sequence_length(22))


def recursive_divide(x, y):
    """
    recursive function that performs division without operators (/ % * //) or any types of loops
    """
    if x == 0 or x < y:
        return 0
    else:
        # e.g 8-2 = 6
        x = x - y
        # (6, 2)
        if x >= y:
            return 1 + recursive_divide(x, y)
        else:
            return 1


# print(recursive_divide(5, 10))


# Starting-index base
def recursive_sum(data, start_index=0):
    """The sum of the elements in the list data, starting
    at the given start_index
    """
    if start_index >= len(data):
        return 0
    else:
        return data[start_index] + recursive_sum(data, start_index + 1)


# Length base
def recursive_sum(data, n=None):
    """The sum of the first n elements of data (default to all)"""
    if n is None:
        n = len(data)
    if n == 0:
        return 0
    else:
        return recursive_sum(data, n - 1) + data[n - 1]


# Make the function below O(n) instead of O(n**2) -- Done
import sys

sys.setrecursionlimit(100000)


def dumbo_func(data, start_index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if start_index >= len(data):
        return 0
    else:
        if (data[start_index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, start_index + 1)
        else:
            return dumbo_func(data, start_index + 1)


# Simple test with short list.
# Original func works fine on this
# data = [677, 90, 785, 875, 7, 90393, 10707]
# print(dumbo_func(data))


def my_enumerate(items, start_index=0):
    """
    Return a list of tuples(i, item)
    item is the ith item, with a 0 origin, of the list items
    """
    if start_index >= len(items):
        return []
    else:
        # iterator = items[start_index]
        # remaining = my_enumerate(items, start_index + 1)
        # remaining.append((start_index, iterator))
        # return remaining

        # For the above, it almost worked but using append modififes the initial list and appends None to it
        # Instead use concatenation or list comprehension
        iterator = items[start_index]
        remaining = my_enumerate(items, start_index + 1)
        return [(start_index, iterator)] + remaining


# ans = my_enumerate([10, 20, 30])
# print(ans)


def num_rushes(slope_height, rush_height_gain, back_sliding):
    if slope_height == 0:
        return 0
    else:
        rushes = 0
        if rushes == 0:
            leftover_height = slope_height - rush_height_gain
            rushes+=1
        else:


        rush = rush_height_gain - back_sliding
        n_rushes = slope_height // rush
        return n_rushes, rush


ans = num_rushes(100, 10, 9)
print(ans)
