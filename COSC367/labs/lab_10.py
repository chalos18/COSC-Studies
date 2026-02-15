import math


def euclidean_distance(v1, v2):
    return math.dist(v1, v2)


# print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))


def majority_element(labels):
    """
    returns a label that has the highest frequency
    """
    freq = {element: 0 for element in labels}
    for element in labels:
        freq[element] += 1
    return max(freq, key=freq.get)


# print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
# print(majority_element("ababc") in "ab")


def knn_predict(input, examples, distance, combine, k):
    """
    predicts the output by combining the output of the k nearest neighbours
    If after selecting k nearest neighbours, the distance to the farthest selected neighbour
    and the distance to the nearest unselected neighbour are the same, more neighbours must be
    selected until these two distances become different or all the examples are selected
    """
    distances = []
    for node in examples:
        x, classification = node
        dist_to_node = distance(input, x)
        distances.append((node, dist_to_node))

    while True:
        dist_sorted = sorted(distances, key=lambda x: x[1])
        closest_k = dist_sorted[:k]
        unselected_k = dist_sorted[k:]

        if not unselected_k:
            elements = [node[1] for node, _ in closest_k]
            return combine(elements)

        farthest_closest_k = closest_k[-1][1]
        nearest_unselected_k = unselected_k[0][1]

        if farthest_closest_k == nearest_unselected_k:
            # print(farthest_closest_k[1], nearest_unselected_k[1])
            k += 1
            # more neighbours must be selected
            continue
        else:
            elements = []
            for node, dist in closest_k:
                x, category = node
                elements.append(category)
            return combine(elements)


# examples = [
#     ([2], "-"),
#     ([3], "-"),
#     ([5], "+"),
#     ([8], "+"),
#     ([9], "+"),
# ]

# distance = euclidean_distance
# combine = majority_element

# for k in range(1, 6, 2):
#     print("k =", k)
#     print("x", "prediction")
#     for x in range(0, 10):
#         print(x, knn_predict([x], examples, distance, combine, k))
#     print()


def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        # Complete (a line or two)
        a = sum(w * x for w, x in zip(weights, input)) + bias
        return 1 if a >= 0 else 0

    return perceptron  # this line is fine


# weights = [2, -4]
# bias = 0
# perceptron = construct_perceptron(weights, bias)

# print(perceptron([1, 1]))
# print(perceptron([2, 1]))
# print(perceptron([3, 1]))
# print(perceptron([-1, -1]))

# from math import inf

# weights = [1]
# bias = 100
# perceptron = construct_perceptron(weights, bias)

# print(perceptron([inf]))
# print(perceptron([-inf]))
def accuracy(classifier, inputs, expected_outputs):
    """
    Passes each input to a perceptron and compares the predictions with the expected outputs
    Returns the accuracy of the classifier on the given data. Accuracy must be a number between 0 and 1
    """
    accuracy = []
    for i, input in enumerate(inputs):
        prediction = classifier(input)
        accuracy.append(1 if prediction == expected_outputs[i] else 0)
    return accuracy.count(1)/len(accuracy)

perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

# print(accuracy(perceptron, inputs, targets))

# weight = w + nx(t-y)
def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    """
    adjusts the weights and bias by iterating through the training data and applying the perceptron learning rule
    """
    # iterate while max epochs does not equal 0
    while max_epochs:
        for example in training_examples:
            inputs, t = example
            perceptron = construct_perceptron(weights, bias)
            y = perceptron(inputs)
            weights = [
                w + (learning_rate * x) * (t - y)
                for w, x in zip(weights, inputs)
            ]
            bias = bias + learning_rate * (t - y)
        max_epochs-=1
    return weights, bias

# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#     ((0, 0), 0),
#     ((0, 1), 0),
#     ((1, 0), 0),
#     ((1, 1), 1),
# ]
# max_epochs = 50

# weights, bias = learn_perceptron_parameters(
#     weights, bias, examples, learning_rate, max_epochs
# )
# print(f"Weights: {weights}")
# print(f"Bias: {bias}\n")

# perceptron = construct_perceptron(weights, bias)

# print(perceptron((0, 0)))
# print(perceptron((0, 1)))
# print(perceptron((1, 0)))
# print(perceptron((1, 1)))
# print(perceptron((2, 2)))
# print(perceptron((-3, -3)))
# print(perceptron((3, -1)))


weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 0),
]
max_epochs = 50

weights, bias = learn_perceptron_parameters(
    weights, bias, examples, learning_rate, max_epochs
)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")
