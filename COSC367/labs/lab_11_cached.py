from abc import abstractmethod, ABCMeta
import numpy as np
import numpy
import math


class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the
        vector of values resulting from function the layer is implementing."""


class ReLU(Function):
    def __init__(self):
        self.cache = []

    def __call__(self, inputs):
        output = []
        for n in inputs:
            if n < 0:
                output.append(0)
            if n >= 0:
                output.append(n)
        output = np.array(output)
        self.cache = output
        return output


class Sigmoid(Function):

    def __init__(self):
        self.cache = []

    def __call__(self, inputs):
        output = []
        for n in inputs:
            sigmoid = 1 / (1 + (math.e ** (-n)))
            output.append(sigmoid)
        output = np.array(output)
        self.cache = output
        return output


class Linear(Function):
    """
    implements a fully connected linear layear in a neural network
    """

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.cache = []

    def __call__(self, inputs):
        # z=Wx+b
        z = np.matmul(self.weights, inputs) + self.bias
        self.cache = z
        return z


def forward_pass(functions, input_vector):
    for function in functions:
        input_vector = function(input_vector)
    return input_vector


# layer = Linear(np.array([[2.0, 0.0, 1.0], [0.0, -1.0, 3.0]]), np.array([1.0, 0.5]))
# input_vector = np.array([1.0, 1.0, 1.0])
# functions = [layer, ReLU()]
# print(forward_pass(functions, input_vector))


# np.set_printoptions(precision=4)

# input_vector = np.array([1, 2], dtype=float)
# functions = [
#     Linear(np.array([[1, -0.5], [0, 1]]), np.array([-3, 1])),
#     ReLU(),
#     Linear(np.array([[1, 0.5]]), np.array([-1])),
#     Sigmoid(),
# ]
# print(forward_pass(functions, input_vector))


# input_vector = np.array([1, 0, 2], dtype=float)
# func = Sigmoid()
# output = func(func(func(input_vector)))
# print(np.all(output == func.cache))

# input1 = np.array([-0.05, 0.25, 0.15])
# input2 = np.array([0.75, -0.5, 0.25])
# func = ReLU()
# output1 = func(input1)
# output2 = func(input2)
# print(np.all(output2 == func.cache))


layer = Linear(np.array([[2.0, 0.0, 1.0], [0.0, -1.0, 3.0]]), np.array([1.0, 0.5]))
input_vector = np.array([1.0, -1.0, -1.0])
functions = [layer, ReLU()]
z = forward_pass(functions, input_vector)
print(input_vector, "->", layer.cache, "->", z)
