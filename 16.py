from pathlib import Path
from copy import copy
from functools import lru_cache
from itertools import product
from time import time

MINUTS = 16

class Node:
    def __init__(self, words) -> None:
        self.name = words[1]
        self.rate = int(words[4][5:-1])
        self.paths = [path.rstrip(",") for path in words[9:]]
        self.off = self.rate > 0

    def __repr__(self) -> str:
        return f"{self.name}({self.rate}): {self.paths}"

def solve(data: list[str]):
    nodes = {line.split()[1]: Node(line.split()) for line in data}
    attemps = {}

    def dist_to_nodes(node):
        dist = {node.name: 0}
        cache = node.paths
        steps = 1
        while cache:
            new_cache = set()
            for name in cache:
                if name not in dist and name != node.name:
                    dist[name] = steps
                    new_cache.update(set(nodes[name].paths))
            cache = new_cache
            steps += 1
        return dist
        
    dists = {name: dist_to_nodes(node) for name, node in nodes.items()}
    cache = {}
    # @lru_cache(maxsize=1000000, )
    def rec(node_name1: str, node_name2, closed: tuple, mins=0, pres=0, prev1=set(), prev2=set()):
        cache_key = (min(node_name1, node_name2), max(node_name1, node_name2), closed)
        if cache_key in cache:
            if mins > cache[cache_key][1]:
                return 0
            elif mins == cache[cache_key][1]:
                return cache[cache_key][0]

        if mins >= MINUTS:
            return  0
        if len(closed) == 1:
            last = closed[0]
            dist = min(dists[node_name1][last], dists[node_name2][last])
            if mins + dist < MINUTS:
                res = pres * (MINUTS - mins) + nodes[closed[0]].rate * (MINUTS - mins - dist - 1)
            else:
                res = pres * (MINUTS - mins)
            cache[cache_key] = res, mins
            return res
        if not closed:
            return pres * (MINUTS - mins)

        
        args = []
        # variants for first (man)
        node = nodes[node_name1]
        if node_name1 in closed:
            new_closed = tuple(name for name in closed if name != node_name1)
            new_prev1 = set() # обнуляем предыдущие посещенные краны, если не зря сюда шли
            args.append((node_name1, new_closed, pres + node.rate, new_prev1))
        for next_node_name in node.paths:
            if next_node_name in prev2: # чтобы не бродил туда-сюда бесцельно
                continue
            args.append((next_node_name, closed, pres, prev1 | set([next_node_name])))

        results = []
        # productive variants for first(man) and second(elephant)
        node = nodes[node_name2]
        for name1, closed, pres, prev1 in args:
            if node_name2 in closed: # открываем текущий если он закрыт ( и больше нуля)
                new_closed = tuple(name for name in closed if name != node_name2)
                new_prev2 = set() # обнуляем предыдущие посещенные краны, если не зря сюда шли
                result = rec(name1, node_name2, new_closed, mins + 1, pres + node.rate, prev1=prev1, prev2=new_prev2)
                results.append(result)
            for next_node_name in node.paths:
                if next_node_name in prev2: # чтобы не бродил туда-сюда бесцельно
                    continue
                result = rec(name1, next_node_name, closed, mins + 1, pres, prev1=prev1, prev2=prev2 | set([next_node_name]))
                results.append(result)
        if not results:
            results.append(0)
        res =  pres + max(results)
        cache[cache_key] = res, mins
        return res

    

    closed = tuple(name for name, node in nodes.items() if node.off)
    ans = rec("AA", "AA", closed, mins=0)
    return ans


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

start = time()
print(solve(example_data))
mid = time()
print("time_temp" , mid - start)
print(solve(my_data))
print("time_main", time() - mid)





