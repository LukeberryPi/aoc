import sys

sys.stdout = open("2025/5/log.txt", "w")

def parse(s: str):
    ranges, ingredients = s.split("\n\n")[0].split("\n"), s.split("\n\n")[1].split("\n")
    return [ranges, ingredients]

def main(s: str):
    fresh_ingredients = set()
    ranges, ingredients = parse(s)
    for ing in ingredients:
        inting = int(ing)
        for rang in ranges:
            bot, top = [int(n) for n in rang.split("-")]
            if bot <= inting <= top:
                fresh_ingredients.add(inting)
                continue
    return len(fresh_ingredients)
                

with open('2025/5/input.txt') as f:
    print("part 1 result", main(f.read()))
