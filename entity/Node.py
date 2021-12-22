class Node:

    def __init__(self, i, j, g=0, h=0, f=None, parent=None, interval=0, optimal=True):
        self.i = i
        self.j = j
        self.g = g
        self.h = h
        self.optimal = optimal  # used for AnytimeSIPP
        if f is None:
            self.f = self.g + self.h
        else:
            self.f = f
        self.interval = interval
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def get_pos(self):
        return self.i, self.j, self.interval
