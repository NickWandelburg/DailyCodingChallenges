# QuickSort sorting algorithm
import random

def quick_sort(data):
    # if data has only one element, return it
    if len(data) <= 1:
        return data
    else:
        # select pivot element
        pivot = data[0]
        # divide data into two parts
        # smaller than pivot
        smaller = [i for i in data[1:] if i <= pivot]
        # greater than pivot
        greater = [i for i in data[1:] if i > pivot]
        # sort smaller and greater parts
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    # generate 10 random integers in range 0-100
    data = [random.randint(0, 100) for i in range(10)]

    # sort data with QuickSort
    sorted_data = quick_sort(data)

    print("Unsorted data: ", data)
    print("Sorted data: ", sorted_data)
