#%%
from pathlib import Path
import numpy as np
import itertools
import re

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input08b.txt' ), 'r' ).read()

#%%

raw = np.array([list(x) for x in input.split('\n')])
dims = raw.shape
#%%

frqs = set(raw.flatten().tolist())
frqs.remove('.')

antis = np.zeros(dims)

#%%

for frq in frqs:
    towers = [np.array([x,y]) for x,y in np.nditer(np.where(raw==frq))]
    for towerpair in itertools.permutations(towers, r =2):
        antinode = towerpair[0] + 2 * (towerpair[1]- towerpair[0])
        if np.all(antinode >= 0) and np.all(antinode < dims):
            antis[antinode[0],antinode[1]] = 1
        
print(f'Result 1: {int(antis.sum()) }')



#%%


for frq in frqs:
    towers = [np.array([x,y]) for x,y in np.nditer(np.where(raw==frq))]
    for towerpair in itertools.combinations(towers, r =2):
        keepon = True
        harmonic_multiplier = 0
        while True:
            antinode1 = towerpair[0] + harmonic_multiplier * (towerpair[1]- towerpair[0])
            antinode2 = towerpair[0] - harmonic_multiplier * (towerpair[1]- towerpair[0])
            test1 = np.all(antinode1 >= 0) and np.all(antinode1 < dims)
            test2 = np.all(antinode2 >= 0) and np.all(antinode2 < dims)
            if test1: antis[antinode1[0],antinode1[1]] = 1
            if test2: antis[antinode2[0],antinode2[1]] = 1
            harmonic_multiplier += 1
            if( (not test1) and (not test2)): break

            
print(f'Result 2: {int(antis.sum()) }')


