from pathlib import Path

directions = "RDLT"

def change_directions(old, turn):
    return directions[(directions.find(old) + (-1) ** (turn == "L")) % 4]

def solve(data: list[str]):
    moves = data[-1]
    m = [[ch if ch != " " else False for ch in line] for line in data[:-1]]
    w = max(len(line) for line in data[:-1])
    h = len(m)
    for i in range(h):
        m[i] = m[i] + [False] * (w - len(m[i]))
    # your solution
    pos = [0, 0]
    direct = "R"
    steps = ""
    for ch in moves + "Z":
        if ch.isalpha():
            print(f"old {pos} {direct} steps:{steps}, {ch}")
            if steps:
                cnt_step = int(steps)
                y, x = pos
                new_pos = pos[:]
                if direct in "LR":
                    dx = 1 if direct == "R" else -1
                    dy = 0
                else:
                    dx = 0
                    dy = 1 if direct == "D" else -1
                while cnt_step:
                    y  = (y + dy) % h
                    x  = (x + dx) % w
                    if not m[y][x]:
                        continue
                    elif m[y][x] == "#":
                        break
                    # elif m[y][x] == ".":
                    new_pos = [y, x]
                    cnt_step -= 1
                pos = new_pos
                # print("new pois", pos)
                steps = ""
            
            if ch != "Z":
                direct = change_directions(direct, ch)
        else:
            steps += ch
            
    ans = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + directions.find(direct) 




    res = data # first time we want print result parsing

    return pos, ans


path = Path(__file__)
filename = path.name.rstrip(".py").split("_")[0]

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




