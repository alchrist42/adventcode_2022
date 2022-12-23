from pathlib import Path

def solve(data: list[str]):
    dct_oper = {}
    dct_vals = {}
    for line in data:
        key, val = line.split(": ")
        if val.isdigit():
            dct_vals[key] = int(val)
        else:
            dct_oper[key] = val.split()
        
    while True:
        for_del = set()
        for key, (a, oper, b) in dct_oper.items():
            if a in dct_vals and b in dct_vals:
                a, b = dct_vals[a], dct_vals[b]
                if oper == "+":
                    val = a + b
                elif oper == "-":
                    val = a - b
                elif oper == "*":
                    val = a * b
                elif oper == "/":
                    val = a / b
                else:
                    raise Exception
                dct_vals[key] = val
                for_del.add(key)
                if key == "root":
                    return val
        for key in for_del:
            dct_oper.pop(key)
    # your solution
    res = dct_oper # first time we want print result parsing

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




