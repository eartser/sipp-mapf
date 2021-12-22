from search_functions.SearchFunction import SearchFunction
from entity.sets import Open, Closed
from entity.Node import Node


class WdSIPP(SearchFunction):

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
                new_node_opt = Node(i, j, g=t, h=h, f=self.w*(t+h), interval=interval, parent=cur_node)
                new_node_subopt = Node(i, j, g=t, h=h, f=t+self.w*h, interval=interval, parent=cur_node, subopt=True)
                if not CLOSED.was_expanded(new_node_opt):
                    OPEN.add_node(new_node_opt)
                if not CLOSED.was_expanded(new_node_subopt):
                    OPEN.add_node(new_node_subopt)

        return False, None, CLOSED, OPEN


class WrSIPP(SearchFunction):
    pass
