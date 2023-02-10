# Check if a string is a palindrome

def check_palindrome(string):
    return string.lower() == string[::-1].lower()


if __name__ == "__main__":
    string = "Level"

    is_palindrome = check_palindrome(string)

    if is_palindrome:
        print(f"\"{string}\" is a palindrome")
    else:
        print(f"\"{string}\" is not a palindrome")