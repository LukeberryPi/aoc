from typing import List

def parse(s: str) -> List[List[int]]:
    spl = s.split("\n")
    to_lists = list(map(lambda line: line.split(" "), spl))
    return [[int(x) for x in xs] for xs in to_lists]

def main(s):
    lsts = parse(s)
    for lst in lsts:
        pass

    return 0

with open('2024/2/input.txt') as f:
    print(main(f.read()))