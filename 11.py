from pathlib import Path
import itertools

CORRECT = {1: [2, 4, 3, 6], 20: [99, 97, 8, 103], 1000: [5204, 4792, 199, 5192]}

class Banana():
    total_bananas = 0

    def __init__(self, val, monkey_ind) -> None:
        self.ind_banana = Banana.total_bananas
        Banana.total_bananas += 1
        self.val = val
        self.monkeys = [monkey_ind]
        self.have_loop = False

    def search_loop(self, n=200):
        """Ищем не заклился ли банан в хождении по обезьянкам, как минимум хвост длинной N должен повториться"""
        if len(self.monkeys) < n * 2 + 2:
            return False
        last = self.monkeys[-1]
        for i in range(-2, -n, -1):
            if self.monkeys[i] == last and \
                    all(self.monkeys[-1 - j] == self.monkeys[i - j] for j in range(n)):
                print(f"found loop for banana {self.ind_banana}, len = {-i-1}, len_val = len(str(self.val))")
                print(self.monkeys[2 * i + 2: i + 1])
                print(self.monkeys[i + 1:])

                self.have_loop = True
                loop = self.monkeys[-i:]
                self.gen_loop = itertools.cycle(loop)
                return
        return False
        


class Monkey:
    def __init__(self) -> None:
        self.items: list[Banana] = []
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
        if item.have_loop: # we found loop for banana and haven't search next val
            return item, next(item.gen_loop)

        item.val = self.oprt(item.val)
        # item = self.bored(item) # second part
        if not item.val % self.check_div:
            next_monk = self.if_true
        else:
            next_monk = self.if_false
        item.monkeys.append(next_monk)
        item.search_loop()
        return item, next_monk




def solve(data: list[str]):
    mnks: list[Monkey] = []
    i = 0
    while i < len(data):
        m = Monkey()
        i += 1
        m.items = [Banana(int(x.rstrip(",")), monkey_ind=len(mnks)) for x in data[i].split()[2:]]
        i += 1
        m.s = data[i].strip()[len("Operation: new = "):]
        i += 1
        m.check_div = int(data[i].split()[-1])
        i += 1
        m.if_true =int(data[i].split()[-1])
        m.if_false =int(data[i + 1].split()[-1])
        i += 2
        mnks.append(m)
    
    def search_seq(results, n=10):
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
    for round in range(1, 10001):
        for mnk in mnks:
            mnk.round_res = 0
            while mnk.items:
                item, ind_monkey = mnk.trow_item_to_monkey()
                mnks[ind_monkey].items.append(item)
            
        round_res = [mnk.round_res for mnk in mnks]
        round_results.append(round_res)
        # if search_seq(round_results):
        #     print("FOUND", search_seq(round_results), f"round {round}")
        #     break
        if not round % 50:
            print(round)

        if round in CORRECT:
            cur_res = [m.total_items for m in mnks]
            assert cur_res == CORRECT[round]
            print("round", round, [m.total_items for m in mnks])

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




