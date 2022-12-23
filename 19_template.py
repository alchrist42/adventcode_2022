from pathlib import Path
from time import time

def solve(data: list[str]):
    # your solution
    res = data # first time we want print result parsing

    return res


path = Path(__file__)
filename = path.name.rstrip(".py").split("_")[0]

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

start = time()
print(solve(example_data))
mid = time()
print("time_temp" , mid - start)
# print(solve(my_data))
print("time_main", time() - mid)




