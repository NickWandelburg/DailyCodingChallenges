# Randomly shuffle items of a list
import random


def shuffle_data(data):
    unshuffled_data = data.copy()
    for i in range(len(unshuffled_data)):
        # get random exchange index
        j = random.randint(0, len(unshuffled_data) - 1)
        # exchange items
        item = unshuffled_data[i]
        unshuffled_data[i] = unshuffled_data[j]
        unshuffled_data[j] = item
    return unshuffled_data


if __name__ == "__main__":
    # generate 10 random integers in range 0-100
    data = [random.randint(0, 100) for i in range(10)]

    # shuffle data randomly
    shuffled_data = shuffle_data(data)

    print("Unshuffled data: ", data)
    print("Shuffled data: ", shuffled_data)
