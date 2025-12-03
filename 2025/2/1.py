import sys

sys.stdout = open("2025/2/log.txt", "a")

def parse(s: str) -> list[tuple[int, int]]:
    return [tuple(scope.split("-")) for scope in s.split(",")]

def main(s: str) -> int:
    scopes = parse(s)
    invalid_id_sum = 0
    for bottom, top in scopes:
        rang = range(int(bottom), int(top) + 1)
        for num in rang:
            strnum = str(num)
            if len(strnum) % 2 != 0:
                continue
            first_half, last_half = strnum[:len(strnum) // 2:], str(num)[len(strnum) // 2::]
            if first_half == last_half:
                invalid_id_sum += num
    return invalid_id_sum

with open('2025/2/input.txt') as f:
    print("result", main(f.read()), "\n")
