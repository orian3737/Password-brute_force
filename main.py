import itertools
import string
import time
import hashlib
from typing import Optional


def common_guess(word: str) -> Optional[str]:
    """
    Check if the password matches a common password from a word list.
    """
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()
    
    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def brute_force_plain(target: str, min_length: int, max_length: int, digits: bool = False, symbols: bool = False) -> Optional[str]:
    """
    Brute-force plain text passwords with a flexible length range.
    """
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess: str = ''.join(guess)

            if guess == target:
                return f'"{target}" was cracked in {attempts:,} guesses (length={length})'


def brute_force_hashed(target_hash: str, min_length: int, max_length: int, digits: bool = False, symbols: bool = False) -> Optional[str]:
    """
    Brute-force hashed passwords with a flexible length range.
    """
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess: str = ''.join(guess)

            if hash_password(guess) == target_hash:
                return f'"{guess}" was cracked in {attempts:,} guesses (length={length})'


def main():
    print('Password Cracking Tool')
    password_type = input("Is your target password plain text or hashed? (plain/hashed): ").strip().lower()

    min_length = int(input("Enter the minimum password length to try: "))
    max_length = int(input("Enter the maximum password length to try: "))

    digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    start_time: float = time.perf_counter()

    if password_type == "plain":
        target_password = input("Enter the plain text password to crack: ").strip()

        if common_match := common_guess(target_password):
            print(common_match)
        else:
            if cracked := brute_force_plain(target_password, min_length, max_length, digits, symbols):
                print(cracked)
            else:
                print('No match found...')
    elif password_type == "hashed":
        target_hash = input("Enter the hashed password to crack: ").strip()

        if cracked := brute_force_hashed(target_hash, min_length, max_length, digits, symbols):
            print(cracked)
        else:
            print('No match found...')
    else:
        print("Invalid input. Please choose 'plain' or 'hashed'.")

    end_time: float = time.perf_counter()
    print(f"Time elapsed: {round(end_time - start_time, 2)} seconds")


if __name__ == '__main__':
    main()
