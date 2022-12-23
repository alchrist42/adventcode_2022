with open("1.txt") as f:
    dataf = f.readlines()

lst = []
sm = 0
for line in dataf:
    line = line.rstrip("\n")
    if not line:
        lst.append(sm)
        sm = 0
    else:
        sm += int(line)

print(sum(sorted(lst)[-3:]))


