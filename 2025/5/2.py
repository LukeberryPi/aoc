import sys

sys.stdout = open("2025/5/log.txt", "w")

def parse(s: str):
    ranges = s.split("\n\n")[0].split("\n")
    return ranges

def main(s: str):
    fresh = set()
    ranges = parse(s)
    for rang in ranges:
        bot, top = [int(n) for n in rang.split("-")]
        for n in range(bot, top + 1):
            fresh.add(n)
    return len(fresh)
            

with open('2025/5/input.txt') as f:
    print("part 2 result", main(f.read()))
