def input_to_lists(s: str) -> tuple[list[int], list[int]]:
    to_lines = list(map(lambda line: line.split("   "), s.split("\n")))
    flatten = [int(x) for xs in to_lines for x in xs]
    left, right = flatten[::2], flatten[1::2]
    return (left, right)

def main(s: str) -> int:
    res = 0
    sorted_left, sorted_right = sorted(input_to_lists(s)[0]), sorted(input_to_lists(s)[1])
    for i in range(len(sorted_left)):
        res += abs(sorted_left[i] - sorted_right[i])
    return res

with open('2024/1/input.txt') as f:
    print(main(f.read()))
