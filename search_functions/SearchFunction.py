import time
import threading


class SearchFunction:

    def __init__(self, heuristic_function):
        self.heuristic_function = heuristic_function
        self.goal_node = None
        self.path_found = False
        self.lock = threading.Lock()

    def find(self, grid_map, start_i, start_j, goal_i, goal_j):
        thread = threading.Thread(target=self._find, args=[grid_map, start_i, start_j, goal_i, goal_j])
        thread.start()
        thread.join(timeout=60)
        if self.goal_node is not None:
            self.path_found = True
        return self.path_found, self.goal_node

    def _find(self, grid_map, start_i, start_j, goal_i, goal_j):
        raise NotImplementedError

    def publish_solution(self, goal_node):
        self.lock.acquire()
        self.goal_node = goal_node
        self.lock.release()

    @staticmethod
    def make_path(goal_node):
        length = goal_node.g
        current_node = goal_node
        path = []
        while current_node.parent:
            path.append(current_node)
            current_node = current_node.parent
        path.append(current_node)
        return path[::-1], length
