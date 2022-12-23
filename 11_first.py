from pathlib import Path


class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.total_items = 0
        self.round_res = 0
        self.check_div = 0
        self.if_true = 0
        self.if_false = 0
        # self.oprt = None
        self.s = ""

    def oprt(self, old):
        return eval(self.s)

    def bored(self, val):
        return val // 3

    def trow_item_to_monkey(self):
        self.total_items += 1
        self.round_res += 1
        item = self.items.pop(0)
        item = self.oprt(item)
        # item = self.bored(item) # second part
        if not item % self.check_div:
            next_monk = self.if_true
        else:
            next_monk = self.if_false
        return item, next_monk


def solve(data: list[str]):
    mnks: list[Monkey] = []
    i = 0
    while i < len(data):
        m = Monkey()
        i += 1
        m.items = [int(x.rstrip(",")) for x in data[i].split()[2:]]
        i += 1
        m.s = data[i].strip()[len("Operation: new = "):]
        i += 1
        m.check_div = int(data[i].split()[-1])
        i += 1
        m.if_true =int(data[i].split()[-1])
        m.if_false =int(data[i + 1].split()[-1])
        i += 2
        mnks.append(m)
    
    def search_seq(results, n=15):
        """Ищет длину повторяющейся последовательности,
         как минимум длиной 10"""
        if len(results) < 50:
            return False
        last = results[-1]
        for i in range(-2, -len(results) + n, -1):
            if results[i] == last and \
                all(results[-1 - j] == results[i - j] for j in range(n)):
                    return -1 - i
        return False

    round_results = [[0] * len(mnks)]
    for round in range(1000):
        for mnk in mnks:
            mnk.round_res = 0
            while mnk.items:
                item, ind_monkey = mnk.trow_item_to_monkey()
                mnks[ind_monkey].items.append(item)
            
        round_res = [mnk.round_res for mnk in mnks]
        round_results.append(round_res)
        if search_seq(round_results):
            print("FOUND", search_seq(round_results), f"round {round}")
            break
        if not round % 50:
            print(round)

        if round == 999:
            assert [m.total_items for m in mnks] == [5204, 4792, 199, 5192]
            # print([m.total_items for m in mnks])

    mnks.sort(reverse=True, key=lambda mnk: mnk.total_items)

    res = mnks[0].total_items * mnks[1].total_items 

    return  res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
# print(solve(my_data))




