# Remove duplicates of a given list
import random

if __name__ == '__main__':
    # Generate a list with 10 random numbers between 0 and 100
    list_with_duplicates = sorted([random.randint(0, 100) for i in range(10)])

    # Add two duplicates to the list
    list_with_duplicates.append(list_with_duplicates[0])
    list_with_duplicates.append(list_with_duplicates[1])

    # Sort the list for easier comparison
    list_with_duplicates.sort()

    # Convert the list to a set (implicitly removes all duplicates) and back to a list
    list_without_duplicates = list(set(list_with_duplicates))

    # Sort the list for easier comparison
    list_without_duplicates.sort()

    print(f'List with duplicates: {list_with_duplicates}')
    print(f'List without duplicates: {list_without_duplicates}')
    print(f'Number of duplicates: {len(list_with_duplicates) - len(list_without_duplicates)}')
