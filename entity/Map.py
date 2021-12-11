from SafeInterval import SafeInterval


class Map:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._safe_intervals = [[[] for _ in range(self._width)] for _ in range(self._height)]

    def set_map_properties(self, width, height, safe_intervals=None):
        self._width = width
        self._height = height
        if safe_intervals is None:
            self._safe_intervals = [[[] for _ in range(self._width)] for _ in range(self._height)]
        else:
            self._safe_intervals = safe_intervals

    def in_bounds(self, i, j):
        return (0 <= j < self._width) and (0 <= i < self._height)

    def traversable(self, i, j):
        return len(self._safe_intervals[i][j]) > 0

    # TODO: Обновить функцию get_neighbors с учетом интервалов
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

    def apply_dynamic_obstacles(self, paths_list):
        for path in paths_list:
            for node in path:
                # Update safe interval
                pass
