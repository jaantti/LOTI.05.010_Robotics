from graphics import *
import time

field = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [2, 0, 1, 0, 3],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

print field

def main():
    win = GraphWin('Floor', 500, 500)

    win.setCoords(0, 5, 5, 0)
    win.setBackground("white")

    for i, row in enumerate(field):
        for j, item in enumerate(row):
            time.sleep(0.5)
            sq = Rectangle(Point(j, i), Point(j + 1, i + 1))
            sq.draw(win)
            if item == 0:
                sq.setFill(color_rgb(230, 230, 200))
            if item == 1:
                sq.setFill(color_rgb(0, 0, 0))
            if item == 2:
                sq.setFill("green")
            if item == 3:
                sq.setFill("red")

    win.getMouse()
    win.close()

main()

'''
    # draw grid
    for x in range(10):
        for y in range(10):
            win.plotPixel(x*50, y*50, "blue")

    square = Rectangle(Point(5,5), Point(6,6))
    square.draw(win)
    square.setFill(color_rgb(150, 150, 150))
'''