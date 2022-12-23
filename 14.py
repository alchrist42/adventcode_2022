from pathlib import Path
from collections import defaultdict

    
def solve(data: list[str]):
    h = [[0] * 1000 for _ in range(300)]
    floor = 0
    for line in data:
        points = [list(map(int, point.split(","))) for point in line.split()[::2]]
        for i in range(1, len(points)):
            a, b = points[i - 1: i + 1]
            if a[0] == b[0]: #vertical line
                x = a[0]
                floor = max(floor, max(a[1], b[1]) + 2)
                for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                    
                    h[y][x] = 1
            else:
                y = a[1]
                floor = max(floor, y + 2)
                for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    h[y][x] = 1
    for x in range(1000): # for part 2
        h[floor][x] = 1
    # print(floor)
    # print(h)

    drops = []
    drops_cnt = 0
    drop = None
    for drop_moves in range(10 ** 10):
        if drop is None:
            drop = [500, 0]
            if h[0][500]: # solution part 2
                return drops_cnt
            drops_cnt += 1
        x, y = drop
        if y == 299: # solution part 1
            return drops_cnt - 1
        if not h[y + 1][x]:
            # round += h[x] - y
            drop = [x, y + 1]
        elif not h[y + 1][x - 1]:
            # round += 1
            drop = [x - 1, y + 1]
        elif not h[y + 1][x + 1]:
            # round += 1
            drop = [x + 1, y + 1]
        else:
            h[y][x] = 1
            drops.append(drop)
            drop = None

        



    res = data # first time we want print result parsing

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




