def concatenate_list(strings):
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concatenate_list(strings[1:])


# result = concatenate_list(["a", "b", "c", "d"])
# print(result)


def product(data):
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])


# result = product([1, 13, 9, -11])
# print(result)


def backwards(s):
    if len(s) == 0:
        return ""
    else:
        return backwards(s[1:]) + s[0]


# result = backwards("Hi there!")
# print(result)


def odd(data):
    even = []
    odds = []
    for n in data:
        if n % 2 == 0:
            even.append(n)
        else:
            odds.append(n)
    return odds


# result = odd([1, 2, 3, 4, 5, 6, 7, 8])
# print(result)


# Attempt
def odds(data):
    if len(data) == 0:
        return []
    else:
        first = data[0]
        # the return value of the call is not actually getting saved anywhere
        # recursive calls need to capture their return values for further processing
        odds(data[1:])
        if first % 2 != 0:
            # cant return here, it stops at the first odd number in this case
            # it has to finish iterating through the whole list
            # the recursive call is already above, this should check for the 'first' item now
            # the append method modifies the list in place and returns None instead of returning the modified list
            return odds(data[0]).append(data[0])


# Answer
def odds(data):
    if len(data) == 0:
        return []
    else:
        first = data[0]
        remaining = odds(data[1:])
        if first % 2 != 0:
            remaining.insert(0, first)
        return remaining


# result = odds([0, 1, 12, 13, 14, 9, -11, -20])
# print(result)


def squares(data):
    if len(data) == 0:
        return []
    else:
        first = data[0]
        remaining = squares(data[1:])
        remaining.insert(0, first**2)
        return remaining


# result = squares([1, 13, 9, -11])
# print(result)


def find(data, value):
    if len(data) == 0:
        return None
    else:
        first = data[0]
        remaining = find(data[1:], value)
        if first == value:
            remaining = 1
        return remaining


def find(data, value):
    """Returns the subscript (position) of the first occurrence of value in data, or None if the value is not found"""
    if not data:
        return None
    elif data[0] == value:
        return 0
    else:
        found = find(data[1:], value)
        if found is None:
            return None
        else:
            return found + 1


# print(find(["hi", "there", "you", "there"], "there"))
# print(find([10, 20, 30], 0))
# print(find([10, 20, 30], 30))
# print(find(list(range(0, 51)), 49))

# def almost_all(numbers):
#     for x in numbers:
#         return [sum(numbers) - x]


def almost_all(numbers):
    total_sum = sum(numbers)

    # Initialize an empty list to store the results
    result = []
    # Iterate through each number in the list
    for x in numbers:
        # Subtract the current number from the total sum and append the result to the result list
        result.append(total_sum - x)

    # Return the result list
    return result


def recursive_sum(data, start_index=0):
    """The sum of the elements in the list data, starting
    at the given start_index
    """
    if start_index >= len(data):
        return 0
    else:
        return data[start_index] + recursive_sum(data, start_index + 1)


# print(almost_all([1, 2, 3]))
# print(almost_all(list(range(10**5))))
