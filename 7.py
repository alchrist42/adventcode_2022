from pathlib import Path

total_sizes = []

def solve(data: list[str]):
    root = {}
    root[0] = root #parent
    cur = root
    parent = None
    i = 0
    while i < len(data):
        pref, oper, *arg = data[i].split()
        if pref != "$":
            raise Exception("huy")
        if oper == "ls":
            i += 1
            while i < len(data) and data[i][0] != "$":
                size, name = data[i].split()
                if size == "dir":
                    if name not in cur:
                        cur[name] = (1, {0: cur})
                else:
                    size = int(size)
                    cur[name] = (0, size)
                i += 1
        else:
            arg = arg[0]
            if arg == "/":
                cur = root
            elif arg == "..":
                cur = cur[0]
            else:
                if arg not in cur:
                    cur[arg] = (0, {0: cur})
                cur = cur[arg][1]
            i += 1



    def rec_dir(folder: dict, tab=0):
        size = 0
        global total_sizes
        for key, val in folder.items():
            if key == 0:
                continue
            if val[0] == 0: #file
                size += val[1]
                # print ("    " * tab, key, val[1])
            elif val[0] == 1: #folder
                # print ("    " * tab, key)
                size_dir = rec_dir(val[1], tab + 1)
                size += size_dir
            
        total_sizes.append(size)
        return size

    
    res = rec_dir(root)
    need_to_del = 30000000 - (70000000 - res)
    total_sizes.sort()
    for size in sorted(total_sizes):
        if size > need_to_del:
            return size



    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




