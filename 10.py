from pathlib import Path

def solve(data: list[str]):
    line = 0
    tick = 0
    skip = False
    val = 1
    q = [0, 0, 0]
    res = 0
    rows, cols = 6, 40
    display = [["."] * cols for _ in range(rows)]
    while tick < 240:
        val += q[0]
        q = [q[1], 0]
        if not skip:
            row = data[line]
            if row.startswith("addx"):
                skip = True
                q[1] = int(row.split()[1])
            line += 1
        else:
            skip = False

        if abs(val - (tick % cols)) < 2:
            display[tick // cols][tick % cols] = "#"

        tick += 1
        if tick in [20, 60, 100, 140, 180, 220]:
            res += tick * val
            # print(tick, val, res)

    for row in display:
        print("".join(row))

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




