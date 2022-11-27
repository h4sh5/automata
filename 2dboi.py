#!/usr/bin/env python3

import sys
import random
import time

# we are going 2D now
GRID = []

WIDTH, HEIGHT = 20,20

for i in range(WIDTH):
	row = []
	for j in range(HEIGHT):
		row.append(random.randrange(0,2)) # 0/1
	GRID.append(row)
print('len grid:', len(GRID))
# print(GRID)

TYPES = [' ', '*'] # simple grid, just 0 and 1

TYPEDICT = dict(zip(list(range(len(TYPES))), TYPES))
TYPEDICT_R = dict([(TYPEDICT.get(k),k) for k in TYPEDICT])
# ^ type mapped to index 

def rule1(grid):
	'''
	loop through each cell, and do rules on its immediate (not diagonal) neighbours
	if 3/4 is not alive, cell is dead
	'''
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			current = grid[r][c]
			right = grid[r][(c+1) % WIDTH] # always wrap around
			left = grid[r][(c-1) % WIDTH]
			up = grid[(r + 1) % HEIGHT][c]
			down = grid[(r - 1) % HEIGHT][c]

			neighbours  = [right,left,up,down]
			alivecount = neighbours.count(1)
			if alivecount >= 2:
				# dead
				grid[r][c] = 0

	return grid



def prettyprint(grid):
	for r in range(HEIGHT):
		for c in range(WIDTH):
			print(TYPES[grid[r][c]], end='')
		print()

def run(grid, generations):
	print('gens:',generations)
	for i in range(generations):
		print('---------------- %i ------------------'%i)
		grid = rule1(grid)
		prettyprint(grid)

generations = 10

if len(sys.argv) > 1:
	generations = int(sys.argv[1])

run(GRID, generations)
