# Split array into two parts with given ratio
import random
import numpy as np


def split_array(arr, ratio):
    arr = np.array(arr)
    # get random indices for split
    split_indices = random.sample(range(len(arr)-1), int(len(arr) * ratio))
    # split array
    arr_1 = arr[split_indices]
    arr_2 = np.delete(arr, split_indices)
    return list(arr_1), list(arr_2)


if __name__ == "__main__":
    # set split ratio
    ratio = 0.7

    # generate 10 random integers in range 0-100
    data = [random.randint(0, 100) for i in range(10)]

    # split data with given ratio
    split_1, split_2 = split_array(data, ratio)

    print(f"Original data: ({len(data)} items)", data)
    print(f"Ratio:  {np.round(ratio, 2)}/{np.round(1-ratio, 2)}")
    print(f"Split 1 ({len(split_1)} items): ", split_1)
    print(f"Split 2 ({len(split_2)} items):", split_2)
