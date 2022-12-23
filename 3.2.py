import string

def solve(data):
    res = 0
    groups = [data[i:i +3] for i in range(0, len(data), 3)]
    for group in groups:
        sets = [set(elf) for elf in group]
        unic = sets[0] & sets[1] & sets[2]
        ch = unic.pop()
        if ch in string.ascii_lowercase:
            n_ch = ord(ch) - ord("a") + 1
        else:
            n_ch = 27 + ord(ch) - ord("A")
        res += n_ch
        # print(n_ch)2

    return res



with open("3_temp.txt") as f:
    example_data = [line.rstrip() for line in f.readlines()]
print(solve(example_data))

with open("3.txt") as f:
    my_data = [line.rstrip() for line in f.readlines()]
print(solve(my_data))

