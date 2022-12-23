def solve(data):
    res = 0
    pairs = [[list(map(int, x.split("-"))) for x in row.split(",")] for row in data]
    for a, b in pairs:
        # pri5nt(p1, p2)
        if b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] or a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
            res += 1
    return res

    

with open("4_temp.txt") as f:
    example_data = [line.rstrip() for line in f.readlines() if line.rstrip()]
print(solve(example_data))

with open("4.txt") as f:
    my_data = [line.rstrip() for line in f.readlines() if line.rstrip()]
print(solve(my_data))




