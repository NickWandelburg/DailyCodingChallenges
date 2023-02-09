# BinarySearch algorithm
import random


def binary_search(data, target):
    # Returns the index of the target if found, otherwise returns None
    if len(data) == 0:
        return None
    else:
        # Find the midpoint of the data
        midpoint = len(data) // 2
        # If the target is equal to the midpoint, return the midpoint
        if data[midpoint] == target:
            return midpoint
        # If the target is less than the midpoint, search the left half
        elif target < data[midpoint]:
            return binary_search(data[:midpoint], target)
        # If the target is greater than the midpoint, search the right half
        else:
            result = binary_search(data[midpoint+1:], target)
            if result is None:
                return None
            else:
                return result + midpoint + 1


if __name__ == "__main__":
    # Generate a list of random numbers sorted in ascending order
    data = sorted([random.randint(0, 100) for _ in range(10)])

    # Select a random target number as the index of the target number
    target_index = random.randint(0, len(data)-1)
    target = data[target_index]

    # Perform a binary search on the data
    binary_search_index = binary_search(data, target)

    if binary_search_index is None:
        print(f"Target {target} not found in {data}")
    else:
        print(f"Target {target} is at index {target_index} in {data}")

