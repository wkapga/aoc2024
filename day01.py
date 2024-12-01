from pathlib import Path
import numpy as np

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input01b.txt' ), 'r' ).read()

s1 = input.split('\n')

s = np.asarray([np.fromstring(x, dtype= int, sep = '   ') for x in s1] )

s.sort(axis = 0)

print('result 1:')
print( np.abs(np.diff(s,1, axis=1)).sum())


# %%
s = np.asarray([np.fromstring(x, dtype= int, sep = '   ') for x in s1] )

score = 0
for x in s[:,0]:
    score = score + x * (sum(s[:,1] == x))

print('result 2:')
print(score)



# %%

s = np.asarray([np.fromstring(x, dtype= int, sep = '   ') for x in s1] )

nr, occur = np.unique(s[:,1], return_counts= True)

occurences = dict(zip(nr, occur))

score = 0
for x in s[:,0]:

    if x in occurences.keys():
        score = score + x * occurences[x]

print('result 2b:')
print(score)