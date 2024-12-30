
def remove_anagrams(lst: list[str]) -> list[str]:
    return list(set([''.join(sorted(el)) for el in lst]))

def find_valid_passphrases_two(s: str) -> int:
    valid_passphrases = 0
    passphrase_list = [passphrase.split(" ") for passphrase in s.split("\n")]

    for passphrase in passphrase_list:
        if len(passphrase) == len(set(passphrase)) and len(passphrase) == len(remove_anagrams(passphrase)):
            valid_passphrases += 1

    return valid_passphrases

with open('2017/4/input.txt') as f:
    print(find_valid_passphrases_two(f.read()))