from .SafeInterval import SafeInterval


class Map:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._safe_intervals = [[[] for _ in range(self._width)] for _ in range(self._height)]
        self.obstacles = []

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

    def get_neighbors(self, i, j):
        neighbors = []
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for d in delta:
            if self.in_bounds(i + d[0], j + d[1]) and self.traversable(i + d[0], j + d[1]):
                neighbors.append((i + d[0], j + d[1]))
        return neighbors

    def get_successors(self, node):
        successors = []
        start_t = node.g + 1
        end_t = self._safe_intervals[node.i][node.j][node.interval].end + 1
        for m in self.get_neighbors(node.i, node.j):
            i, j = m
            for int_i, safe_interval in enumerate(self._safe_intervals[i][j]):
                if safe_interval.start > end_t or safe_interval.end < start_t:
                    continue

                t = max(start_t, safe_interval.start)
                if t == safe_interval.start:
                    for obstacle in self.obstacles:
                        if t < len(obstacle) and obstacle[t-1] == (i, j) and obstacle[t] == (node.i, node.j):
                            t = min(end_t, safe_interval.end) + 1
                            break

                if t > min(end_t, safe_interval.end):
                    continue
                successors.append((i, j, int_i, t))
        return successors

    def get_size(self):
        return self._height, self._width

    def apply_dynamic_obstacles(self, paths_list):
        for path in paths_list:
            for node in path:
                # Update safe interval
                pass
