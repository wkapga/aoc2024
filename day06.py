from pathlib import Path
import numpy as np
import re

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2024"

input = open(Path(proj_path,'input06a.txt' ), 'r' ).read()

#%%

raw = np.array([list(x) for x in input.split('\n')])

dimensions = np.shape(raw)

startingpoint = np.array(np.nonzero(raw == '^')).flatten()

obstacles = np.transpose(np.nonzero(raw == '#'))



startingdirection = np.array([-1, 0])


def change_direction(direction):
    rotatiomatrix = np.array([[0, -1],[1, 0]])
    return np.matmul(direction, rotatiomatrix)

def check_obstacle(point, direction, obstacles):
    return (np.array(point + direction) == obstacles).all(axis=1).any()

def check_out(point, direction, dimensions):
    next = point + direction
    return ( (next < 0).any() or (next == dimensions).any() )

point = startingpoint
direction = startingdirection

visited = np.zeros(dimensions, dtype= int)
visitlist = list()
visited[tuple(startingpoint)] = 1

while not check_out(point, direction, dimensions):
    
    if check_obstacle(point, direction, obstacles):
        direction = change_direction(direction)
        visitlist.append([point, direction])
    else:
        point = point + direction
        visited[tuple(point)] = visited[tuple(point)] + 1
        visitlist.append([point, direction])

print(f'Result 1: {np.sum(visited)}')
