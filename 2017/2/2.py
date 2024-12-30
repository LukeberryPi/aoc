
def spreadsheet_to_matrix(spreadsheet: str) -> list[list[int]]:
    rows = spreadsheet.split("\n")
    matrix = []
    for row in rows:
        matrix.append(row.split("\t"))

    return [[int(value) for value in row] for row in matrix]

def list_quotient_sum(lst: list[int]) -> int:
    for i, value in enumerate(lst):
        for different_value in lst[i + 1:]:
            if value % different_value == 0:
                return value // different_value
            elif different_value % value == 0:
                return different_value // value

    return 0

def main(s: str) -> int:
    result = 0
    lines = spreadsheet_to_matrix(s)

    for line in lines:
        result += list_quotient_sum(line)

    return result

with open('2017/2/input.txt') as f:
    print(main(f.read()))
