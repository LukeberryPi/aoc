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
        print("current starts at", current)
        amount = int(amount)
        quotient, remainder = divmod(amount, 100)
        if current == 0:
            hits0 += 1
        if direction == "R":
            current += remainder
            if current > 99:
                current -= 100
                hits0 += 1
        if direction == "L":
            current -= remainder
            if current < 0:
                current += 100
                hits0 += 1
        if current == 100:
            current = 0
        print(f"moves {direction} for {amount}")
        hits0 += quotient
        print("current ends at", current)
        print(f"0 has been hit {hits0} times\n")
    return hits0
        

with open('2025/1/sample.txt') as inpt:
    print("result", main(inpt.read()))
