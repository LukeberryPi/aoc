import sys
from collections import deque

sys.stdout = open("2025/3/log.txt", "w")

BATTERY_SIZE = 12

def parse(s: str) -> list[str]:
    return s.splitlines()

def main(s: str) -> int:
    total_joltage = 0
    banks = parse(s)
    for bank in banks:
        final_battery = ""
        window, initial = bank[:-BATTERY_SIZE], bank[-BATTERY_SIZE:]
        current_index = 0
        while len(final_battery) < BATTERY_SIZE:
            largest_window_battery = max([int(bat) for bat in window])
            if largest_window_battery > int(initial[current_index]):
                final_battery += str(largest_window_battery)
                largest_window_battery_index = bank.find(str(largest_window_battery))
                current_index += 1
                window = bank[largest_window_battery_index + 1:-BATTERY_SIZE + current_index]
            else:
                final_battery += initial[current_index:]
        total_joltage += int(final_battery)
    return total_joltage

with open('2025/3/sample.txt') as f:
    print("part 1 result", main(f.read()))

# {battery_value: int, on: bool, seen: bool}
# while not all(seen): recalculate battery

# 811111111111119 -> 811111111119

# bank is 918111111176543
# rest, initial = 918, 111111176543
# is there a number in rest bigger than the first number in initial
# if yes