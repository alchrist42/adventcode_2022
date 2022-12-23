from pathlib import Path
from queue import PriorityQueue
from dataclasses import dataclass, field
from collections import namedtuple


Pos = namedtuple("Pos", "row col")

@dataclass(order=True)
class PriItem:
    priority: int
    # priority: field(compare=False)
    cur: field(compare=False)
    moves: field(compare=False)
    # moves: int

def evristic(a: Pos, b: Pos, m: list[list[int]]) -> int:
    dst = 0
    dif_height =  0

    dst = abs(a.row - b.row) + abs(a.col - b.col)
    dif_height = m[b.row][b.col] -  m[a.row][a.col]
    priority = max(dst, dif_height)
    if priority == 0 and (a.row != b.row or a.col != b.col):
        raise Exception
    return priority

def solve(data: list[str]):
    rows, cols = len(data), len(data[0])
    m = [[0] * cols for _ in range(rows)]
    passed = [[10**10] * cols for _ in range(rows)]
    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch == "S":
                start = Pos(row, col)
                m[row][col] = 0
            elif ch == "E":
                end = Pos(row, col)
                m[row][col] = ord("z") - ord("a")
            else:
                m[row][col] = ord(ch) - ord("a")


    res = 10 ** 10
    while True:
        start = None
        for row, line in enumerate(m):
            for col, height in enumerate(line):
                if height == 0 and passed[row][col] != 0: # search not started from a pos
                    start = Pos(row, col)
                    break
            if start is not None:
                break
        else:
            break
            
        print(f"start from a {start} ", end = "")
        
        steps = PriorityQueue()
        steps.put(PriItem(evristic(start, end, m), start, 0))
        passed[start.row][start.col] = 0

        for checks in range(10**10):
            if steps.empty():
                print()
                break
            step: PriItem  = steps.get()
            if step.cur.row == end.row and step.cur.col == end.col:
                print(step.moves, checks)
                res = min(res, step.moves)
                break
            cur, moves = step.cur, step.moves
            # print(f"check {cur}. dst={step.priority}")

            possitions = []
            if cur.row:
                possitions.append(Pos(cur.row - 1, cur.col))
            if cur.row + 1 != rows:
                possitions.append(Pos(cur.row + 1, cur.col))
            if cur.col:
                possitions.append(Pos(cur.row, cur.col - 1))
            if cur.col + 1 != cols:
                possitions.append(Pos(cur.row, cur.col + 1))

            for pos in possitions:
                if m[pos.row][pos.col] - m[cur.row][cur.col] > 1 \
                        or moves + 1 >= passed[pos.row][pos.col]:
                    continue
                passed[pos.row][pos.col] = moves + 1
                steps.put(PriItem(evristic(pos, end, m) + moves, pos, moves + 1))
            if not checks % 1000:
                print(".", end="")
                



    # res = data # first time we want print result parsing

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




