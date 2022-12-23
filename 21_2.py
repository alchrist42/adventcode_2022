from pathlib import Path

def solve(data: list[str]):
    dct_oper = {}
    dct_vals = {}
    hmn = {"humn": 0}
    for line in data:
        key, val = line.split(": ")
        if val.isdigit():
            dct_vals[key] = int(val)
        else:
            dct_oper[key] = val.split()
        
    goal = None
    while goal is None:
        for_del = set()
        for key, (a_str, oper, b_str) in dct_oper.items():
            if a_str in dct_vals and b_str in dct_vals:
                a, b = dct_vals[a_str], dct_vals[b_str]
                if key == "root":
                    # print(a, b, a_str in hmn, b_str in hmn, len(hmn) == len(set(hmn)))
                    # return hmn
                    if a_str in hmn:
                        goal = b
                    elif b_str in hmn:
                        goal = a
                    else:
                        raise Exception("work only for strath way from human to root")
                    break
                if a_str in hmn:
                    hmn[key] = (a_str, oper, b)
                elif b_str in hmn:
                    hmn[key] = (a, oper, b_str)
                    

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
                
        for key in for_del:
            dct_oper.pop(key)
    
    hmn.pop("humn")
    for key, (a, oper, b) in reversed(hmn.items()):
        # print (key, a, oper, b)
        
        if oper == "+":
            if isinstance(a, str):
                goal -= b
            elif isinstance(b, str):
                goal -= a
            else:
                raise Exception
        elif oper == "-": # goal = a - b
            if isinstance(a, str):
                goal  = goal + b
            elif isinstance(b, str):
                goal = a - goal
            else:
                raise Exception
        elif oper == "*": 
            if isinstance(a, str):
                goal /= b
            elif isinstance(b, str):
                goal /= a
            else:
                raise Exception
        elif oper == "/": # goal = a / b
            if isinstance(a, str):
                goal = goal * b
            elif isinstance(b, str):
                goal = a / goal
            else:
                raise Exception
    res = goal
    return res


path = Path(__file__)
filename = path.name.rstrip(".py").split("_")[0]

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




