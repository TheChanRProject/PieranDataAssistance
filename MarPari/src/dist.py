import math
# Distance Function
def distance(point_1: tuple, point_2: tuple) -> float:
    return math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)

# Point Input Function with Distances From All Combinations of 3 Points Specified by User
def point_input():
    x = [float(i) for i in input("Put in 3 x values separated by a space: ").split(" ")]
    y = [float(i) for i in input("Put in 3 y values separated by a space: ").split(" ")]
    points = list(zip(x,y))
    distances = [distance(points[0], points[1]), distance(points[1], points[2]), distance(points[0], points[2])]
    return f"Distance between first point and second point is {distances[0]} \n \
    Distance between second point and third point is {distances[1]} \n \
    Distance between first point and third point is {distances[2]}"

print(point_input())
