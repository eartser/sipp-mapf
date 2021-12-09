class Map:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._cells = []

    def set_grid_cells(self, width, height, grid_cells):
        self._width = width
        self._height = height
        self._cells = grid_cells

    def in_bounds(self, i, j):
        return (0 <= j < self._width) and (0 <= i < self._height)

    def traversable(self, i, j):
        return not self._cells[i][j]

    def get_neighbors(self, i, j):
        neighbors = []

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                n_i = i + di
                n_j = j + dj
                if self.in_bounds(n_i, n_j) and self.traversable(n_i, n_j) and \
                        self.traversable(n_i, j) and self.traversable(i, n_j):
                    neighbors.append((n_i, n_j))

        return neighbors

    def get_size(self):
        return self._height, self._width
