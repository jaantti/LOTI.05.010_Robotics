from graphics import *
import time

class Field:
    def __init__(self, width, height, gridCount):
        self.sleep = 0
        self.win = GraphWin()
        self.gridCount = gridCount
        self.width = width
        self.height = height

    def createWindow(self):
        self.win = GraphWin('Path planning', 500, 500)
        self.win.setCoords(0, self.gridCount, self.gridCount, 0)
        self.win.setBackground("white")

    def update(self, stateArray):
        for i, row in enumerate(stateArray):
            for j, item in enumerate(row):
                time.sleep(self.sleep)
                sq = Rectangle(Point(j, i), Point(j + 1, i + 1))
                sq.draw(self.win)
                # Passable terrain
                if item == 0:
                    sq.setFill(color_rgb(230, 230, 200))
                # Obstacle
                if item == 1:
                    sq.setFill(color_rgb(0, 0, 0))
                # Start
                if item == 2:
                    sq.setFill("green")
                # End
                if item == 3:
                    sq.setFill("red")
                # Visited spaces
                if item == 4:
                    sq.setFill(color_rgb(220, 170, 220))
                # Path
                if item == 5:
                    sq.setFill(color_rgb(220, 130, 220))

    def updateNp(self, npArray):
        for i in npArray:
            for item in i:
                time.sleep(self.sleep)
                sq = Rectangle(Point(item.x, item.y), Point(item.x + 1, item.y + 1))
                sq.draw(self.win)
                #tx = Text(Point(item.x+0.5, item.y+0.5), str(item.parent))
                #tx.draw(self.win)
                if item.parent is not None:
                    circ = Circle(Point(item.x+0.5, item.y+0.5), 0.1)
                    circ.draw(self.win)
                    linex = item.x - item.parent.x
                    liney = item.y - item.parent.y
                    line = Line(Point(item.x+0.5, item.y+0.5), Point(item.x+0.5 - linex, item.y+0.5-liney))
                    line.draw(self.win)
                # Passable terrain
                if item.type == 0:
                    sq.setFill(color_rgb(230, 230, 200))
                # Obstacle
                if item.type == 1:
                    sq.setFill(color_rgb(0, 0, 0))
                # Start
                if item.type == 2:
                    sq.setFill("green")
                # End
                if item.type == 3:
                    sq.setFill("red")
                # Visited spaces
                if item.type == 4:
                    sq.setFill(color_rgb(220, 170, 220))
                # Path
                if item.type == 5:
                    sq.setFill(color_rgb(220, 130, 220))

    def closeOnMouse(self):
        self.win.getMouse()
        self.win.close()

    def setSleepTime(self, time):
        self.sleep = time
