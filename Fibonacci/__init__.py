# Find the nth Fibonacci number
import random

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # Generate random number between 1 and 100
    n = random.randint(1, 10)

    print(f"The {n}th Fibonacci number is {fib(n)}")
