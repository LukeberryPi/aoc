def main(s: str) -> int:
    total = 0

    if s[-1] == s[0]:
        total += int(s[0])

    for curr, next in list(zip(s, s[1:])):
        if curr == next:
            total += int(curr)

    return total


with open('2017/1/input.txt') as f:
    print(main(f.read()))
