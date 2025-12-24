import sys

sys.stdout = open("2025/5/log.txt", "w")

def parse(s: str):
    ranges = s.split("\n\n")[0].split("\n")
    return ranges

def main(s: str):
    ranges = parse(s)
    result = 0
    tuples = []
    for rang in ranges:
        start, end = [int(n) for n in rang.split("-")]
        tuples.append((start, end))
    tuples.sort()
    cur_start, cur_end = tuples[0]
    for tup in tuples[1:]:
        start, end = tup
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            result += cur_end - cur_start + 1
            cur_start, cur_end = start, end
    result += cur_end - cur_start + 1 
    return result
            

with open('2025/5/input.txt') as f:
    print("part 2 result", main(f.read()))
