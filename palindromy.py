def is_palindrom (word):
    """
        Funkcja sprawdza czy słowo podane przez użytkownika to palindrom. 
        Zwraca wartość True gdy palindrom
        Zwraca wartość Fasle gdy nie palindrom 
        Argument:
        word
    """
    print(f"{word[::-1] == word[::1]}")

is_palindrom(input('wstaw słowo do sprawdzenia: '))