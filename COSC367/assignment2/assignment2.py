def is_valid_expression(object, function_symbols, leaf_symbols):
    """
    Tests whether the object is a valid expression
    an expression if it meets one of following:
        constant leaf - integer
        variable leaf - a string of leaf symbols
        function application -
            contains 3 elements,
            has a first element that is a string (e.g., '*'), selected from a pre-defined set of function symbols.
            has the remaining two elements as expressions themselves, which serve as the arguments of the function.
    returns: True if valid, False otherwise
    """

    # base case if its a variable leaf
    if object in leaf_symbols:
        return True
    else:
        # if its a constant leaf
        if type(object) == int:
            return True
        if type(object) == float:
            return False
        # if its a function application
        if len(object) == 3:
            if object[0] in function_symbols:
                argument_1 = is_valid_expression(
                    object[1], function_symbols, leaf_symbols
                )
                argument_2 = is_valid_expression(
                    object[2], function_symbols, leaf_symbols
                )
                return argument_1 and argument_2
            else:
                return False
        else:
            return False


def depth(expression):
    """
    Recursive function
    The depth of an expression that is just a single leaf is zero
    """
    if not isinstance(expression, list):
        return 0

    max_depth = 0
    for item in expression:
        if isinstance(item, list):
            max_depth = max(max_depth, depth(item))

    return max_depth + 1


def evaluate(expression, bindings):
    """
    an integer evaluates to itself
    a string is looked up in a dictionary of binding which maps strings to integers
    For a list:
        the value of the function symbol is looked up in the dict of bindings.
            function symbols are mapped to binary functions that take two ints as args and return an int
        the two remaining elements in the list are evaluated
        the function is applied to the values of these arguments, and the result becomes the value of the list
    """
    # int evaluates to itself
    if type(expression) == int:
        return expression
    # str is looked up in bindings
    if type(expression) == str:
        return bindings[expression]
    # recursive case
    evaluated_values = []
    for element in expression:
        result = evaluate(element, bindings)
        evaluated_values.append(result)

    # print(evaluated_values)
    result = evaluated_values[0](*evaluated_values[1:])
    return result


import random


def _check_distinctness(expressions):
    str_expressions = []
    for expression in expressions:
        str_expressions.append(str(expression))
    # to_str = [' '.join(str(sublist) for sublist in expressions)]
    print(str_expressions)
    unique = set(str_expressions)
    n_unique = len(unique)
    print(n_unique)
    return n_unique


def random_expression(function_symbols, leaves, max_depth):
    """
    randomly generates an expression
    function_symbols: a list of function symbols (strings)
    leaves: a list of constant and variable leaves (integers and strings)
    max_depth: a non-negative integer that specifies the maximum depth allowed for the generated expression.
    function will be called 10000 time to generate this many expressions
    1000 must be syntactically distinct. ['+', 1, 2] and ['+', 2, 1] will be regarded as different expressions.
    at least 100 must be of depth 1 and at least 100 must be of depth max_depth
    """
    # toss a coin (or other condition you determine is satisfied)
    # if its heads, return a leaf node
    # heads is 0, tails is 1
    coin_flip = random.randint(0, 1)
    len_leaves = len(leaves)
    if coin_flip == 0:
        return leaves[random.randrange(0, len_leaves)]
    # tails
    else:
        # if its tails, return a random expression tree (a 3 element list)
        # function must be randomly selected from list of function symbols
        # then randomly generate its two arguments
        if max_depth == 0:
            return leaves[random.randrange(0, len_leaves)]

        expression_tree = []
        len_f_symbols = len(function_symbols)
        random_function = function_symbols[random.randrange(0, len_f_symbols)]

        if max_depth >= 0:
            operand1 = random_expression(function_symbols, leaves, max_depth - 1)
            operand2 = random_expression(function_symbols, leaves, max_depth - 1)

            expression_tree.append(random_function)
            expression_tree.append(operand1)
            expression_tree.append(operand2)

    return expression_tree


def prune(expression, max_depth, leaf_symbols):
    """
    returns the expression that results from removing all nodes from expression that 
    are at a depth greater than max_depth
    if there is a function node at depth equal to max_depth, the function nodes and its subtrees
    are to be replaced with a random leaf node chosen from leaf_symbols
    """
    # base case if we are at max_depth or below then return a random leaf node to replace expression
    # return a random leaf node
    if not isinstance(expression, list):
        return expression
    if max_depth == 0:
        len_leaves = len(leaf_symbols)
        return leaf_symbols[random.randrange(0, len_leaves)]
    if max_depth < 0:
        return '!'

    new_expression = expression.copy()

    for i, subtree in enumerate(new_expression):
        if isinstance(subtree, list):
            pruned_subtree = prune(subtree, max_depth - 1, leaf_symbols)
            new_expression[i] = pruned_subtree
    return new_expression


def attach(expression1, expression2, position):
    # Helper function to recursively traverse and rebuild
    def helper(expr1, index):
        # `index` is a mutable list [current_position]
        if index[0] == position:
            # Replace this node
            index[0] += 1
            return expression2

        # Base case: if expr is an atom (not a list)
        if not isinstance(expr1, list):
            index[0] += 1
            return expr1

        # Otherwise, traverse the list (compound expression)
        result = []
        for item in expr1:
            if index[0] > position:
                # Already replaced, just copy remaining
                result.append(item)
            else:
                result.append(helper(item, index))
        return result

    return helper(expression1, [0])


def generate_rest(initial_sequence, expression, length):
    """
    returns a list of integers with the specified length that is the
    continuation of the initial list according to the given expression
    """
    bindings = {
        "i": len(initial_sequence),
        "x": initial_sequence[-2],
        "y": initial_sequence[-1],
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    result = []
    while length:
        evaluation = evaluate(expression, bindings)
        result.append(evaluation)
        if len(result) == 1:
            bindings['x'] = initial_sequence[-1]
            bindings['y'] = result[-1]
        else:
            # update bindings as new values are generated
            bindings['x'] = result[-2]
            bindings["y"] = result[-1]

        bindings['i'] +=1
        length-=1
    return result

import random


def random_expression(depth=0, max_depth=3):
    if depth >= max_depth:
        return random.choice(["i", "x", "y", random.randint(-5, 5)])

    op = random.choice(["+", "-", "*"])
    left = random_expression(depth + 1, max_depth)
    right = random_expression(depth + 1, max_depth)
    return [op, left, right]


def predict_rest(sequence):
    """
    finds the pattern in the sequence and "predicts" the rest by returning a list of 
    the next 5 ints in the sequence.
    potentially generating random expressions until a match is found
    """
    while True:
        # generate expression trees with different operators
        expr = random_expression()
        generated = generate_rest(sequence[:3], expr, len(sequence) - 3)
        # attempt to generate rest of sequence
        if generated == sequence[3:]:
            # if it matches the sequence then use it
            return generate_rest(sequence, expr, 5)
