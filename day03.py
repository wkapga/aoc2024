

#%%
from pathlib import Path
import numpy as np
import re

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input03b.txt' ), 'r' ).read()


instructions = re.findall('mul\(\d+,\d+\)', input)

ll = [re.findall('\d+',instruction) for instruction in  instructions]

print(f'Result 1:{sum([(int(y[0]) * int(y[1])) for y in ll])}')


#%%

mul_pos =[]
mul_res = []
do_pos = []
dont_pos = []

for mul in re.finditer('mul\(\d+,\d+\)', input):
    ll = re.findall('\d+', mul.group())
    mul_pos.append( mul.start()  )
    mul_res.append(int(ll[0]) * int(ll[1])) 

for dos in re.finditer(r'do\(\)', input):
    do_pos.append( dos.start() )

for donts in re.finditer('don\'t\(\)', input):
    dont_pos.append( donts.start() )

doit = True
result = 0
res_ix = 0
for i in range(0, len(input)):
    if i in do_pos:  doit= True 
    if i in dont_pos: doit= False
    
    if i in mul_pos: 
        result +=  doit * mul_res[res_ix]
        res_ix += 1
        
print(f'Result 2:{result}')

