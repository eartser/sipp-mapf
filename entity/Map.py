from .SafeInterval import SafeInterval
from math import inf


class Map:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._safe_intervals = [[[] for _ in range(self._width)] for _ in range(self._height)]
        self.obstacles = []  # list of paths of obstacles

    def set_map_properties(self, width, height, safe_intervals=None):
        self._width = width
        self._height = height
        if safe_intervals is None:
            self._safe_intervals = [[[] for _ in range(self._width)] for _ in range(self._height)]
        else:
            self._safe_intervals = safe_intervals  # TODO: do we need copy here?

    def in_bounds(self, i, j):
        return (0 <= j < self._width) and (0 <= i < self._height)

    def traversable(self, i, j):
        return len(self._safe_intervals[i][j]) > 0  # list is empty for static obstacles

    def get_neighbors(self, i, j):
        neighbors = []
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for d in delta:
            if self.in_bounds(i + d[0], j + d[1]) and self.traversable(i + d[0], j + d[1]):
                neighbors.append((i + d[0], j + d[1]))
        return neighbors

    def get_successors(self, node):
        successors = []
        start_t = node.g + 1  # the earliest time we can get to the successor
        if node.i >= self._height or node.j >= self._width or node.interval >= len(self._safe_intervals[node.i][node.j]):
            print(self._height, self._width, len(self._safe_intervals[node.i][node.j]), node.i, node.j, node.interval)
        end_t = self._safe_intervals[node.i][node.j][node.interval].end + 1  # the latest time -//-
        for m in self.get_neighbors(node.i, node.j):
            i, j = m
            for int_i, safe_interval in enumerate(self._safe_intervals[i][j]):
                if safe_interval.start > end_t or safe_interval.end < start_t:
                    continue

                t = max(start_t, safe_interval.start)

                # edge collisions
                if t == safe_interval.start:  # otherwise in timestamp t-1 the cell is empty, no edge collisions
                    for obstacle in self.obstacles:
                        # edge collision condition
                        if t < len(obstacle) and obstacle[t-1] == (i, j) and obstacle[t] == (node.i, node.j):
                            t = inf  # in this case we can't go to this cell
                            break

                if t > min(end_t, safe_interval.end):
                    continue
                successors.append((i, j, int_i, t))
        return successors

    def get_size(self):
        return self._height, self._width

    @staticmethod
    def extended_path(path):
        new_path = []
        for ind in range(1, len(path)):
            cur_node = path[ind]
            prev_node = path[ind - 1]
            for _ in range(cur_node.g - prev_node.g):
                new_path.append((prev_node.i, prev_node.j))
        new_path.append((path[-1].i, path[-1].j))
        return new_path

    def apply_dynamic_obstacles(self, paths_list):

        for path in paths_list:
            extended_path = self.extended_path(path)
            self.obstacles.append(extended_path)
            obstacle_in_cell = [[[] for _ in range(self._width)] for _ in range(self._height)]
            updated_cells = set()
            for t, (i, j) in enumerate(extended_path):
                updated_cells.add((i, j))
                obstacle_in_cell[i][j].append(t)

            for i, j in updated_cells:
                k = 0
                new_safe_intervals = []
                for interval in self._safe_intervals[i][j]:
                    while k < len(obstacle_in_cell[i][j]) and obstacle_in_cell[i][j][k] < interval.start:
                        k += 1

                    if k >= len(obstacle_in_cell[i][j]):
                        new_safe_intervals.append(interval)
                        continue

                    cur_start = interval.start
                    while k < len(obstacle_in_cell[i][j]) and obstacle_in_cell[i][j][k] <= interval.end:
                        cur_end = obstacle_in_cell[i][j][k] - 1
                        if cur_start <= cur_end:
                            new_safe_intervals.append(SafeInterval(cur_start, cur_end))

                        cur_start = cur_end + 2
                        k += 1

                    if cur_start <= interval.end:
                        new_safe_intervals.append(SafeInterval(cur_start, interval.end))

                self._safe_intervals[i][j] = new_safe_intervals


class TimestampSearchMap(Map):

    def __init__(self, grid_map):
        super().__init__()
        self._width = grid_map._width
        self._height = grid_map._height
        self._safe_intervals = grid_map._safe_intervals

    def get_neighbors(self, i, j):
        neighbors = super().get_neighbors(i, j)
        neighbors.append((i, j))
        return neighbors

    def get_successors(self, node):

        def check_move(i1, j1, i2, j2, t):
            for obstacle in self.obstacles:
                if t + 1 < len(obstacle) and obstacle[t + 1] == (i2, j2):
                    return False
                if t + 1 < len(obstacle) and obstacle[t] == (i2, j2) and obstacle[t + 1] == (i1, j1):
                    return False
            return True

        successors = []
        for m in self.get_neighbors(node.i, node.j):
            i, j = m
            if not check_move(node.i, node.j, i, j, node.g):
                continue
            successors.append((i, j))
        return successors

    def apply_dynamic_obstacles(self, paths_list):
        for path in paths_list:
            self.obstacles.append(self.extended_path(path))
