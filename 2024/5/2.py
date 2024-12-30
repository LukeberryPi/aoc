from collections import deque, defaultdict
from typing import List, Tuple

def parse_rules(s: str) -> List[Tuple[str, ...]]:
    spl = s.split("\n\n")[0]
    return [tuple(rule.split("|")) for rule in spl.split("\n")]

def parse_updates(s: str) -> List[List[str]]:
    spl = s.split("\n\n")[1]
    return [update.split(",") for update in spl.split("\n")]

def main(s: str) -> int:
    res = 0
    rules = parse_rules(s)
    updates = parse_updates(s)
    for update in updates:
        for i, upd in enumerate(update):
            befores = update[:i]
            afters = update[i + 1:]
            relevant_rules = [rule for rule in rules if upd in rule and (rule[0] and rule[1]) in update]
            all_rule_nodes = set()
            is_invalid = any(rule[0] in afters or rule[1] in befores for rule in relevant_rules)
            if is_invalid:
                all_rule_nodes = set()
                for bef, aft in relevant_rules:
                    all_rule_nodes.add(bef)
                    all_rule_nodes.add(aft)
                graph = defaultdict(list)
                in_degree = {node: 0 for node in all_rule_nodes}
                for bef, aft in relevant_rules:
                    graph[bef].append(aft)
                    in_degree[aft] += 1
                # print(f"""update {update} \n\n graph {graph} \n\n in_degree {in_degree} \n\n\n\n""")
                correct_order = []
                q = deque([item for item in update if in_degree[item] == 0])
                while q:
                    curr = q.popleft()
                    correct_order.append(curr)
                    for node in graph[curr]:
                        in_degree[node] -= 1
                        if in_degree[node] == 0:
                            q.append(node)
                print(f"previous array {update} \n\n correctly ordered array {correct_order} \n\n rules are {relevant_rules} \n\n\n\n")
                res += int(correct_order[len(correct_order) // 2])
    return res

with open("2024/5/input.txt") as f:
    print(main(f.read()))