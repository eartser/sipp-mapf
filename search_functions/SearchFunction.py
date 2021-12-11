from entity.sets import Open, Closed
from entity.Node import Node


class SearchFunction:

    def __init__(self, heuristic_function, w=1):
        self.heuristic_function = heuristic_function
        self.w = w

    def find(self, grid_map, start_i, start_j, goal_i, goal_j):
        raise NotImplementedError

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
