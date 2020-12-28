import math
import numpy as np
import matplotlib.pyplot as plt

COLORS = [
    "#D81159", "#218380", "#FBB13C",
    "#73D2DE", "#5E5768", "#548C2F",
    "#1D4E89", "#8F95D3", "#BCC4DB",
    "#023436", "#5D2A42", "#FF8360"
]
CLUSTER_AMOUN = 5
SIZE = 100
SEGMENT = [100, 10000]
X = 0
Y = 1
FIG = plt.gcf()
FIG.show()


def find_minimum(arr):
    minimum = min(map(lambda _: min(_), arr))
    return np.where(arr == minimum)


def vector_len(a_x, a_y, b_x, b_y):
    diff_x = a_x - b_x
    diff_y = a_y - b_y
    return math.sqrt(diff_x * diff_x + diff_y * diff_y)


def KNP(dinstances):
    a, b = list(find_minimum(dinstances))
    indexes = [a]
    road_map = list(a)
    while len(indexes) != SIZE - 1:
        dinstances[a[0]][a[1]] = math.inf
        dinstances[a[1]][a[0]] = math.inf
        for temp in range(len(dinstances[0])):
            dinstances[temp][a[0]] = math.inf
            dinstances[temp][a[1]] = math.inf
        minimums = list(map(lambda _: min(dinstances[_]), road_map))
        c = min(minimums)
        a = np.where(dinstances == c)
        a = [a[0][0], a[1][0]]
        indexes.append(a)
        if a[0] not in road_map:
            road_map.append(a[0])
        elif a[1] not in road_map:
            road_map.append(a[1])

    return road_map, indexes


if __name__ == "__main__":
    indexes = []
    road_map = []
    graph = list([[], []] for i in range(CLUSTER_AMOUN))
    points = np.random.randint(SEGMENT[0], SEGMENT[1], size=(2, SIZE))
    dinstances = np.empty((SIZE, SIZE))
    for i in range(len(points[X])):
        dinstances[i][i] = math.inf
        for j in range(0, i):
            dinstances[j][i] = dinstances[i][j] = vector_len(points[X][i], points[Y][i], points[X][j], points[Y][j])
    dinstances_copy = dinstances.copy()
    road_map, indexes = KNP(dinstances)
    for i in range(CLUSTER_AMOUN):
        index, maximum = 0, 0
        for j in range(len(indexes) - 1):
            a, b = indexes[j]
            index = j if dinstances_copy[a][b] > maximum else index
            maximum = max(maximum, dinstances_copy[a][b])
        del indexes[index]
    for temp in indexes:
        arr = [
            [points[X][temp[0]], points[X][temp[1]]],
            [points[Y][temp[0]], points[Y][temp[1]]]
        ]
        plt.plot(arr[X], arr[Y], color=COLORS[1])
    plt.plot(points[X], points[Y], 'ro', color="red")
    FIG.canvas.draw()
    plt.show()