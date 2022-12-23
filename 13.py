from pathlib import Path
import functools

def my_compare(a, b):
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for i in range(len(a)):
        if i == len(b): # b end
            return False
        x, y = a[i], b[i]
        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return True
            if x > y:
                return False
        else:
            res = my_compare(x, y)
            if res is not None:
                return res

    if len(a) < len(b):
        return True
    return None

def compare_for_sort(a, b):
    res =  my_compare(a, b)
    if res:
        return -1
    elif res is None:
        return 0
    else:
        return 1

def solve(data: list[str]):

    res1 = 0
    for i in range(0, len(data), 2):
        a, b = eval(data[i]), eval(data[i + 1])
        if my_compare(a, b):
            res1 += i // 2 + 1


    lst = [eval(line) for line in data]
    d1, d2 = [[2]], [[6]]
    lst.extend([d1, d2])
    lst.sort(key=functools.cmp_to_key(compare_for_sort))
    print(*lst, sep="\n")

    res2 = (lst.index(d1) + 1) * (lst.index(d2) + 1)

    return res1, res2
 

path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




