from pathlib import Path

KK4 = 4000000

def solve(data: list[str]):
    sb = []
    for line in data:
        line = line.split()
        sx, sy, bx, by = line[2], line[3], line[-2], line[-1]
        sx = int(sx[2: -1])
        sy = int(sy[2: -1])
        bx = int(bx[2: -1])
        by = int(by[2:])
        sb.append([sx, sy, bx, by])
        print(bx, by, sx, sy)
    
    ans1= set()
    becans_in_row1 = set()
    ans2 = set()
    becans_in_row2 = set()
    for board in [KK4]:
        h = [[] for _ in range(board)]
        for n_row, (sx, sy, bx, by) in enumerate(sb):
            print(".", end="")
            mnht_dst = abs(sx - bx) + abs(sy - by)
            print(f"({n_row})mnh {mnht_dst}, range ({max(0, sy - mnht_dst), min(board, sy + mnht_dst + 1)})")
            for row in range(max(0, sy - mnht_dst), min(board, sy + mnht_dst + 1)):
                otr = h[row]
                dst_to_row1 = abs(row - sy)
                ost1 = mnht_dst - dst_to_row1
                l, r = max(0, sx - ost1), min(board, sx + ost1)
                otr.append((l, r))
        print()
        for y, otr in enumerate(h):
            otr.sort()
            _, r = otr[0] # забиваем что ответ может быть первым или последним элементом строки
            for l, new_r in otr[1:]:
                if l - r > 1: # FOUND
                    print(f"FOUND HOLE {y}, {l - 1}")
                    print(f"ans({board}) = {(l - 1) * KK4 + y}")
                r = max(r, new_r)


    return None


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

# print(solve(example_data))
print(solve(my_data))




