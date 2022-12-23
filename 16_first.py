from pathlib import Path
from copy import copy
from functools import lru_cache

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
        dist = {}
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
    # @lru_cache(maxsize=1000000)
    def rec(node_name: str, closed: tuple, mins=0, pres=0, passed=None):
        # if pres > 78 and node_name=="CC":
        #     print(pres, f"in min {mins} {closed}")
        cache_key = (node_name, closed, mins, pres)
        if cache_key in cache:
            return cache[cache_key]
        if mins >= 30:
            return  0
        results = []
        node = nodes[node_name]
        if node_name in closed: # открываем текущий если он закрыт ( и больше нуля)
            new_closed = tuple(name for name in closed if name != node_name)
            result = rec(node.name, new_closed, mins + 1, pres + node.rate)
            results.append(result)
        if len(closed) > 1:
            for next_node_name in node.paths:
                # dist = dists[next_node_name]
                result = rec(next_node_name, closed, mins + 1, pres)
                results.append(result)
        elif len(closed) == 1: #simple last step
            dist_for_last_node = dists[node_name][closed[0]]
            if mins + dist_for_last_node < 30:
                res =  pres * (30 - mins) + nodes[closed[0]].rate * (30 - mins - dist_for_last_node - 1)
            else:
                res = pres * (30 - mins)
            cache[cache_key] = res
            return res
        else:
            res = pres * (30 - mins)
            cache[cache_key] = res
            return res
        res = pres + max(results)
        cache[cache_key] = res
        return res
    

    closed = tuple(name for name, node in nodes.items() if node.off)
    ans = rec("AA", closed, mins=0)
    return ans


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

print(solve(example_data))
print(solve(my_data))




