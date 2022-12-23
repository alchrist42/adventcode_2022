from pathlib import Path

def print_field(steps):
    row_min = min(x[0] for x in steps)
    row_max = max(x[0] for x in steps)

    col_min = min(x[1] for x in steps)
    col_max = max(x[1] for x in steps)
    n, m = row_max - row_min + 1, col_max - col_min + 1
    hlp = [[" "] * m for _ in range(n)]
    for x, y in steps:
        hlp[x - row_min][y - col_min] = "#"
    for row in hlp:
        print("".join(row))

def solve(data: list[str]):
    H, Ts = [0, 0], [[0, 0] for _ in range(9)]
    steps = set()
    steps.add(tuple(Ts[8]))
    for line in data:
        direct, cnt = line.split()  
        cnt = int(cnt)
        for _ in range(cnt):
            if direct == "R":
                H[1] += 1
            elif direct == "L":
                H[1] -= 1
            elif direct == "U":
                H[0] -= 1
            elif direct == "D":
                H[0] += 1
            # print("H", H, end="\t")
            
            tmp_H = H[:]
            for T in Ts:
                # if abs(T[0] - H[0]) + abs(T[1] - H[1]) > 3:
                #     raise Exception
                if abs(T[0] - H[0]) + abs(T[1] - H[1]) <= 1 or \
                    (abs(T[0] - H[0]) == 1 and abs(T[1] - H[1]) == 1) :
                    # print()
                    break
                if abs(T[0] - H[0]) > 1:
                    if abs(T[1] - H[1]) > 1:
                        T[1] = T[1] + (H[1] - T[1]) // 2
                    else:
                        T[1] = H[1]
                    T[0] = T[0] + (H[0] - T[0]) // 2
                if abs(T[1] - H[1]) > 1:
                    if abs(T[0] - H[0]) > 1:
                        T[0] = T[0] + (H[0] - T[0]) // 2
                    else:
                        T[0] = H[0]
                    T[1] = T[1] + (H[1] - T[1]) // 2
                H = T[:]
            # print("T", Ts[8])

            steps.add(tuple(Ts[8]))
            # print_field(steps)

            H = tmp_H
            # print(steps)
            # print(steps)

        


    res = data # first time we want print result parsing
    print((steps))


    return len(steps)


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




