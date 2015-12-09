#!/proj/env/bin/python
import os
import sys
import re

grid = [[0 for x in range(1000)] for x in range(1000)]
with open("lights.txt") as f:
    for line in f:
        positions = map(int, re.findall(r'\d+', line))
        for i in range(positions[0], positions[2] + 1):
            for j in range(positions[1], positions[3] + 1):
                if "turn on" in line:
                    grid[i][j] += 1
                elif "turn off" in line:
                    if grid[i][j] > 0:
                        grid[i][j] -= 1
                elif "toggle" in line:
                    grid[i][j] += 2
nr_of_lights = 0
for i in range(1000):
    for j in range(1000):
        nr_of_lights += grid[i][j]
print nr_of_lights
