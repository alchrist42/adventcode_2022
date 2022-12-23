from pathlib import Path

directs = [
    [
        (-1, -1), (-1, 0), (-1, 1) # north
    ],
    [
        (1, -1), (1, 0), (1, 1) # south
    ],
    [
        (-1, -1), (0, -1), (1, -1) # west
    ],
    [
        (-1, 1), (0, 1), (1, 1) # east
    ]
]
NEAREST = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

EXPAND = 100

def solve(data: list[str]):
    h, w = len(data) + EXPAND * 2, len(data[0]) + EXPAND * 2
    m = [[0] * w for _ in range(h)]

    elf_cnt = 1
    
    min_x, max_x = w, 0
    min_y, max_y = h, 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                min_x = min(min_x, x + EXPAND)
                max_x = max(max_x, x + EXPAND)
                min_y = min(min_y, y + EXPAND)
                max_y = max(max_y, y + EXPAND)
                m[y + EXPAND][x + EXPAND] = elf_cnt
                elf_cnt += 1
    # for line in m:
    #     print(''.join(str(ch) if ch else "." for ch in line))
    # print()


    for _ in range(100000):
        first = 0
        new_positions = {}
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                val = m[y][x]
                if not val:
                    continue
                min_x = min(min_x, x - 1)
                max_x = max(max_x, x + 1)
                min_y = min(min_y, y - 1)
                max_y = max(max_y, y + 1)
                if not any(m[y + i][x + j] for i, j in NEAREST):
                    new_positions[(y, x)] = val
                    continue
                first += 1
                    
                for n, pairs in enumerate(directs):
                    if any(m[y + i][x + j] for i, j in pairs):
                        continue
                    # found good direct
                    
                    dy, dx = pairs[1]
                    new_y, new_x = y + dy, x + dx
                    if (new_y, new_x) not in new_positions:
                        new_positions[(new_y, new_x)] = val
                    else:
                        new_positions[(y, x)] = val
                        # return back 2th elfa
                        val_2 = new_positions.pop((new_y, new_x)) 
                        new_positions[(y + 2 * dy, x + 2 * dx)] = val_2
                    break
                else: # no any free directions
                    new_positions[(y, x)] = val
                    continue
        if not first:
            print('no any moves')
            return _ + 1
            break
        if not _ % 100:
            print(first)
        directs.append(directs.pop(0))
        
        # print(new_positions)
        m = [[0] * w for _ in range(h)]
        for (y, x), val in new_positions.items():
            m[y][x] = val
        # for line in m:
        #     print(''.join("#" if ch else "." for ch in line))
        # print()
    
    min_x, max_x = w, 0
    min_y, max_y = h, 0
    ans = h * w
    for y in range(h):
        for x in range(w):
            if m[y][x]:
                ans -= 1
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    
    ans -= w * min_y
    ans -= w * (h - max_y - 1)
    ans -= (max_y - min_y + 1) * min_x
    ans -= (max_y - min_y + 1) * (w - max_x - 1)

    return ans


path = Path(__file__)
filename = path.name.rstrip(".py").split("_")[0]

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




