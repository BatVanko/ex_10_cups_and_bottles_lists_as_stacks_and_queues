from collections import deque

wasted_water = 0
cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    difference = current_cup - current_bottle

    if difference > 0:
        cups.appendleft(difference)
    elif difference < 0:
        wasted_water += abs(difference)
if bottles:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles))}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
print(f"Wasted litters of water: {wasted_water}")
