# Find missing number in an array of n-1 numbers in range 1 to n
def find_missing_number(arr):
    n = len(arr) + 1
    # Formula to compute the sum of n numbers
    total = (n * (n + 1)) / 2
    # Sum of all the numbers in the array
    sum_of_arr = sum(arr)
    # Subtract the sum of the array from the sum of n numbers
    return int(total - sum_of_arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]

    print(f"The missing number is in {arr} is {find_missing_number(arr)}")

