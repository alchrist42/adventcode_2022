with open("2.txt") as f:
    dataf = f.readlines()

def fnc (a, b):
    # add for 2 task
    # print(f"get {a}, mode {b}", end=" ")
    # b = (a + b + 2) % 3
    # print(f"choise {b}")

    res = b + 1
    res += 3 * ((b - a + 1) % 3)
    return res

sm = 0
for  line in dataf:
    a, b = map(ord, line.split())
    a -= ord("A")
    b -= ord("X")
    sm += fnc(a, b)
    

print(sm)

