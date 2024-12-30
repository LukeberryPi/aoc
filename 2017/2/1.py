
def spreadsheet_to_matrix(spreadsheet: str) -> list[list[int]]:
    rows = spreadsheet.split("\n")
    matrix = []
    for row in rows:
        matrix.append(row.split("\t"))

    return [[int(value) for value in row] for row in matrix]

def main(s: str) -> int:
    result = 0
    lines = spreadsheet_to_matrix(s)

    for line in lines:
        result += max(line) - min(line)

    return result

with open('2017/2/input.txt') as f:
    print(main(f.read()))