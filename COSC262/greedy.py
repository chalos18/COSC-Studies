from datetime import datetime
from algorithms import *
from tests import *
import csv


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


def buskers_schedule_attempt(show_list):
    """
    Takes a list of show tuples and returns a list of tuples
    Each tuple contains a title, the start time and the end of a show. Order the  tuples by start time.

    """
    calculate_show_list = []
    for k, j, v in show_list:
        calculate_show_list.append((k, j, j + v))

    # The below does not sort by finish time
    sorted_show_list = sorted(calculate_show_list)
    print(sorted_show_list)
    S = []
    t_current = 0
    show_list_len = len(sorted_show_list)
    for j in range(show_list_len):
        if sorted_show_list[j][1] >= t_current:
            S.append(sorted_show_list[j])
            t_current = sorted_show_list[j][2]
    return sorted(S)


def buskers_schedule(show_list):
    calculate_show_list = []
    for k, j, v in show_list:
        calculate_show_list.append((k, j, j + v))

    sorted_show_list = sorted(
        calculate_show_list, key=lambda x: x[2]
    )  # Sort by end time
    S = []
    t_current = 0
    for show in sorted_show_list:
        if show[1] >= t_current:
            S.append(show)
            t_current = show[2]
    return S


def process_csv(file_path):
    data = []
    with open(file_path, "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip the header row if needed
        next(csv_reader, None)
        for row in csv_reader:
            # Process each row into a tuple and append it to the data list
            processed_row = (
                int(row[0]),  # Assuming the first column is an integer ID
                row[1],  # Name
                row[2],  # Start Time
                row[3],  # Duration
            )
            data.append(processed_row)
    return data


file_path = "intervalscheduling.csv"  # Replace with the actual path to your CSV file
data = process_csv(file_path)


def convert_time_to_minutes(time_str):
    """Converts time string in 'hh:mm:ss' format to minutes."""
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 60 + time_obj.minute + time_obj.second / 60


data = [
    (27, "11:15:00", "00:17:00"),
    (3, "09:11:00", "00:25:00"),
    (11, "11:18:00", "00:44:00"),
    (19, "09:20:00", "00:10:00"),
    (6, "13:24:00", "00:06:00"),
    (103, "11:02:00", "00:20:00"),
    (24, "12:42:00", "01:50:00"),
    (81, "10:29:00", "00:54:00"),
    (93, "12:04:00", "00:32:00"),
    (159, "14:40:00", "00:16:00"),
    (77, "15:15:00", "00:09:00"),
    (92, "11:58:00", "00:31:00"),
    (15, "14:50:00", "00:23:00"),
    (16, "09:31:00", "00:15:00"),
    (5, "15:34:00", "00:20:00"),
    (205, "12:42:00", "00:07:00"),
    (100, "10:29:00", "01:17:00"),
    (99, "14:36:00", "00:43:00"),
    (1, "14:51:00", "00:22:00"),
]

# Convert start time and duration to minutes
converted_data = [
    (ID, convert_time_to_minutes(start_time), convert_time_to_minutes(duration))
    for ID, start_time, duration in data
]

# Use the buskers_schedule function
result = buskers_schedule(converted_data)
# print(result)


# [('b', 1, 4), ('e', 4, 7), ('h', 8, 11)]
# print(
#     buskers_schedule(
#         [
#             ("a", 0, 6),
#             ("b", 1, 3),
#             ("c", 3, 2),
#             ("d", 3, 5),
#             ("e", 4, 3),
#             ("f", 5, 4),
#             ("g", 6, 4),
#             ("h", 8, 3),
#         ]
#     )
# )


def fractional_knapsack(capacity, items):
    """
    Returns the maximun achievable value obtainable with a knapsack of the given capacity
    and a given lsit of items, each represented by a tuple (name, value, weight). In this problem,
    you are allowed to take fractions of an item but at most one of any item.
    """
    dict_bi_wi = {}
    for tuples in items:
        value = tuples[1]
        weight = tuples[2]
        bi_wi = int(value / weight)
        dict_bi_wi[bi_wi] = tuples

    dict_bi_wi_values = sorted(dict_bi_wi, reverse=True)

    count = {}
    total = 0
    for value in dict_bi_wi_values:
        if capacity == 0:
            break
        dict_tuple_values = dict_bi_wi[value]
        weight_values = dict_tuple_values[2]
        if capacity - weight_values > 0:
            capacity -= weight_values
            total_value = dict_bi_wi[value][1]
            total += dict_bi_wi[value][1]
        if capacity - weight_values < 0:
            portion = capacity / weight_values
            remaining = weight_values * portion
            capacity -= remaining
            total_value = dict_bi_wi[value][1] * portion
            total += total_value
        count[dict_bi_wi[value][0]] = (1, total_value)

    return total


items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4),
]
print(float(fractional_knapsack(10, items)))

# # The example from the lecture notes
# items = [
#     ("Chocolate cookies", 20, 5),
#     ("Potato chips", 15, 3),
#     ("Pizza", 14, 2),
#     ("Popcorn", 12, 4),
# ]
# print(fractional_knapsack(9, items))
