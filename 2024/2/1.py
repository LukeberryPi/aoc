from typing import List

def parse(s: str) -> List[List[int]]:
    spl = s.split("\n")
    to_lists = list(map(lambda line: line.split(" "), spl))
    return [[int(x) for x in xs] for xs in to_lists]

def main(s) -> int:
    lsts = parse(s)
    safe_lists = 0
    for lst in lsts:
        diffs = []
        is_safe = True
        for left, right in zip(lst, lst[1:]):
            diff = right - left
            if abs(diff) > 3 or abs(diff) < 1:
                is_safe = False
                break
            diffs.append(diff > 0)
        if is_safe:
            ascending = all(diffs)
            descending = not any(diffs)
            if ascending or descending:
                safe_lists += 1
    return safe_lists

with open('2024/2/input.txt') as f:
    print(main(f.read()))