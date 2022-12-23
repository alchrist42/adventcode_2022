from pathlib import Path

def solve(data: list[str]):
    n, m = len(data), len(data[0])
    grid = [list(map(int, row)) for row in data]
    hlp = [[None] * m for _ in range(n)]
    for i in range(n):
        mx1, mx2 = grid[i][0], grid[i][-1]
        hlp[i][0] = hlp[i][-1] = False
        for j in range(m):
            if grid[i][j] <= mx1 and (hlp[i][j] is None or hlp[i][j] == True):
                hlp[i][j] = True
            else:
                hlp[i][j] = False
            mx1 = max(mx1, grid[i][j])
            if grid[i][-j -1] <= mx2 and (hlp[i][-j - 1] is None or hlp[i][-j - 1] == True):
                hlp[i][-j -1] = True
            else:
                hlp[i][-j -1] = False
            mx2 = max(mx2, grid[i][-j - 1])
    for j in range(n):
        mx1, mx2 = grid[0][j], grid[-1][j]
        hlp[0][j] = hlp[-1][j] = False
        for i in range(m):
            if grid[i][j] <= mx1 and (hlp[i][j] is None or hlp[i][j] == True):
                hlp[i][j] = True
            else:
                hlp[i][j] = False
            mx1 = max(mx1, grid[i][j])

            if grid[-i - 1][j] <= mx2 and (hlp[i][j] is None or hlp[-i -1][j] == True):
                hlp[-i - 1][j] = True
            else:
                hlp[-i - 1][j] = False
            mx2 = max(mx2, grid[-i - 1][j])
    
    res = sum(sum(x for x in row) for row in hlp)
    # return n * m - res #part 1
    
    # part 2
    hlp = [[[None] * 4 for j in range(m)] for i in range(n)]
    for i in range(n):
        mx1, mx2 = {x:0 for x in range(10)}, {x:-1 for x in range(10)}
        for j in range(m):
            pos = max(pos for key, pos in mx1.items() if key >= grid[i][j])
            hlp[i][j][0] = j - pos
            mx1[grid[i][j]] = j
            pos = min(pos for key, pos in mx2.items() if key >= grid[i][-j-1])
            hlp[i][-j-1][1] = pos + j + 1
            mx2[grid[i][-j-1]] = -j - 1
    for j in range(n):
        mx1, mx2 = {x:0 for x in range(10)}, {x:-1 for x in range(10)}
        for i in range(m):
            pos = max(pos for key, pos in mx1.items() if key >= grid[i][j])
            hlp[i][j][2] = i - pos
            mx1[grid[i][j]] = i
            pos = min(pos for key, pos in mx2.items() if key >= grid[-i - 1][j])
            hlp[-i -1][j][3] = pos + i + 1
            mx2[grid[-i -1][j]] = -i - 1

    res = 0
    for row in hlp:
        for x in row:
            res = max(res, x[0] * x[1] * x[2] * x[3])
            if res == 45:
                pass

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




