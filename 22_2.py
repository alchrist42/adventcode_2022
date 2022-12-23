from pathlib import Path
from time import sleep

directions = "RDLU"
dct = {a: b for a, b in zip("RDLU", ">v<^")}

def change_directions(old, turn):
    return directions[(directions.find(old) + (-1) ** (turn == "L")) % 4]

def solve(data: list[str], model="temp"):
    moves = data[-1]
    m = [[ch if ch != " " else False for ch in line] for line in data[:-1]]
    w = max(len(line) for line in data[:-1])
    h = len(m)
    edge = max(h, w) // 4
    for i in range(h):
        m[i] = m[i] + [False] * (w - len(m[i]))
    # your solution
    if model == "temp":
        pos = [0, 2 * edge]
    else:
        pos = [0, edge]
    direct = "R"
    steps = ""
    for ch in moves + "Z":
        if ch.isalpha():
            if steps:
                cnt_step = int(steps)
                y, x = pos
                new_pos = pos[:]
                new_direct = direct
                
                while cnt_step:
                    if direct in "LR":
                        dx = 1 if direct == "R" else -1
                        dy = 0
                    else:
                        dx = 0
                        dy = 1 if direct == "D" else -1
                    y  = (y + dy) % h
                    x  = (x + dx) % w
                    if model == "temp" and (not m[y][x] or (2 * edge <= x < 3 * edge and ((y == 0 and dy == 1) or (y == 3 * edge - 1 and dy == -1)))):
                        if x == edge * 2 - 1 and direct == "L":
                            if y < edge:
                                y, x = edge, x - (edge - y)
                                direct = "D"
                            elif y >= edge * 2:
                                y, x = edge * 2 - 1, x - (y - edge * 2)
                                direct = "U"
                        elif x == edge * 3 and direct == "R":
                            if y < edge:
                                y, x = 3 * edge - 1 - y, 3 * edge - 1
                                direct = "L"
                            elif edge <= y < 2 * edge:
                                y, x = 2 * edge, edge * 3 + (2 * edge - y - 1)
                                direct = "D"
                        elif x == 4 * edge - 1 and direct == "L":
                            y, x = 3 * edge - 1, edge * 3 + (2 * edge - y - 1)
                            direct = "U"
                        elif x == 0 and direct == "R":
                            y, x = 3 * edge - y - 1, 3 * edge - 1
                        # down and up
                        elif y == edge - 1 and direct == "U":
                            if x < edge:
                                y, x = 0, 3 * edge - x - 1
                                direct = "D"
                            elif edge <= x < 2 * edge:
                                y, x = edge - (2 * edge - x), 2 * edge
                                direct = "R"
                        elif y == edge * 2 and direct == "D":
                            if x < edge:
                                y, x = 3 * edge - 1, 3 * edge - x - 1
                                direct = "U"
                            elif edge <= x < 2 * edge:
                                y, x = edge * 2 + (x - edge), 2 * edge
                                direct = "R"
                        elif y == 0 and dy == 1:
                            if 2 * edge <= x < 3 * edge:
                                y, x = 2 * edge - 1, 3 * edge - x - 1
                                direct = "U"
                            elif x >= edge * 3:
                                y, x = edge + (4 * edge -x - 1), 0
                                direct = "R"
                        elif y == 3 * edge - 1 and dy == -1:
                            y, x = edge, 3 * edge - x - 1
                            direct = "D"
                        elif y == 2 * edge - 1 and direct == "U":
                            y, x = 2 * edge - (x - 3 * edge + 1)
                            direct = "L"

                    if model == "main" and not m[y][x]:
                        if x == edge - 1 and direct == "L":
                            if y < edge:
                                y, x = 2 * edge + edge - y - 1, 0
                                direct = "R"
                            else:
                                y, x = 2 * edge, y - edge
                                direct = "D"
                        elif x == 0  and direct == "R":
                            y, x = 3 * edge - y - 1, 2 * edge - 1
                            direct = "L"
                        elif x == 2 * edge and direct == "R":
                            if y < edge * 2:
                                y, x = edge - 1, edge + y
                                direct = "U"
                            else:
                                y, x = 3 * edge - y - 1, 3 * edge - 1
                                direct = "L"
                        elif x == edge and direct == "R":
                            y, x = 3 * edge - 1, edge + y - 3 * edge
                            direct = "U"
                        elif x == 3 * edge - 1 and direct == "L":
                            if y < edge * 3:
                                y, x = edge * 3 - y - 1, edge
                                direct = "R"
                            else:
                                y, x = 0, edge + y - edge * 3
                                direct = "D" 

                        # by y
                        elif y == 0 and direct == "D":
                            x += edge * 2
                        elif y == 2 * edge - 1 and direct == "U":
                            y, x = edge + x, edge
                            direct = "R"
                        elif y == 4 * edge - 1 and direct == "U":
                            if x < edge * 2:
                                y, x = 3 * edge + x - edge, 0
                                direct = "R"
                            else:
                                x -= edge * 2
                        elif y == edge * 3 and direct == "D":
                            y, x = 3 * edge + x - edge, edge - 1
                            direct = "L"
                        elif y == edge and direct == "D":
                            y, x = edge + x - 2 * edge, edge * 2 - 1
                            direct = "L"

                    if m[y][x] == "#":
                        break
                    if not m[y][x]:
                        pass
                    m[y][x] = dct[direct]

                    # elif m[y][x] == ".":
                    new_pos = [y, x]
                    new_direct = direct
                    print(*[' '.join(x if x else ' ' for x in line) for line in m], sep="\n", end="\n\n")
                    sleep(0.15)
                    cnt_step -= 1
                pos = new_pos
                direct = new_direct
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

# print(solve(example_data))
print(solve(my_data, model="main"))




