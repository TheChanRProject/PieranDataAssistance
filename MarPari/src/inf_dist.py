import math
from itertools import combinations
# Distance Function
def distance(point_1: tuple, point_2: tuple) -> float:
    return math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)

# Point Input Function with Distances From All Combinations of 3 Points Specified by User
def point_input():
    x = [float(i) for i in input("Put in x values separated by a space: ").split(" ")]
    y = [float(i) for i in input("Put in y values separated by a space: ").split(" ")]
    points = list(zip(x,y))
    combos = list(combinations(points, 2))
    distances = []
    for pos in combos:
        distances.append(distance(pos[0], pos[1]))
    return distances


print(point_input())
