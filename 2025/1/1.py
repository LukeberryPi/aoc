def parse(s: str) -> list[tuple[str, str]]:
    to_tuples = [(line[:1], line[1:]) for line in s.splitlines()]
    return to_tuples

def main(s: str) -> int:
    tuples = parse(s)
    current = 50
    at0 = 0;
    for (direction, amount) in tuples:
        amount = int(amount)
        if amount > 100:
            amount = amount % 100
        if direction == "R": 
            current += amount
        if direction == "L": 
            current -= amount
        if current >= 100: 
            current -= 100
        if current < 0: 
            current += 100
        if current == 0:
            at0 += 1
    return at0

with open('2025/1/input.txt') as inpt:
    print(main(inpt.read()))

# L436 -> L36