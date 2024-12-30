def parse(s: str) -> list[list[str]]:
    return [list(x) for x in s.split("\n")]

# every time you find an x, search for m in all directions
# if you find an m, search for a in all directions, etc...
# or index all letters and see if they are adjacent in the
# correct order

def find_letter_coordinates(matrix: list[list[str]], letter: str) -> list[tuple[str, str]]:
    pos = []
    for i, lst in enumerate(matrix):
        for j in range(len(lst)):
            if matrix[i][j] == letter:
                pos.append((i, j))
    return pos

def main(s: str):
    count = 0
    matrix = parse(s)
    dic = {}
    for ch in "XMAS":
        dic[ch] = find_letter_coordinates(matrix, ch)
    for x in dic["X"]:
        x_row, x_col = x
        for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1)]:
            m_expected = (x_row + dx, x_col + dy)
            a_expected = (x_row + 2 * dx, x_col + 2 * dy)
            s_expected = (x_row + 3 * dx, x_col + 3 * dy)
            if (m_expected in dic["M"] and a_expected in dic["A"] and s_expected in dic["S"]):
                count += 1
    return count

with open("2024/4/input.txt") as f:
    print(main(f.read()))