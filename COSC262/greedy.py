from algorithms import *
from tests import *


def change_greedy(amount, coinage):
    """
    amount -> money in some units 'cents'
    coinage -> list of integer coin values (in an arbitrary order)
    returns the breakdown of that amount into coins as obtained by the greedy algorithm
    The return value is a list of (coin_count, coin_value) tuples sorted in descending order of coin_value,
    including only cases where coin_count is greater than zero.

    If an exact breakdown is not achieved using the greedy algorithm, return None
    """
    defaultdict = {}
    for coin in coinage:
        if coin not in defaultdict:
            defaultdict[coin] = 0

    while amount > 0:
        coin_max = 0
        for coin in defaultdict:
            if coin > coin_max and coin <= amount:
                coin_max = coin
        if coin_max not in defaultdict:
            return None
        defaultdict[coin_max] += 1
        amount = amount - coin_max

    dict_tuple = [(k, v) for k, v in defaultdict.items() if v > 0]
    dict_tuple.sort(reverse=True)
    right_order = [(v, k) for k, v in dict_tuple]

    return right_order


# [(3, 25), (1, 5), (2, 1)]
# print(change_greedy(82, [1, 10, 25, 5]))
# [(3, 25), (5, 1)]
# print(change_greedy(80, [1, 10, 25]))
# None
# print(change_greedy(82, [10, 25, 5]))


def buskers_schedule(show_list):
    """
    Takes a list of show tuples and returns a list of tuples
    Each tuple contains a title, the start time and the end of a show. Order the  tuples by start time.

    """
    calculate_show_list = []
    for k, j, v in show_list:
        calculate_show_list.append((k, j, j + v))

    sorted_show_list = sorted(calculate_show_list)
    S = []
    t_current = 0
    show_list_len = len(sorted_show_list)
    for j in range(show_list_len):
        if sorted_show_list[j][1] >= t_current:
            S.append(sorted_show_list[j])
            t_current = sorted_show_list[j][2]
    return sorted(S)


# [('b', 1, 4), ('e', 4, 7), ('h', 8, 11)]
print(
    buskers_schedule(
        [
            ("a", 0, 6),
            ("b", 1, 3),
            ("c", 3, 2),
            ("d", 3, 5),
            ("e", 4, 3),
            ("f", 5, 4),
            ("g", 6, 4),
            ("h", 8, 3),
        ]
    )
)
