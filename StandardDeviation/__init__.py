# Compute the standard deviation of a given list of numbers
import random


def mean(data):
    return sum(data) / len(data)


def standard_deviation(data):
    # Get the mean of tha list
    mu = mean(data)
    return (sum([(x - mu)**2 for x in data]) / len(data))**(1/2)


if __name__ == '__main__':
    # Generate a list of 10 random numbers
    data = [random.randint(0, 100) for i in range(10)]

    # Compute the standard deviation
    std = standard_deviation(data)

    print(f'The standard deviation of {data} is {round(std, 2)}')
