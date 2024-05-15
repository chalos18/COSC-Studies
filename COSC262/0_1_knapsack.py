import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
        
#  Top down implementation with memoisation -> cache as dict
def max_value_top_down_dict_cache(items, capacity, n=None, cache=None):
    """
    Returns the maximum value achievable with the given list of items 
    and a knapsack of the given capacity.
    fewer than 500 items and fewer than 500 capacity
    """
    if n is None:
        n = len(items)
    if cache is None:
        cache = {}
    if n == 0 or capacity == 0:
        return 0
    elif (n,capacity) in cache:
        return cache[(n,capacity)]
    elif items[n-1].weight > capacity:
        return max_value_top_down_dict_cache(items, capacity, n-1, cache)
    else:
        best = max(max_value_top_down_dict_cache(items, capacity, n-1, cache), 
                   items[n-1].value + max_value_top_down_dict_cache(items, capacity-(items[n-1].weight), n-1, cache))
        cache[(n, capacity)] = best
        return best
    
def max_value_top_down_table_cache(items, capacity, n=None, cache=None,item_list=None):
    """
    Returns the maximum value achievable with the given list of items 
    and a knapsack of the given capacity.
    fewer than 500 items and fewer than 500 capacity
    """
    if n is None:
        n = len(items)
    # if item_list is None:
    #     items_used = [[] for _ in range(n)]
    if cache is None:
        cache = [capacity * [-1] for row in range(n)]
    if n == 0 or capacity == 0:
        return 0
    elif cache[n-1][capacity-1] != -1:
        return cache[n-1][capacity-1]
    elif items[n-1].weight > capacity:
        return max_value_top_down_table_cache(items, capacity, n-1, cache)
    else:
        best = max(max_value_top_down_table_cache(items, capacity, n-1, cache), 
                   items[n-1].value + max_value_top_down_table_cache(items, capacity-(items[n-1].weight), n-1, cache))
        cache[n-1][capacity-1] = best
        return best
    
# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same

# items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
# print(max_value_top_down_table_cache(items, 500))

items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

# print(max_value_top_down_table_cache(items, 10))


def max_value_bottom_up(items, capacity, n=None, cache=None):
    """
    Returns the maximum value achievable with the given list of items 
    and a knapsack of the given capacity, along with the list of items used.
    fewer than 500 items and fewer than 500 capacity
    """
    if n is None:
        n = len(items)
    if cache is None:
        cache = [[-1] * (capacity + 1) for _ in range(n + 1)]

    # Initialize a dictionary to keep track of items used
    items_used = {}

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                cache[i][w] = 0
            elif items[i - 1].weight <= w:
                # Update the cache table
                cache[i][w] = max(
                    items[i - 1].value + cache[i - 1][w - items[i - 1].weight],
                    cache[i - 1][w]
                )
                # Track the item used
                if cache[i][w] != cache[i - 1][w]:
                    items_used[(i, w)] = items[i - 1]
            else:
                cache[i][w] = cache[i - 1][w]
    
    print(cache)

    # Reconstruct the list of items used
    itemList = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if (i, j) in items_used:
            itemList.append(items_used[(i, j)])
            j -= items_used[(i, j)].weight
        i -= 1

    return cache[n][capacity], itemList




# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same

items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
# print(max_value_bottom_up(items, 500))

items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value_bottom_up(items, 10))


# items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
# # print(max_value(items, 500))

# items = [
#     Item(45, 3),
#     Item(45, 3),
#     Item(80, 4),
#     Item(80, 5),
#     Item(100, 8)]

# print(max_value(items, 10))




