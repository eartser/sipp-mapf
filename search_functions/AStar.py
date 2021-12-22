from search_functions.SearchFunction import SearchFunction
from entity.sets import Open, Closed
from entity.Node import TimestampSearchNode


class AStar(SearchFunction):
    def _find(self, grid_map, start_i, start_j, goal_i, goal_j):
        OPEN = Open()
        CLOSED = Closed()

        start = TimestampSearchNode(start_i, start_j, h=self.heuristic_function(start_i, start_j, goal_i, goal_j))

        OPEN.add_node(start)

        while not OPEN.is_empty():
            cur_node = OPEN.get_best_node()
            CLOSED.add_node(cur_node)
            if cur_node.i == goal_i and cur_node.j == goal_j:
                self.publish_solution(cur_node)
                return True, cur_node

            for i, j in grid_map.get_successors(cur_node):
                g = cur_node.g + 1
                h = self.heuristic_function(i, j, goal_i, goal_j)
                new_node = TimestampSearchNode(i, j, g=g, h=h, parent=cur_node)
                if CLOSED.was_expanded(new_node):
                    continue
                OPEN.add_node(new_node)

        return False, None
