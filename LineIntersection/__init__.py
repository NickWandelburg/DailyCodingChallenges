# Find the intersection of two Lines
def get_intersection(a1, b1, a2, b2):
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y


if __name__ == "__main__":
    # First Line y = a1 * x + b1
    a1 = 3
    b1 = -4

    # Second Line y = a2 * x + b2
    a2 = 4
    b2 = -9

    # Find the intersection of the two lines
    x, y = get_intersection(a1, b1, a2, b2)

    print(f"The intersection of y={a1}x{b1:+} and y={a2}x{b2:+} is at ({x}, {y})")

