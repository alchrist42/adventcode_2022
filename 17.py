from pathlib import Path
from itertools import cycle

figs = [
    [
        [1, 1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]



def solve(data: list[str]):
    moves = data[0]
    cave = [
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    tower = 1 #include floor
    cave_h = len(cave) + 1
    gas_i = 0
    for cnt_fig in range(10):
        fig = figs[cnt_fig % len(figs)]
        pos = [0, 2]
        fig_h = len(fig)
        new_cave_h = tower + 3 + fig_h
        for _ in range(cave_h, new_cave_h + 1):
            cave.insert(0, cave[0][:])
        cave_h = new_cave_h
        while True:
            gas_i %= len(data)
            move = 1 if moves[gas_i] == ">" else -1
            gas_i += 1

            # side moves
            pos[1] += move
            # check
            collision = False
            for y in range(len(fig)):
                for x in range(len(fig[0])):
                    block = fig[y][x]
                    block_in_cave = cave[pos[0] + y][pos[1] + x]
                    if block and block_in_cave:
                        collision = True
                        pos[1] -= move
                        break
                if collision:
                    break
            
            # down movie
            collision = False
            pos[0] += 1
            for y in range(len(fig)):
                for x in range(len(fig[0])):
                    block = fig[y][x]
                    block_in_cave = cave[pos[0] + y][pos[1] + x]
                    if block and block_in_cave:
                        collision = True
                        break
                if collision:
                    break
            if collision:
                move_stop = True
                pos[0] -= 1
                for y in range(len(fig)):
                    for x in range(len(fig[0])):
                        block = fig[y][x]
                        cave[pos[0] + y][pos[1] + x] = block
                for i, line in enumerate(cave):
                    if any(line[1:-1]):
                        first_non_empty_line = i
                tower = len(cave) - first_non_empty_line
                print(f"tower_h = {tower}", *["|".join("#" if cell else " " for cell in line) for line in cave], "\n", sep="\n")
                break
            
            
                







    # your solution
    res = data # first time we want print result parsing

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
# print(solve(my_data))




