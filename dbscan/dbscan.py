import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

AXIS = [-1000, 1000]
POINT_AMOUNT = 1000
MIN_CLUSTER_AMOUNT = math.sqrt(POINT_AMOUNT)
COLORS = ["#4caf50", "#ffeb3b", "#f44336"]
RADIUS = abs(AXIS[0] - AXIS[1]) / 10
FIG = plt.gcf()
FIG.show()
X=0
Y=1

def vector_len(a_x, a_y, b_x, b_y):
    diff_x = a_x - b_x
    diff_y = a_y - b_y
    return math.sqrt(diff_x * diff_x + diff_y * diff_y)

if __name__ == "__main__":
    points = np.random.randint(AXIS[X], AXIS[Y], (2, POINT_AMOUNT))
    dinstances = list([] for i in range(POINT_AMOUNT))
    for i in range(len(points[X])):
        for j in range(len(points[X])):
            dinstances[i].append(vector_len(points[X][i], points[Y][i], points[X][j], points[Y][j]))
    green = [[], []]
    yellow = [[], []]
    gIndexes = []
    yIndexes = []
    red = points.copy()
    for i in range(len(dinstances[X])):
        filtered = list(filter(lambda x: x <= RADIUS and x != 0, dinstances[i]))
        if (len(filtered) < MIN_CLUSTER_AMOUNT): continue
        gIndexes.append(i)
        green[X].append(points[X][i])
        green[Y].append(points[Y][i])
    for i in range(len(dinstances)):
        if (i in gIndexes): continue
        if(not any(map(lambda x: dinstances[i][x] <= RADIUS and dinstances[i][x] != 0, gIndexes))): continue
        yIndexes.append(i)
        yellow[X].append(points[X][i])
        yellow[Y].append(points[Y][i])
    plt.plot(points[X], points[Y], 'ro', color=COLORS[2])
    plt.plot(green[X], green[Y], 'ro', color=COLORS[0])
    plt.plot(yellow[X], yellow[Y], 'ro', color=COLORS[1])
    FIG.canvas.draw()
    plt.show()