from .SearchFunction import SearchFunction
from entity.sets import Open, Closed
from entity.Node import Node


class SIPP(SearchFunction):

    def find(self, grid_map, start_i, start_j, goal_i, goal_j):
        OPEN = Open()
        CLOSED = Closed()

        start = Node(start_i, start_j, h=self.heuristic_function(start_i, start_j, goal_i, goal_j))

        OPEN.add_node(start)

        while not OPEN.is_empty():
            cur_node = OPEN.get_best_node()
            CLOSED.add_node(cur_node)
            if cur_node.i == goal_i and cur_node.j == goal_j:
                return True, cur_node, CLOSED, OPEN

            for i, j, interval, t in grid_map.get_successors(cur_node):
                h = self.heuristic_function(i, j, goal_i, goal_j)
                new_node = Node(i, j, g=t, h=h, interval=interval, parent=cur_node)
                if CLOSED.was_expanded(new_node):
                    continue
                OPEN.add_node(new_node)

        return False, None, CLOSED, OPEN
