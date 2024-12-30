import re

def parse(s: str) -> list[list[str]]:
    return [list(x) for x in s.split("\n")]

# for a given A, check for 2 S and 2 M diagonally adjacent
# same letter cannot be in the same diagonal

def find_letter_coordinates(matrix: list[list[int]], letter: str) -> list[tuple[int, int]]:
    pos = []
    for i, lst in enumerate(matrix):
        for j in range(len(lst)):
            if matrix[i][j] == letter:
                pos.append((i, j))
    return pos

def main(s: str) -> int:
    count = 0
    matrix = parse(s)
    dic = {}
    for ch in "MAS":
        dic[ch] = find_letter_coordinates(matrix, ch)
    for a in dic["A"]:
        a_row, a_col = a
        s_count, m_count = 0, 0
        for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            if (a_row + dx, a_col + dy) in dic["M"] and (a_row - dx, a_col - dy) in dic["M"]: continue
            if (a_row + dx, a_col + dy) in dic["S"] and (a_row - dx, a_col - dy) in dic["S"]: continue
            s_count += 1 if (a_row + dx, a_col + dy) in dic["S"] else 0
            m_count += 1 if (a_row + dx, a_col + dy) in dic["M"] else 0
        if s_count == 2 and m_count == 2:
            count += 1
    return count

with open("2024/4/input.txt") as f:
    print(main(f.read()))