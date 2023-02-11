# Get the indices of a pair in a sorted array in O(n), where the sum matches a given number
import random


def array_pair_sum(data, pair_sum):
    i = 0
    j = len(data)-1
    while i < j:
        # Sum of indices i and j matches the given pair sum
        if data[i] + data[j] == pair_sum:
            return [i, j]
        # Sum of indices i and j is greater than the given pair sum
        # Decrement j to get a smaller sum
        elif data[i] + data[j] > pair_sum:
            j -= 1
        # Sum of indices i and j is less than the given pair sum
        # Increment i to get a larger sum
        else:
            i += 1

if __name__ == '__main__':
    # Generate 10 random integers in range 0-10 without duplicates in ascending order
    data = sorted(random.sample(range(1, 20), 10))

    # Get two random indices
    indices = random.sample(range(0, len(data)-1), 2)

    # Get the sum of the two random indices as the pair sum
    pair_sum = data[indices[0]] + data[indices[1]]

    # Get the indices of the pair in the sorted array, where the sum is the pair sum
    pair_indices = array_pair_sum(data, pair_sum)

    print(f"The indices of the pair in the sorted array {data}, where the sum is {pair_sum} are {pair_indices}.")
    print(f"Validation: {pair_sum == data[pair_indices[0]] + data[pair_indices[1]]}")


