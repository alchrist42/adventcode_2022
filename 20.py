from pathlib import Path

def solve(data: list[str]):
    print(len(data), end= "->")
    data = [(int(x), i) for i, x in enumerate(data)]
    print(len(set(data)))
    print(sorted(data)[:20])
    res = data # first time we want print result parsing
    shifts = [0] * len(data)
    cpy = data[:]
    i = ind = 0
    while ind != len(data):
        while data[i][1] != ind:
            i += 1
        x = data[i][0]
        new_pos = (i + x) % len(data)
        if i + x < 0:
            new_pos -= 1
        # print(i, x, new_pos)
        # if new_pos > i:
        #     new_pos += 1
        data.insert(new_pos, data.pop(i))
        ind += 1
        # print([dig for dig, _ in data])



    return None


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

# print(solve(example_data))
print(solve(my_data))




