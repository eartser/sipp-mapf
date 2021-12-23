from search_functions.SearchFunction import SearchFunction
from entity.sets import OpenAndClosed, Focal
from entity.Node import Node


class FocalSIPP(SearchFunction):

    def __init__(self, heuristic_function, additional_heuristic_function, w=1):
        super().__init__(heuristic_function)
        self.w = w
        self.additional_heuristic_function = additional_heuristic_function

    def _find(self, grid_map, start_i, start_j, goal_i, goal_j):
        OPEN_AND_CLOSED = OpenAndClosed()
        FOCAL = Focal(self.additional_heuristic_function, goal_j, goal_j)

        start = Node(start_i, start_j, h=self.heuristic_function(start_i, start_j, goal_i, goal_j))

        OPEN_AND_CLOSED.add_node(start)
        FOCAL.add_node(start)

        while not FOCAL.is_empty() and not OPEN_AND_CLOSED.is_empty():
            f_min = OPEN_AND_CLOSED.best_f_value
            cur_node = FOCAL.get_best_node()
            OPEN_AND_CLOSED.get_node(cur_node)
            if cur_node.i == goal_i and cur_node.j == goal_j:
                self.publish_solution(cur_node)
                return True, cur_node

            for i, j, interval, t in grid_map.get_successors(cur_node):
                h = self.heuristic_function(i, j, goal_i, goal_j)
                new_node = Node(i, j, g=t, h=h, interval=interval, parent=cur_node)
                OPEN_AND_CLOSED.add_node(new_node)
                if new_node.f <= self.w * f_min:
                    FOCAL.add_node(new_node)

            if not OPEN_AND_CLOSED.is_empty():
                f_new = OPEN_AND_CLOSED.best_f_value
                if f_min < f_new:
                    for node in OPEN_AND_CLOSED:
                        if self.w * f_min < node.f <= self.w * f_new:
                            FOCAL.add_node(node)

        return False, None
