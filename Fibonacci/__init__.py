# Find the n-th Fibonacci number
import random

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    # Generate random number between 1 and 10
    n = random.randint(1, 10)

    print(f"The {n}th Fibonacci number is {fibonacci(n)}")
