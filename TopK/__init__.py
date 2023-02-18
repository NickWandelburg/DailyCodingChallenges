# Find the top k elements in a list without using any sorting
import random

def top_k(data, k):
    _data = data.copy()
    _top_k_elements = []
    for _ in range(k):
        # Find the current maximum element in the list
        curr_max = _data[0]
        curr_max_index = 0
        for i in range(1, len(_data)):
            if _data[i] > curr_max:
                curr_max = _data[i]
                curr_max_index = i
        # Add the current maximum element to the top k elements list
        _top_k_elements.append(curr_max)
        # Remove the current maximum element from the list
        del _data[curr_max_index]
    return _top_k_elements


if __name__ == '__main__':
    # Generate a list of 10 random numbers
    data = [random.randint(0, 100) for i in range(10)]

    # Find the top 3 elements
    k = 3
    top_k_elements = top_k(data, k)

    print(f'Top {k} elements in {data} are {top_k_elements}')
