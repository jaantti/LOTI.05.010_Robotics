import math

class FieldPoint:
    def __init__(self, x, y, Type=None, Passable=True):
        self.x = x
        self.y = y
        self.opened = False
        self.closed = False
        self.passable = Passable
        self.parent = None
        self.fScore = None
        self.gScore = None
        self.type = Type

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __cmp__(self, other):
        if self.fScore < other.fScore:
            return -1
        elif self.fScore > other.fScore:
            return 1
        else:
            return 0

    def dist(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def setParent(self, parent):
        self.parent = parent

    def equals(self, point):
        return self.x == point.x and self.y == point.y
