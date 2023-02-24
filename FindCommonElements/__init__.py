# Find common elements in two sorted lists
import random

def find_common_numbers(_list1, _list2) -> list:
    # Create a set to store the common numbers without duplicates
    _common_numbers = set()
    # Comparison pointers
    i = 0
    j = 0
    # Iterate through both lists
    while i < len(_list1) and j < len(_list2):
        # If the numbers are equal, add to the set
        if _list1[i] == _list2[j]:
            _common_numbers.add(_list1[i])
            i += 1
            j += 1
        # If the number in list1 is smaller, get the next higher number in list1 for comparison
        elif _list1[i] < _list2[j]:
            i += 1
        # If the number in list1 is smaller, get the next higher number in list2 for comparison
        else:
            j += 1
    return list(_common_numbers)


if __name__ == "__main__":
    # Generate two sorted lists of random numbers with same size
    list1 = sorted([random.randint(0, 20) for i in range(10)])
    list2 = sorted([random.randint(0, 20) for i in range(10)])

    common_numbers = find_common_numbers(list1, list2)

    if len(common_numbers) == 0:
        print(f"There are no common numbers in {list1} and {list2}")
    else:
        print(f"The common numbers in {list1} and {list2} are: {common_numbers}")
