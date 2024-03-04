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


# First attempt
def num_rushes(slope_height, rush_height_gain, back_sliding, counter=0):
    # this base case is bad because what if the slope height is the same as the rush height gain, then it should count as one rush
    # technically the slope height could also go below 0 according to the calculations made so this is a bad base case
    if slope_height == 0:
        return 1
    else:
        # counter adds unnecessary recursion depth, improve the base case instead
        if counter == 0:
            leftover_height = slope_height - rush_height_gain
            return 1 + num_rushes(
                slope_height=leftover_height,
                rush_height_gain=rush_height_gain,
                back_sliding=back_sliding,
                counter=counter + 1,
            )
        else:
            # correct calculation but could be made in less steps
            rush_slide = rush_height_gain - back_sliding
            slope_height = slope_height - rush_slide
            return 1 + num_rushes(
                slope_height=slope_height,
                rush_height_gain=rush_height_gain,
                back_sliding=back_sliding,
            )


# ans = num_rushes(100, 15, 7)
# print(ans)


def num_rushes(slope_height, rush_height_gain, back_sliding):
    if slope_height <= rush_height_gain:
        return 1
    else:
        return 1 + num_rushes(
            slope_height - rush_height_gain + back_sliding,
            rush_height_gain,
            back_sliding,
        )


# # Test cases
# ans = num_rushes(10, 10, 9)
# print(ans)  # Output: 1

# ans = num_rushes(100, 10, 0)
# print(ans)  # Output: 10

# ans = num_rushes(100, 15, 7)
# print(ans)


# Num rushes with reduction
# def num_rushes(slope_height, rush_height_gain, back_sliding, reduction=0):
#     if slope_height <= rush_height_gain:
#         return 1
#     else:
#         if reduction == 0:
#             return 1 + num_rushes(
#                 slope_height - rush_height_gain + back_sliding,
#                 rush_height_gain,
#                 back_sliding,
#                 reduction=reduction + 0.95,
#             )
#         else:
#             if reduction <= 0.9025:
#                 return 1 + num_rushes(
#                     slope_height
#                     - rush_height_gain * reduction
#                     + back_sliding * reduction,
#                     rush_height_gain,
#                     back_sliding,
#                     reduction=reduction,
#                 )
#             else:
#                 return 1 + num_rushes(
#                     slope_height
#                     - rush_height_gain * reduction
#                     + back_sliding * reduction,
#                     rush_height_gain,
#                     back_sliding,
#                     reduction=reduction,
#                 )


def num_rushes(slope_height, rush_height_gain, back_sliding, reduction=0.95):
    if slope_height <= rush_height_gain:
        return 1
    else:
        return 1 + num_rushes(
            slope_height - rush_height_gain + back_sliding,
            rush_height_gain * 0.95,
            back_sliding * 0.95,
            reduction=reduction * 0.95,
        )


# ans = num_rushes(100, 15, 7)
# print(ans)

# ans = num_rushes(10, 10, 9)
# print(ans)


# ans = num_rushes(150, 20, 9)
# print(ans)

# ans = num_rushes(113, 11, 0)
# print(ans)


NUM_RMDS = 9  # number of right-most digits required


def multiply2by2(A, B):
    """Takes two 2-by-2 matrices, A and B, and returns their product. The
    product will only contain a limited number of digits to cope with
    large numbers.  The input and output matrices are in the form of
    lists of lists (of lengths 2). This function only works for 2-by-2
    matrices. The size (dimensions) of the input does not grow with
    respect to n in the original problem. Therefore the time
    complexity of this function is Theta(1). This is different from
    the general matrix multiplication problem where the time
    complexity for multiplying two n-by-n matrices is O(n^3).

    """

    # compute the matrix product
    product = [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]

    # retain only the required number of digits on the right
    product = [[x % 10**NUM_RMDS for x in row] for row in product]

    return product


def matrix_power(A, n):
    """Takes a 2x2 matrix A and a non-negative integer n as exponent and
    returns A raised to the power of n (which will be a 2x2 matrix)."""

    # if n is 0 then return the identity matrix.
    if n == 0:
        return [[1, 0], [0, 1]]
    else:
        p = matrix_power(A, n // 2)
        if n % 2 == 0:
            return multiply2by2(p, p)
        else:
            return multiply2by2(A, multiply2by2(p, p))


def fib(n):
    """Returns the n-th Fibonacci number by raising a special matrix to the
    power of n and returning an element on the off-diagonal."""

    A = [[1, 1], [1, 0]]

    return matrix_power(A, n)[0][1]


# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(100))


"""
# Merge Sort pseudocode

procedure Merge-Sort(A,l,r)
if l<r
    m  ← (l+r)/2
    Merge-Sort(A,l,m)
    Merge-Sort(A,m+1,r)
    Merge(A,l,m,r)
"""

# Make the below, recursive
# def all_pairs(list1, list2):
#     tuples = []
#     for list1_el in list1:
#         for list2_el in list2:
#             tuples.append((list1_el, list2_el))
#     return tuples


def all_pairs_inner(list2, start_index=0):
    if start_index >= len(list2):
        return []
    else:
        iterator = list2[start_index]
        remaining = all_pairs_inner(list2, start_index + 1)
        return [iterator] + remaining
        # return [iterator].append(all_pairs_inner(list2, start_index + 1))


# print(all_pairs_inner([10, 20, 30]))


def all_pairs(list1, list2, start_index = 0):
    # if start_index >= len(list1):
    #     return []
    # else:
    #     iterator = list1[start_index]
    #     remaining = all_pairs_inner(list1, start_index + 1)
    pairs = []
    for list1_el in list1:
        list2_pairs = all_pairs_inner(list2)
        for pair in list2_pairs:
            pairs.append((list1_el, pair))
    return pairs


# print(all_pairs([1, 2], [10, 20, 30]))


def generate_pairs_for_element(list1_el, list2):
    if not list2:
        return []
    else:
        pair = (list1_el, list2[0])
        remaining_pairs = generate_pairs_for_element(list1_el, list2[1:])
        return [pair] + remaining_pairs


def all_pairs(list1, list2):
    if not list1:
        return []
    else:
        list1_el = list1[0]
        pairs_with_list1_el = generate_pairs_for_element(list1_el, list2)
        remaining_pairs = all_pairs(list1[1:], list2)
        return pairs_with_list1_el + remaining_pairs

# Test the function
# print(all_pairs([1, 2], [10, 20, 30]))
