from pathlib import Path
import numpy as np
import re

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input06b.txt' ), 'r' ).read()

#%%

raw = np.array([list(x) for x in input.split('\n')])

dimensions = np.shape(raw)

startingpoint = np.array(np.nonzero(raw == '^')).flatten()

obstacles = np.transpose(np.nonzero(raw == '#'))

rotatiomatrix = np.array([[0, -1],[1, 0]])
rotatiomatrixleft = np.array([[0, 1],[-1, 0]])

startingdirection = np.array([-1, 0])


def change_direction(direction):
    
    return np.matmul(direction, rotatiomatrix)

def check_obstacle(point, direction, obstacles):
    return (np.array(point + direction) == obstacles).all(axis=1).any()

def check_out(point, direction, dimensions):
    next = point + direction
    return ( (next < 0).any() or (next == dimensions).any() )

point = startingpoint
direction = startingdirection

visited = np.zeros(dimensions, dtype= int)

visited[tuple(startingpoint)] = 1

while not check_out(point, direction, dimensions):
    
    if check_obstacle(point, direction, obstacles):
        direction = change_direction(direction)
    else:
        point = point + direction
        visited[tuple(point)] = visited[tuple(point)] + 1

print(f'Result 1: {np.sum(visited)}')


#%%


def check_loop(point, direction, obstacles):
  
    cornerlist = list()
    
    while not check_out(point, direction, dimensions):
        if check_obstacle(point, direction, obstacles):
            direction = change_direction(direction)
            
            # check for loop
            if len(cornerlist)> 0:
                if (np.array([*point, *direction]) == np.array(cornerlist) ).all(axis=1).any():
                        return True
            
            cornerlist.append(np.array([*point, *direction]))
                        
        else:
            point = point + direction
          
    #print(cornerlist)
    return False



visitedbool = 1* (visited > 0) 

v = np.logical_or(visitedbool,np.roll(visitedbool, shift=1, axis = 0))
v = np.logical_or(v,np.roll(visitedbool, shift=-1, axis = 0))
v = np.logical_or(v,np.roll(visitedbool, shift=1, axis = 1))
v = np.logical_or(v,np.roll(visitedbool, shift=-1, axis = 1))
v = np.logical_xor(v,(raw == '#')) # there are already obstacles


for position, totest in np.ndenumerate(v):
    print(position, totest)




#%%
i=0
loop_obstacles = list()
for position, totest in np.ndenumerate(v):
   
    if totest:
        new_obstacle = np.array(position)
        obstacles_mod = np.vstack((obstacles, new_obstacle ) )
        res = check_loop(startingpoint,startingdirection, obstacles_mod)
        if res: 
            loop_obstacles.append(new_obstacle)
            print(i, res, new_obstacle)
        i += 1
    # print(i, res, new_obstacle)

result = np.unique(np.array(loop_obstacles), axis=0).shape[0]

print(f'Result 2: {result}')








