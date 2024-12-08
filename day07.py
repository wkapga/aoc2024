#%%
from pathlib import Path
import numpy as np
import itertools

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input07b.txt' ), 'r' ).read()

#%%


targets = [int(x.split(':')[0]) for x in   input.split('\n')]
valueslist = [x.split(': ')[1:] for x in   input.split('\n')]
valueslist = [x[0].split(' ') for x in valueslist]
valueslist =  [[int(x) for x in values] for values in valueslist]


#%%



#%%
def checktestingvalue(testingvalue, values, oplist):
    result = values[0]
    for i, v in enumerate(values[1:]):
        if oplist[i-1] == 'a':
            result = result + v
        else:
            result = result * v
        if result > testingvalue:
            return False
        if result == testingvalue:
            return True
    return False 


#%%
calibresult = 0
for testingvalue, values in zip(targets, valueslist):
    ops = list(itertools.product('am',repeat = len(values) - 1))
    for oplist in ops:
        res = checktestingvalue(testingvalue, values, oplist)
        #print(res,testingvalue, values, oplist )
        if res:
            calibresult += testingvalue
            break
    
print(f'Result 1: {calibresult }')

# Result 1: 1582598718861


 
#%%

def checktestingvalue2(testingvalue, values, oplist):
    result = values[0]
    for i, v in enumerate(values[1:]):
        
        match oplist[i]:
            case 'a':
                result = result + v
            case 'm':
                result = result * v
            case 'c':
                result = int(str(result) + str(v))
        if result > testingvalue:
            return False
    if result == testingvalue:
        return True
    return False 

#%%
calibresult = 0
for testingvalue, values in zip(targets, valueslist):
    ops = list(itertools.product('amc',repeat = len(values) - 1))
    for oplist in ops:
        res = checktestingvalue2(testingvalue, values, oplist)
        
        if res:
            calibresult += testingvalue
            break
    print(res,testingvalue, values, oplist )
print(f'Result 2: {calibresult }')
