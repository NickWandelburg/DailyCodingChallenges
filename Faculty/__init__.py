# Compute the n-th factorial (n!)
import random

def get_factorial(n):
    # 0! = 1
    faculty = 1
    # n! = n * (n-1)!
    for i in range(1, n+1):
        faculty *= i
    return faculty

def get_factorial_recursive(n):
    # 0! = 1
    if n == 0:
        return 1
    # n! = n * (n-1)!
    return n * get_factorial_recursive(n-1)


if __name__ == "__main__":
    # Get a random number between 0 and 10
    n = random.randint(0, 10)

    # Get the factorial of n with the for-based method
    factorial = get_factorial(n)
    # Get the factorial of n with the recursive method
    factorial_recursive = get_factorial_recursive(n)

    print(f"For-Bases: Factorial of {n} is {factorial}")
    print(f"Recursive: Factorial of {n} is {factorial_recursive}")
