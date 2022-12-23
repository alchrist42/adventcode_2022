def solve(data):


    return res

    

with open("4_temp.txt") as f:
    example_data = [line.rstrip() for line in f.readlines() if line.rstrip()]
with open("4.txt") as f:
    my_data = [line.rstrip() for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))

