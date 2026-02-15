from abc import abstractmethod, ABCMeta
import numpy as np


class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the
        vector of values resulting from function the layer is implementing."""


class ReLU(Function):

    def __call__(self, inputs):
        output = []
        for n in inputs:
            if n < 0:
                output.append(0)
            if n >= 0:
                output.append(n)
        return np.array(output)


import numpy

# relu = ReLU()
# inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
# outputs = relu(inputs)
# print(type(outputs) == numpy.ndarray)


# inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
# relu = ReLU()
# print(f"{'' : <5}ReLU")
# for i, o in zip(inputs, relu(inputs)):
#     print(f"{f'{i:.2f}' : <5} -> " + f"{o:.2f}")
import math


class Sigmoid(Function):

    def __call__(self, inputs):
        output = []
        for n in inputs:
            sigmoid = 1 / (1 + (math.e ** (-n)))
            output.append(sigmoid)
        return np.array(output)


# sigmoid = Sigmoid()
# inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
# outputs = sigmoid(inputs)
# print(type(outputs) == numpy.ndarray)

# inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
# sigmoid = Sigmoid()
# print(f"{'' : <3}Sigmoid")
# for i, o in zip(inputs, sigmoid(inputs)):
#     print(f"{f'{i:.2f}' : <5} -> " + f"{o:.2f}")


class Linear(Function):
    """
    implements a fully connected linear layear in a neural network
    """

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def __call__(self, inputs):
        # z=Wx+b
        z = np.matmul(self.weights, inputs) + self.bias
        return z


# f = Linear(np.identity(2), np.zeros(2))
# print(type(f.weights) == np.ndarray)
# print(type(f.bias) == np.ndarray)


# weights = np.array([[1, 2, 1], [3, -1, 2]], dtype=float)
# bias = np.array([0.5, -0.5])

# linear_layer = Linear(weights, bias)
# inputs = np.array([1, 1, 1], dtype=float)
# outputs = linear_layer(inputs)

# print(type(outputs) == np.ndarray)
# print(len(outputs) == 2)


# weights = np.array([[1, 2, 1], [3, -1, 2]], dtype=float)
# bias = np.array([0.5, -0.5])

# linear_layer = Linear(weights, bias)
# inputs = np.array([1, 0, 2], dtype=float)
# outputs = linear_layer(inputs)

# print(f"{inputs} -> {outputs}")

def forward_pass(functions, input_vector):
    for function in functions:
        input_vector = function(input_vector)
    return input_vector


layer = Linear(
    np.array([[2.0, 0.0, 1.0], [0.0, -1.0, 3.0]]),
    np.array([1.0, 0.5])
)
input_vector = np.array([1.0, 1.0, 1.0])
functions = [layer, ReLU()]
print(forward_pass(functions, input_vector))


np.set_printoptions(precision=4)

input_vector = np.array([1, 2], dtype=float)
functions = [
    Linear(np.array([[1, -0.5], [0, 1]]), np.array([-3, 1])),
    ReLU(),
    Linear(np.array([[1, 0.5]]), np.array([-1])),
    Sigmoid()
]
print(forward_pass(functions, input_vector))