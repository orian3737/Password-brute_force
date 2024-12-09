import itertools
import string
import time
from typing import Optional

def common_guess(word: str) -> Optional[str]:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()
        
    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'
        
def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> Optional[str]:
    chars: str = string.ascii_lowercase
    
    if digits:
        chars += string.digits
    
    if symbols:
        chars += string.punctuation
    
    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)
        
        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses'
        
        # Removed the print statement to prevent output of guessed passwords
        # print(guess, attempts)
        
def main():
    print('Searching...')
    password: str = 'Password1' # Add pasword Here to Brute force
    
    start_time: float = time.perf_counter()
    
    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, length=i, digits=True, symbols=False):
                print(cracked)
            else:
                print('There was no match...')
            
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's')

if __name__ == '__main__':
    main()
