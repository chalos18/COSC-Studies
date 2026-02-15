from assignment2 import (
    is_valid_expression,
    depth,
    evaluate,
    random_expression,
    _check_distinctness,
    prune
)

expression = ["*", "x", ["+", "y", 1]]
max_depth = 1
pruned = prune(expression, max_depth, ["!"])
print("Expression: ", expression)
print("Pruned Expression: ", pruned)

# expression = ["*", "x", ["+", "y", 1]]
# max_depth = 1
# pruned = prune(expression, max_depth, ["!"])
# print("Expression: ", expression)
# print("Pruned Expression: ", pruned)


# expression = ["-", ["+", "a", ["*", "b", "c"]], ["*", ["+", "x", 1], "y"]]
# max_depth = 2
# pruned = prune(expression, max_depth, ["!"])
# print("Expression: ", expression)
# print("Pruned Expression: ", pruned)


# expression = ["+", "x", "z"]
# max_depth = 0
# pruned = prune(expression, max_depth, ["!"])
# print("Expression: ", expression)
# print("Pruned Expression: ", pruned)


# expression = "a"
# max_depth = 1
# pruned = prune(expression, max_depth, ["!"])
# print(expression)
# print(pruned)



