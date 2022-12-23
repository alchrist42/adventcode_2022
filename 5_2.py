def solve(data):
    for  i in range(len(data)):
        if data[i][1].isnumeric():
            step_i = i
            break

    ln = len(data[0])
    n = (ln + 1) // 4
    stacks = [[] for _ in range(n)]
    for i in range(step_i - 1, -1, -1):
        row = data[i]
        for j in range(1, ln, 4):
            if row[j] != " ":
                stacks[j // 4].append(row[j])

    for move in data[step_i + 1:]:
        (_, cnt, _, a, _, b) = move.split()
        cnt, a, b = map(int, [cnt, a, b])
        a -= 1
        b -= 1

        stacks[b].extend(stacks[a][-cnt:])
        stacks[a] = stacks[a][:-cnt]

    res = "".join(col[-1] for col in stacks if col)
    # res = 1
    return res

    

with open("5_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
print(solve(example_data))

with open("5.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
print(solve(my_data))




