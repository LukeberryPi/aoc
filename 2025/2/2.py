import sys

sys.stdout = open("2025/2/log.txt", "w")

def parse(s: str) -> list[tuple[str, ...]]:
    return [tuple(scope.split("-")) for scope in s.split(",")]

def main(s: str) -> int:
    scopes = parse(s)
    invalid_id_sum = 0
    for bottom, top in scopes:
        rang = range(int(bottom), int(top) + 1)
        for num in rang:
            print("num", num)
            strnum = str(num)
            id_length = len(strnum)
            current = ""
            for char in strnum:
                current += char
                current_length = len(current)
                print("current", current)
                if current_length > id_length // 2:
                    print("skipping because sequence is too big and no repeat", current)
                    break
                quotient, remainder = divmod(id_length, current_length)
                if quotient and not remainder and current * quotient == strnum:
                        print("number got added", num)
                        invalid_id_sum += num
                        break
    return invalid_id_sum

with open('2025/2/input.txt') as f:
    print("part 2 result", main(f.read()), "\n")
