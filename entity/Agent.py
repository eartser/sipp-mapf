class Agent:
    def __init__(self, start_i, start_j, goal_i, goal_j, priority):
        self.start_i = start_i
        self.start_j = start_j
        self.goal_i = goal_i
        self.goal_j = goal_j
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
