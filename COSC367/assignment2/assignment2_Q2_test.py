from assignment2 import is_valid_expression, depth

expression = 12
print(depth(expression))

expression = "weight"
print(depth(expression))

expression = ["add", 12, "x"]
print(depth(expression))

expression = ["add", ["add", 22, "y"], "x"]
print(depth(expression))
