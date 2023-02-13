# Compute the distance between a given point (x0,y0) and a given line y=ax+by+c
import math


def point_to_line_distance(a, b, c, x0, y0):
    return (abs(a * x0 + b * y0 + c)) / math.sqrt(a**2 + b**2)


if __name__ == '__main__':
    # Definition of the line constants
    a = 3
    b = 4
    c = -6

    # Definition of the point
    x0 = .0
    y0 = .0

    distance = point_to_line_distance(a, b, c, x0, y0)

    print(f"Distance between point ({x0},{y0}) and line y={a}x{b:+}y{c:+} is {round(distance, 2)}")

