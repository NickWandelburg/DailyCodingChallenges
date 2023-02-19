# Find duplicate numbers in a list
import random

def find_duplicates(data):
    non_duplicates = []
    duplicates = []
    for number in data:
        if number not in non_duplicates:
            # Number has not been seen already
            non_duplicates.append(number)
        else:
            # Number has been seen already, so it is a duplicate
            duplicates.append(number)
    return duplicates


if __name__ == '__main__':
    # Generate a list of 10 numbers in range 0-10
    data = list(range(10))
    # Add duplicate numbers
    data.append(5)
    data.append(6)

    # Shuffle the list
    random.shuffle(data)

    duplicate_numbers = find_duplicates(data)

    print(f"{duplicate_numbers} is duplicate in {data}")

