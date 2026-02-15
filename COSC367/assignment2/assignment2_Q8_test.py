from assignment2 import (
    is_valid_expression,
    depth,
    evaluate,
    random_expression,
    _check_distinctness,
    prune,
    attach,
    generate_rest,
    predict_rest,
)

# sequence = [0, 1, 2, 3, 4, 5, 6, 7]
# the_rest = predict_rest(sequence)
# print(sequence)
# print(the_rest)


# sequence = [0, 2, 4, 6, 8, 10, 12, 14]
# print(predict_rest(sequence))


# sequence = [31, 29, 27, 25, 23, 21]
# print(predict_rest(sequence))


# sequence = [0, 1, 4, 9, 16, 25, 36, 49]
# print(predict_rest(sequence))


# sequence = [3, 2, 3, 6, 11, 18, 27, 38]
# print(predict_rest(sequence))


# sequence = [0, 1, 1, 2, 3, 5, 8, 13]
# print(predict_rest(sequence))


sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print(predict_rest(sequence))


# sequence = [1, 3, -5, 13, -31, 75, -181, 437]
# print(predict_rest(sequence))
