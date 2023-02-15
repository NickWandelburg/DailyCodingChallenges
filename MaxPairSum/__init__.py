# Find the maximum sum of a pair of numbers in an array
import random


def max_pair_sum(arr):
    # Initialize the maximum numbers to 0
    max1 = max2 = 0
    for i in arr:
        # If the current number is greater than the first maximum number
        if i > max1:
            # Update the second maximum number to the first maximum number
            max2 = max1
            # Update the first maximum number to the current number
            max1 = i
        # If the current number is greater than the second maximum number
        elif i > max2:
            # Update the second maximum number to the current number
            max2 = i
    return max1 + max2


def max_pair_sum_sorting(arr):
    # Sort the array
    arr.sort()
    # Return the sum of the last two elements which correspond to the largest numbers
    return arr[-1] + arr[-2]


if __name__ == '__main__':
    # Generate random array with 10 elements
    data = [random.randint(0, 100) for i in range(10)]

    print(f"Manual method: The maximum sum of a pair of numbers in {data} is {max_pair_sum(data)}")
    print(f"Sorting method: The maximum sum of a pair of numbers in {data} is {max_pair_sum_sorting(data)}")

