def is_palindrom (word):
    print(f"{word[::-1] == word[::1]}")

is_palindrom(input('wstaw słowo do sprawdzenia: '))