# Compute the volume of a sphere given its radius
import math

def get_volume(radius):
    return (4/3) * math.pi * radius**3


if __name__ == '__main__':
    # Radius
    r = 5.0

    # Compute the volume
    volume = get_volume(r)

    print(f'The volume of a sphere with radius {r} is {volume:.2f}')

