def input_to_lists(s: str) -> tuple[list[int], list[int]]:
    to_lines = list(map(lambda line: line.split("   "), s.split("\n")))
    flatten = [int(x) for xs in to_lines for x in xs]
    left, right = flatten[::2], flatten[1::2]
    return (left, right)

def main(s: str) -> int:
    res = 0
    left, right = input_to_lists(s)
    for el in left:
        instances_in_right = right.count(el)
        res += el * instances_in_right
    return res

with open('2024/1/input.txt') as f:
    print(main(f.read()))
