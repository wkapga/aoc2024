from pathlib import Path
import numpy as np
import re
from collections import defaultdict
from itertools import permutations

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input05b.txt' ), 'r' ).read()

#%%

pages = defaultdict(list)
updates = list()

i = 0
for line in input.split('\n'):
    if '|' in line:
        tup = [int(x) for x in line.split('|')]
        pages[tup[0]].append(tup[1])

    if ',' in line:
        updates.append( [int(x) for x in line.split(',')] )


# %%

result = 0
incorrects = list()

def check_order(update):
    is_valid = True
    for i, _ in enumerate(update):
        a = pages[update[i]]
        b = update[(i+1):]
        is_valid = is_valid and set(b).issubset(set(a))
    return is_valid

result = 0
for update in updates:
    is_valid = check_order(update)
    if is_valid:
        result += is_valid * update[len(update)//2]
    else:
        
        incorrects.append(update)

print(f'Result 1: {result}')
# Result 1: 4637
#%%
for update in incorrects:
    k = 1
    while not check_order(update):
        snip = update[:k]
        new = update[k]
        for i, _ in enumerate(snip):
            tocheck = [*snip[:i], new, *snip[i:]]
            if check_order(tocheck):
                update[:(k+1)] = tocheck
                break
        k += 1

result = 0
for update in incorrects:
    result +=  update[len(update)//2]

print(f'Result 2: {result}')
# Result 6370

