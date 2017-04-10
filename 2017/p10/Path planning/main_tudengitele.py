from Field import *
from FieldPoint import *
import numpy as np

# 0 - Passable
# 1 - Wall
# 2 - Start
# 3 - End
# 4 - Visited spaces
# 5 - Path
field = [[0, 1, 0, 1, 0, 1, 3],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [2, 0, 0, 0, 0, 0, 0]]

fieldX = len(field)
fieldY = len(field)

nodes = np.empty((fieldX, fieldY), dtype=object)
open = []
closed = []
start = None
finish = None

f = Field(500, 500, fieldX)
f.createWindow()
f.update(field)

# Get objects from field
for i, row in enumerate(field):
    for j, item in enumerate(row):
        if item == 1:
            nodes[j, i] = FieldPoint(j, i, Type=1, Passable=False)
        else:
            nodes[j, i] = FieldPoint(j, i, Type=item)
            if item == 2:
                start = FieldPoint(j, i)
            if item == 3:
                finish = FieldPoint(j, i)

# Set up starting node
start.gScore = 0
open.append(start)

# Find path using A*
while len(open) > 0 and finish not in closed:
    # Write you code here

    f.updateNp(nodes)

# Draw the path
while not currentPath.equals(start):
    index = closed.index(currentPath)
    if closed[index].type != 3:
        closed[index].type = 5
    currentPath = closed[index].parent

    time.sleep(0.1)
f.updateNp(nodes)
finisIndex = closed.index(finish)

f.closeOnMouse()