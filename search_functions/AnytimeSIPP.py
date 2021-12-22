from search_functions.SearchFunction import SearchFunction
from entity.sets import Open, Closed
from entity.Node import Node
from math import inf


class AnytimeSIPP(SearchFunction):

    def __init__(self, heuristic_function):
        super().__init__(heuristic_function, w=inf)
        self.start_epsilon = 10
        self.solution = None

    def find(self, grid_map, start_i, start_j, goal_i, goal_j):
        OPEN = Open()
        INCONS = []

        startNode = Node(start_i, start_j,
                         h=self.start_epsilon * self.heuristic_function(start_i, start_j, goal_i, goal_j))

        OPEN.add_node(startNode)
        OPEN, INCONS, goalNode = self.improve_path(OPEN, INCONS, grid_map, self.start_epsilon, goal_i, goal_j)

        if goalNode is not None:
            epsilon = min(self.start_epsilon, goalNode.g / min(self.get_min_sum_gh(OPEN), self.get_min_sum_gh(INCONS)))
            self.publish_solution(goalNode, epsilon)
        else:
            return False, None, inf

        while epsilon > 1:
            epsilon = (epsilon + 1) / 2
            for node in INCONS:
                OPEN.add_node(node)
            OPEN.add_node(Node(start_i, start_j,
                                h=epsilon * self.heuristic_function(start_i, start_j, goal_i, goal_j)))

            OPEN, INCONS, goalNode = self.improve_path(OPEN, INCONS, grid_map, epsilon, goal_i, goal_j)
            epsilon = min(epsilon, goalNode.g / min(self.get_min_sum_gh(OPEN), self.get_min_sum_gh(INCONS)))
            self.publish_solution(goalNode, epsilon)

        return True, self.solution, self.w


    def improve_path(self, OPEN, INCONS, grid_map, epsilon, goal_i, goal_j):
        CLOSED = Closed()

        while not OPEN.is_empty():
            s = OPEN.get_best_node()
            if s.i == goal_i and s.j == goal_j:
                return OPEN, INCONS, s

            CLOSED.add_node(s)

            opt = [False]
            if not s.subopt:
                opt.append(True)

            for o in opt:
                for i, j, interval, t in grid_map.get_successors(s):
                    newNode = Node(i, j, g=t, interval=interval, subopt=not o, parent=s)
                    if CLOSED.was_expanded(newNode):
                        expandedNode = CLOSED.nodes[newNode.get_pos()]
                        if expandedNode.g > t:
                            expandedNode.parent = s
                            expandedNode.g = t
                            expandedNode.subopt = o
                            INCONS.append(expandedNode)
                            CLOSED.nodes[newNode.get_pos()] = expandedNode
                    else:
                        if o:
                            newNode.f = epsilon * (t + self.heuristic_function(i, j, goal_i, goal_j))
                        else:
                            newNode.f = t + epsilon * self.heuristic_function(i, j, goal_i, goal_j)

                        OPEN.add_node(newNode)

        return OPEN, INCONS, None

    def publish_solution(self, goalNode, epsilon):
        self.solution = goalNode
        self.w = epsilon

    def get_min_sum_gh(self, array):
        minSum = inf
        for node in array:
            minSum = min(minSum, node.g + node.h)
        return minSum
