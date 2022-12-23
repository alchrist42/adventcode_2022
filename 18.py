from pathlib import Path

def solve(data: list[str]):
    data = [list(map(int, line.split(","))) for line in data]
    mx = max([line[0] for line in data]) + 3
    my = max([line[1] for line in data]) + 3
    mz = max([line[2] for line in data]) + 3

    h = [[[False] * mz for y in range(my)] for x in range (mx)]
    for x, y, z in data:
        h[x+1][y+1][z+1] = True

    cache=set()
    cache.add((0, 0, 0))
    while cache:
        (x, y, z) = cache.pop()
        h[x][y][z] = -1
        for i,j,l in [(0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            dx = x + i
            dy = y + j

            dz = z + l
            # print(dx, dy, dz)
            if dx >= 0 and dy >= 0 and dz >= 0 and dx < mx and dy < my and dz < mz:
                # print("check", dx,  dy, dz, h[dx][dy][dz])
                if h[dx][dy][dz] == 0:
                    cache.add((dx, dy, dz))
            # print(cache)
    
    ans = 0
    for x in range(1, mx):
        for y in range(1, my):
            for z in range(1, mz):
                ans += h[x][y][z] - h[x][y][z-1] == 2
                ans += h[x][y][-z-1] - h[x][y][-z] == 2
    for x in range(1, mx):
        for z in range(1, mz):
            for y in range(1, my):
                ans += h[x][y][z] - h[x][y - 1][z] == 2
                ans += h[x][-y -1][z] - h[x][-y][z]==2
    for z in range(1, mz):
        for y in range(1, my):
            for x in range(1, mx):
                ans += h[x][y][z] - h[x - 1][y][z]==2
                ans += h[-x - 1][y][z] - h[-x][y][z]==2



    # your solution
    res = data # first time we want print result parsing

    return ans


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




