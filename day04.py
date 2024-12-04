#%%
from pathlib import Path
import numpy as np
import re

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input04b.txt' ), 'r' ).read()

#%%
mm = np.array([list(x) for x in  input.split('\n')] )


#%%

def reverse(input):
    return input[::-1]

def xmas(s):
     return len(re.findall('XMAS',s)) + len(re.findall('XMAS',reverse(s)))

def m2s(mm):
    s = '\n'.join([''.join(row) for row in mm])
    return s

def mdiag2s(mm):
    n = mm.shape[0]
    dd = [np.diagonal(mm,offset = i) for i in range(-n+1, n)]
    s = '\n'.join([''.join(row) for row in dd])
    return s

result = (
xmas(m2s(mm)) +
xmas(m2s(np.rot90(mm))) +
xmas(mdiag2s(mm) ) +
xmas(mdiag2s(np.flipud(mm)) )  )

print(f'Result 1: {result}')

#%%

n = mm.shape[0]
result = 0 
for i in range(1, n-1):
    for j in range(1, n-1):
        axis1 = False
        axis2 = False
        if mm[i,j] == 'A':
            if ((mm[i-1, j - 1] == 'M') and (mm[i+1, j + 1] == 'S')  ) or \
            ((mm[i-1, j - 1] == 'S') and (mm[i+1, j + 1] == 'M')  ):
                axis1 = True
            if ((mm[i-1, j + 1] == 'M') and (mm[i+1, j - 1] == 'S')  ) or \
            ((mm[i-1, j + 1] == 'S') and (mm[i+1, j - 1] == 'M')  ):
                axis2 = True
        result += axis1 * axis2

print(f'Result 2: {result}')
