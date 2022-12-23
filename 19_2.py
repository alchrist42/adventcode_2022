from functools import lru_cache
from pathlib import Path
from time import time

STEPS = 32

def solve(data: list[str]):
    data = [line.split(" ") for line in data]
    ans = 1

    for rec_n, rec in enumerate(data[:3]):
        cost_ore = int(rec[6])
        cost_clay = int(rec[12])
        cost_obs = (int(rec[18]), int(rec[21]))
        cost_geo = (int(rec[27]), int(rec[30]))

        need_rclay = (((cost_obs[1] ** 2)* cost_geo[1]) ** 0.25 ) 
        print(cost_ore, cost_clay, cost_obs, cost_geo, need_rclay)

        @lru_cache(1000000)
        def rec(rore, rclay, robs, rgeo, ore, clay, obs, geo, step=0):
            if step == STEPS:
                return geo
            new_ore = ore + rore
            new_clay = clay + rclay
            new_obs = obs + robs
            new_geo = geo + rgeo


            results = []
            if ore >= cost_geo[0] and obs >= cost_geo[1]: # Если можем билдить geode робота - даже не пробуем делать других
                res = rec(rore, rclay, robs, rgeo + 1, new_ore - cost_geo[0], new_clay, new_obs - cost_geo[1], new_geo, step + 1)
                results.append(res)
                return res
            if ore >= cost_obs[0] and clay >= cost_obs[1]: # Если еще нет производителей обсидиана - однозначно делаем его
                res = rec(rore, rclay, robs + 1, rgeo, new_ore - cost_obs[0], new_clay - cost_obs[1], new_obs, new_geo, step + 1)
                results.append(res)
            if results:
                res = rec(rore, rclay, robs, rgeo, new_ore, new_clay, new_obs, new_geo, step + 1)
                results.append(res)
                return max(results)
            res = rec(rore, rclay, robs, rgeo, new_ore, new_clay, new_obs, new_geo, step + 1)
            results.append(res)
            if ore >= cost_ore and rore < 6 and step < 10:
                res = rec(rore + 1, rclay, robs, rgeo, new_ore - cost_ore, new_clay, new_obs, new_geo, step + 1)
                results.append(res)
            if ore >= cost_clay and step < 15:
                res = rec(rore, rclay + 1, robs, rgeo, new_ore - cost_clay, new_clay, new_obs, new_geo, step + 1)
                results.append(res)
            # if rclay > 5:
            #     print(".", end="")
            return max(results)

        result = rec(1, 0, 0, 0, 0, 0, 0, 0)
        print(rec_n, result)
        ans *= result


    return ans


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
print(solve(my_data))
print("time_main", time() - mid)




