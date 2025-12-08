import sys

sys.stdout = open("2025/3/log.txt", "w")

def parse(s: str) -> list[str]:
    return s.splitlines()

def main(s: str) -> int:
    total_joltage = 0
    banks = parse(s)
    for bank in banks:
        lst = [int(bat) for bat in bank]
        largest_battery = max(lst)
        largest_battery_index = lst.index(largest_battery)
        if largest_battery_index == len(lst) - 1:
            largest_battery = max(lst[:-1])
            largest_battery_index = lst.index(largest_battery)
        remainder = bank[largest_battery_index + 1:]
        second_largest_battery = max([int(b) for b in remainder])
        highest_joltage = str(largest_battery) + str(second_largest_battery)
        total_joltage += int(highest_joltage)
    return total_joltage

with open('2025/3/input.txt') as f:
    print("part 2 result", main(f.read()))
