from pathlib import Path

def solve(data: list[str]):
    row = data[0]
    for i in range(len(row) - 14):
        if len(set(row[i:i + 14])) == 14:
            return i + 14

    return -1


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




