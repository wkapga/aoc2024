#%%
from pathlib import Path
import numpy as np

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input02b.txt' ), 'r' ).read().split('\n')

#%%

def test_list(levels):
    updown = np.sign(max(levels[-2:]) - min(levels[:2]) )
    for i in range(1,len(levels)):
        diff = updown* (levels[i] - levels[i-1] )
        if (diff <1) or (diff >3):
            return False
            break
    return True


feasible = 0
for j in range(0,len(input)):
    feasible += 1* test_list([int(x) for x in input[j].split(' ')])

print(f'result 1: {feasible}')

#%%


feasible = 0
for j in range(0,len(input)):
    levels = [int(x) for x in input[j].split(' ')]
    list_is_safe = test_list(levels)

    if list_is_safe:
        feasible += 1
    else:
        for i,_ in enumerate(levels):
            levels_mod = levels.copy()
            levels_mod.pop(i)
            list_is_safe = test_list(levels_mod)
            if list_is_safe:
                feasible += 1
                break

print(f'result 2: {feasible}')


