from typing import List

def find_valid_passphrases(s: str) -> int:
    valid_passphrases = 0
    passphrase_list = [passphrase.split(" ") for passphrase in s.split("\n")]

    for passphrase in passphrase_list:
        if len(passphrase) == len(set(passphrase)):
            valid_passphrases += 1

    return valid_passphrases

with open('2017/4/input.txt') as f:
    print(find_valid_passphrases(f.read()))