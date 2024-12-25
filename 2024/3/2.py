import re

# store index for all do()
# store index for all don't()
# perform operations only if some index(do) < op < next index(don't)

def main(s: str):
    res = 0
    regdo = "do()"
    regdont = "don't()"
    regmul = "mul\(\d{1,3},\d{1,3}\)"
    dopos = [pos.end() for pos in re.finditer(regdo, s)]
    dontpos = [pos.end() for pos in re.finditer(regdont, s)]
    muls = [mul for mul in re.finditer(regmul, s)]
    disallowed_ranges = [(dont, next((do for do in dopos if do > dont), float("inf"))) for dont in dontpos]
    for mul in muls:
        is_disallowed = any(mul.start() > start and mul.start() < end for [start, end] in disallowed_ranges)
        if is_disallowed: continue
        spl = mul.group().split("(")[1][:-1]
        a, b = spl.split(",")
        res += int(a) * int(b)
    return res

with open('2024/3/input.txt') as f:
    print(main(f.read()))