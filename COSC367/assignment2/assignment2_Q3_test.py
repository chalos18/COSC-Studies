from assignment2 import is_valid_expression, depth, evaluate

# bindings = {}
# expression = 12
# print(evaluate(expression, bindings))

# bindings = {"x": 5, "y": 10, "length": 15}
# expression = "y"
# print(evaluate(expression, bindings))

# bindings = {"x": 5, "y": 10, "abc": 15, "add": lambda x, y: x + y}
# expression = ["add", 12, "x"]
# print(evaluate(expression, bindings))

import operator

bindings = dict(x=5, y=10, blah=15, add=operator.add)
expression = ["add", ["add", 22, "y"], "x"]
print(evaluate(expression, bindings))
