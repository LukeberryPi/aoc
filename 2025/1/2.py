import sys

sys.stdout = open('2025/1/log.txt', 'w')

def parse(s: str) -> list[tuple[str, str]]:
    to_tuples = [(line[:1], line[1:]) for line in s.splitlines()]
    return to_tuples

def main(s: str) -> int:
    tuples = parse(s)
    current = 50
    hits0 = 0;
    for (direction, amount) in tuples:
        amount = int(amount)

        print("old", current)
        print(direction, amount)

        if direction == "R":
            current += amount
            if current > 99 and current != 100:
                hits0 += 1
                current -= 100
        if direction == "L":
            current -= amount
            if current < 0:
                hits0 += 1
                current += 100
            
        print("new", current)
        print("")
        print("hits", hits0)
        print("\n")

    return hits0
        

with open('2025/1/input.txt') as inpt:
    print("result", main(inpt.read()))
