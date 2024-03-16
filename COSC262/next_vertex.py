from algorithms import *
from tests import * 
import math

def next_vertex(in_tree, distance):
    min_distance = float("inf")
    min_vertex = None

    for i, dist in enumerate(distance):
        if not in_tree[i]:
            if dist < min_distance:
                min_distance = dist
                min_vertex = i
            elif min_vertex is None:
                min_vertex = i

    return min_vertex

# Next vertex

# failing edge case
in_tree = [True, False, False, True]
distance = [3, 5, 3, 0]
print(next_vertex(in_tree, distance))

# failing edge case - not failing
in_tree = [True, True, True, False, True]
distance = [math.inf, 0, math.inf, math.inf, math.inf]
print(next_vertex(in_tree, distance))

in_tree = [False, True, True, False, False]
distance = [math.inf, 0, 3, 12, 5]
print(next_vertex(in_tree, distance))
