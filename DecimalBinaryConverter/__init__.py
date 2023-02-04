# Convert a decimal number to binary number and vice versa

def binary_to_decimal(binary_number):
    decimal_number = 0
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * 2 ** (len(binary_number) - i - 1)
    return decimal_number


def decimal_to_binary(decimal_number):
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


if __name__ == '__main__':
    decimal_number = 10
    print(f'Decimal number: {decimal_number}')
    binary_number = decimal_to_binary(decimal_number)
    print(f'Binary number: {binary_number}')
    binary_to_decimal(binary_number)
    print(f'Decimal number: {binary_to_decimal(binary_number)}')
