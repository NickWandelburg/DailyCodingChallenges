# Given an array of integers, find the sum of its elements.

def array_sum(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return arr_sum

def recursive_array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_array_sum(arr[1:])


if __name__ == '__main__':
    data = [1, 2, 3, 4, 10, 11]
    print(f'Sum of {data} is: {array_sum(data)}')
    print(f'Recursive Sum of {data} is: {recursive_array_sum(data)}')
