def main(s: str) -> int:
    total = 0
    opposite_index = len(s) // 2

    for curr, next in list(zip(s, s[opposite_index:])):
        if curr == next:
            total += int(curr) * 2

    return total

with open('2017/1/input.txt') as f:
    print(main(f.read()))
