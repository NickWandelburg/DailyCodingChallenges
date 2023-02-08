# Find the vertex of a quadratic function
def find_vertex(a, b, c):
    # solved derivative of quadratic function
    x = -b / (2 * a)
    # quadratic function at vertex
    y = a * (x ** 2) + b * x + c
    return x, y


if __name__ == "__main__":
    a = 1
    b = -10
    c = 4

    x, y = find_vertex(a, b, c)
    x, y = round(x, 2), round(y, 2)

    if a == 1:
        print(f"The vertex of y=x\u00b2{b:+}x{c:+} is at ({x}, {y})")
    elif a == -1:
        print(f"The vertex of y=-x\u00b2{b:+}x{c:+} is at ({x}, {y})")
    else:
        print(f"The vertex of y={a}x\u00b2{b:+}{c:+} is at ({x}, {y})")

