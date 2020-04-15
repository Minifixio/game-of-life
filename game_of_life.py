
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

grid = []
gridSize = 100
rate = 50 # in ms

def initPop():
    global grid, gridSize
    grid = np.random.randint(2, size=(gridSize, gridSize))
    return grid

def nextGen(): # Creating next generation
    global grid
    newGrid = grid.copy()
    for x in range(len(grid)):
        for y in range(len(grid)):
            n = neighbors(x, y)
            if newGrid[x, y] == 1: # Conway's rules
                if n < 2 or n > 3:
                    newGrid[x, y] = 0
            if newGrid[x, y] == 0:
                if n == 3:
                    newGrid[x, y] = 1
    grid = newGrid
    return newGrid

def neighbors(x, y): # Finding number of living neighbors
    global grid
    total = 0
    xMin, xMax = lim(x, len(grid))
    yMin, yMax = lim(y, len(grid))
    for i in range(xMin, xMax + 1):
        for j in range(yMin, yMax + 1):
            total += grid[i, j]
    return total - grid[x, y] # Removing the scope cell

def lim(v, lenght):
    if v == 0:
        vMin = 0
    else:
        vMin = v - 1
    if v + 1 > lenght - 1:
        vMax = v
    else:
        vMax = v + 1
    return vMin, vMax

def updateData(frameNumber):
    mat.set_data(nextGen())
    return

fig, ax = plt.subplots()
mat = ax.matshow(initPop(), cmap='gray')
ani = animation.FuncAnimation(fig, updateData, init_func=initPop, interval=rate)
plt.show()


