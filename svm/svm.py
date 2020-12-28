import math
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt

COLORS = [
    "#D81159", "#218380", "#FBB13C",
    "#73D2DE", "#5E5768", "#548C2F",
    "#1D4E89", "#8F95D3", "#BCC4DB",
    "#023436", "#5D2A42", "#FF8360"
]

SEGMENTS = [
    [50, 120],
    [0, 50]
]
GRADIEN_STEP = 0.01
STEP_AMOUNT = 1000
AMOUNT = 10
X_ORD = 0
Y_ORD = 1

def normalize(data):
    normalized = []
    max_x = max(map(lambda _: _[X_ORD], data))
    max_y = max(map(lambda _: _[Y_ORD], data))
    for i in range(len(data)):
        normalized.append([data[i][X_ORD] / max_x, data[i][Y_ORD] / max_y])
    return normalized


def distance(vec1, vec2):
    return vector_len(map(lambda x, y: x - y, vec1, vec2))


def vector_len(vec):
    return math.sqrt(sum(map(lambda a: a * a, vec)))


def calc_margin(vec1, vec2):
    return sum(map(lambda x, y: x * y, vec1, vec2))


def sum_vectors(vec1, vec2):
    return list(map(lambda a, b: a + b, vec1, vec2))


def multiply_vector(vec, value):
    return list(map(lambda a: a * value, vec))


def normal_vector(arr_points):
    return reduce(lambda p, n: sum_vectors(p, n), arr_points, [1, 1])


if __name__ == "__main__":
    data = []
    for i in range(len(SEGMENTS)):
        temp = np.random.randint(SEGMENTS[i][X_ORD], SEGMENTS[i][Y_ORD], size=(AMOUNT, 2)).tolist()
        data += temp
        for point in temp: point.append((-1) ** i)
    marks = np.array(list(map(lambda x: x[-1], data)))
    raw_data = np.array(list(map(lambda x: x[0:-1], data)))

    vector = np.zeros((len(raw_data), 2))
    data = np.array(data)
    prod = np.zeros(len(data))
    epoch = 1

    while (epoch < 10000):
        y = vector * raw_data
        prod = (y[:, 0] + y[:, 1]) * marks
        for val in range(len(prod)):
            if (prod[val] >= 1):
                vector = vector - GRADIEN_STEP * (vector / STEP_AMOUNT)
            else:
                vector = vector + GRADIEN_STEP * (raw_data[val] * marks[val] - vector / STEP_AMOUNT)
        epoch += 1
    vector = list(vector[0])
    vector.append(vector_len(vector))

    plt.scatter(raw_data[:, 0], raw_data[:, 1], c=[COLORS[y] for y in marks])
    plt.plot([0, -vector[2] / vector[0]], [-vector[2] / vector[1], 0], '--', c=COLORS[3])
    plt.show()