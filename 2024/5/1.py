
def parse_rules(s: str) -> list[tuple[str, ...]]:
    spl = s.split("\n\n")[0]
    return [tuple(rule.split("|")) for rule in spl.split("\n")]

def parse_updates(s: str) -> list[list[str]]:
    spl = s.split("\n\n")[1]
    return [update.split(",") for update in spl.split("\n")]

def main(s: str) -> int:
    res = 0
    rules = parse_rules(s)
    updates = parse_updates(s)
    for update in updates:
        valid = True
        for i, upd in enumerate(update):
            befores = update[:i]
            afters = update[i + 1:]
            relevant_rules = [rule for rule in rules if upd in rule]
            is_invalid = any(rule[0] in afters or rule[1] in befores for rule in relevant_rules)
            if is_invalid:
                valid = False
        if valid:
            res += int(update[len(update) // 2])
    return res


with open("2024/5/input.txt") as f:
    print(main(f.read()))
