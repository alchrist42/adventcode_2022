import string

def solve(data):
    res = 0
    for row in data:
        r1, r2 = row[:len(row)//2], row[len(row)//2:]
        ch = (set(r1) & set(r2)).pop()
        if ch in string.ascii_lowercase:
            n_ch = ord(ch) - ord("a") + 1
        else:
            n_ch = 27 + ord(ch) - ord("A")
        res += n_ch
        # print(n_ch)

    return res



with open("3_temp.txt") as f:
    example_data = [line.rstrip() for line in f.readlines()]
print(solve(example_data))

with open("3.txt") as f:
    my_data = [line.rstrip() for line in f.readlines()]
print(solve(my_data))

