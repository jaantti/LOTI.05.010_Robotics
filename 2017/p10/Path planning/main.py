from Field import *
from FieldPoint import *
import numpy as np

field = [[0, 0, 0, 0, 1, 0, 3],
         [0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [2, 0, 0, 0, 0, 0, 0]]

fieldX = 7
fieldY = 7

nodes = np.empty((fieldX, fieldY), dtype=object)
open = []
closed = []
start = None
finish = None

f = Field(500, 500, fieldX)
f.createWindow()
f.update(field)

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

start.gScore = 0
open.append(start)

while len(open) > 0 and finish not in closed:

    if len(open) == 1:
        best = open.pop()
        closed.append(best)
    else:
        open.sort()
        best = open.pop(0)
        closed.append(best)
    if best.type != 3:
        best.type = 4
    x = best.x
    y = best.y
    toCheck = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]

    for p in toCheck:
        if p[0] >= 0 and p[0] < fieldX and p[1] >= 0 and p[1] < fieldY:
            toCheckNode = nodes[p[0], p[1]]
            if toCheckNode.passable and toCheckNode not in closed:
                if toCheckNode not in open:
                    toCheckNode.parent = best
                    hs = toCheckNode.dist(finish)
                    gs = toCheckNode.dist(best)
                    toCheckNode.gScore = best.gScore + gs
                    toCheckNode.fScore = hs + toCheckNode.gScore
                    open.append(toCheckNode)
                else:
                    gs = best.gScore + toCheckNode.dist(best)
                    if gs < toCheckNode.gScore:
                        hs = toCheckNode.dist(finish)
                        toCheckNode.fScore = hs + gs
                        toCheckNode.gScore = gs
                        toCheckNode.parent = best
    f.updateNp(nodes)
    #time.sleep(0.5)

currentPath = finish

while not currentPath.equals(start):
    index = closed.index(currentPath)
    if closed[index].type != 3:
        closed[index].type = 5
    currentPath = closed[index].parent

    time.sleep(0.1)
f.updateNp(nodes)
finisIndex = closed.index(finish)

f.closeOnMouse()