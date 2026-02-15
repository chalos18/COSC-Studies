from assignment2 import (
    is_valid_expression,
    depth,
    evaluate,
    random_expression,
    _check_distinctness,
    prune,
    attach,
)


# expression1 = ['+', 'a', 'b']
# expression2 = 'x'
# position = 1
# print(attach(expression1, expression2, position))

# expression1 = ['+', 'a', 'b']
# expression2 = ['-', 'x', 'y']
# position = 2
# print(attach(expression1, expression2, position))

# expression = ['*', 'x', ['+', 'y', 1]]
# subtree = ['-', 'a', 'b']
# position = 1
# print("Expression:", expression)
# print("New subtree:", subtree)
# print(f"Subtree attached at position {position}:", attach(expression, subtree, position))


expression = ["*", "x", ["+", "y", 1]]
subtree = ["-", "a", "b"]
position = 3
print("Expression:", expression)
print("New subtree:", subtree)
print(
    f"Subtree attached at position {position}:", attach(expression, subtree, position)
)
