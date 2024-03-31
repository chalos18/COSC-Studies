import operator
from algorithms import *


def sorted_array(seq, key, positions):
    seq_len = len(seq)
    B = [0 for i in range(seq_len)]
    for a in seq:
        B[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] + 1
    return B


# [1, 2, 3]
# print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))

# [1, 2, 2, 2, 3]
# print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))

# [100]
# print(sorted_array([100], lambda x: x, [0] * 101))


def key_positions(seq, key):
    k = max(list(map(key, seq)))
    C = [0 for i in range(k + 1)]
    for i in range(0, k + 1):
        C[i] = 0
    for a in seq:
        C[key(a)] = C[key(a)] + 1
    sums = 0
    for i in range(0, k + 1):
        C[i], sums = sums, sums + C[i]
    return C


# [0, 1, 2]
# print(key_positions([0, 1, 2], lambda x: x))
# [0, 1, 3, 3, 3, 5, 5, 5, 5, 5]
# print(key_positions(range(-3, 3), lambda x: x**2))

# print(max((lambda x: x**2)(([-3, -2, -1, 0, 1, 2]))))


def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)


"""Counting Sort"""
# d, b, c, a

objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
# print(", ".join(object[0] for object in counting_sort(objects, key)))


def radix_key(d):
    def get_digit(number):
        # Convert the number to a string representation
        number_str = str(number)

        # Check if the length of the number is greater than or equal to d
        if len(number_str) >= d:
            # Extract the d-th digit from the end of the number string
            digit = int(number_str[-d])
        else:
            # If the length of the number is less than d, return 0
            digit = 0
        return digit

    # Return the inner function
    return get_digit


# number = 132
# ones = radix_key(1)
# print(ones(number))
# tens = radix_key(2)
# print(tens(number))
# hundreds = radix_key(3)
# print(hundreds(number))


# numbers = [1, 10, 100]
# ones = radix_key(1)
# for number in numbers:
#     print(ones(number))


# numbers = [1, 10, 100]
# tens = radix_key(2)
# for number in numbers:
#     print(tens(number))


def radix_sort(numbers, d):
    # Corrected the range to include the most significant digit
    for i in range(1, d + 1):
        # Extract current digit
        numbers = counting_sort(numbers, lambda x, i=i: (x // 10 ** (i - 1)) % 10)
    return numbers


input_list = [329, 457, 657, 839, 436, 720, 355]
output_list = radix_sort(input_list, 3)
# print(input_list)
# print(output_list)

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
