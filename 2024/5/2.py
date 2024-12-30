from collections import deque, defaultdict

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
        all_rules_where_both_elements_are_in_the_update = [rule for rule in rules if rule[0] in update and rule[1] in update]
        all_relevant_rule_nodes = set()
        for x, y in all_rules_where_both_elements_are_in_the_update:
            all_relevant_rule_nodes.add(x)
            all_relevant_rule_nodes.add(y)
        graph = defaultdict(list)
        in_degree = {node: 0 for node in all_relevant_rule_nodes}
        for bef, aft in all_rules_where_both_elements_are_in_the_update:
            graph[bef].append(aft)
            in_degree[aft] += 1
        # print(f"original list {update} \n ACTUAL relevant rules {all_rules_where_both_elements_are_in_the_update} \n graph {graph} \n in_degree {in_degree} \n\n")
        # print(f"og update {update} \n all rules where both elements are in the update {all_rules_where_both_elements_are_in_the_update} \n all relevant rule nodes {all_relevant_rule_nodes} \n\n")
        for i, upd in enumerate(update):
            befores = update[:i]
            afters = update[i + 1:]
            relevant_rules = [rule for rule in rules if upd in rule]
            is_invalid = any(rule[0] in afters or rule[1] in befores for rule in relevant_rules)
            if is_invalid:
                valid = False
        if not valid:
            correct_order = []
            q = deque([item for item in all_relevant_rule_nodes if in_degree[item] == 0])
            while q:
                curr = q.popleft()
                correct_order.append(curr)
                for node in graph[curr]:
                    in_degree[node] -= 1
                    if in_degree[node] == 0:
                        q.append(node)
            print(correct_order)
            res += int(correct_order[len(correct_order) // 2])
            # print(f"previous array {update} \n\n correctly ordered array {correct_order} \n\n rules are {relevant_rules} \n\n\n\n")
    return res

with open("2024/5/input.txt") as f:
    print(main(f.read()))

# we have an array of tuples
# each tuple has nodes (x, y) where x must precede y
# create graph[x] = [y1, y2, ...]
# graph[node] = elements that must come after it
# in_degree is a dictionary
# in_degree[y] = number of elements that must precede it
# initialize empty array to place items in correct order
# initialize queue with any y where in_degree[y] == 0 (no elements must come before it, so it is the first element)
# while there is a queue
# pop the left value and append it to the correctly ordered array
# since the value has left the queue, subtract the in_degree of all the elements that must come after it by 1
# if there's any in_degree == 0, append it to the queue