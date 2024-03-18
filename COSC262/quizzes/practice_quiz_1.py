def concat_list(strings):
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concat_list(strings[1:])


# ans = concat_list(['a', 'hot', 'day'])
# print(ans)

# ans = concat_list(['x', 'y', 'z'])
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
        first = data[0]
        remaining = odds(data[1:])
        if first % 2 != 0:
            remaining.insert(0, first)
        return remaining

print(odds([0, 1, 12, 13, 14, 9, -11, -20]))
