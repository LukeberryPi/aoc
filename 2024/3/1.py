import re

def main(s: str):
    reg = "mul\(\d{1,3},\d{1,3}\)"
    ops = re.findall(reg, s)
    res = 0
    for op in ops:
        spl = op.split("(")[1][:-1]
        a, b = spl.split(",")
        res += int(a) * int(b)
    return res

with open('2024/3/input.txt') as f:
    print(main(f.read()))