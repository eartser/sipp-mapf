class Node:

    def __init__(self, i, j, g=0, h=0, f=None, parent=None, interval=0, subopt=False):
        self.i = i
        self.j = j
        self.g = g
        self.h = h
        if f is None:
            self.f = self.g + self.h
        else:
            self.f = f
        self.interval = interval
        self.parent = parent
        self.subopt = subopt

    def __lt__(self, other):
        return self.f < other.f

    def get_pos(self):
        return self.i, self.j, self.interval, self.subopt

    def __str__(self):
        return f'(i={self.i}, j={self.j}, int={self.interval}, t={self.g})'

    def __repr__(self):
        return str(self)


class TimestampSearchNode(Node):
    def get_pos(self):
        return self.i, self.j, self.g
