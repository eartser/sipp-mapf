class MAPF:
    def __init__(self, agents, grid_map, search_function):
        self.grid_map = grid_map
        self.agents = sorted(agents)
        self.search_function = search_function
        self.makespan = 0
        self.flowtime = 0

    def find_solution(self):
        agent_paths = []
        for agent in self.agents:
            res, goal_node = self.search_function.find(
                self.grid_map,
                agent.start_i,
                agent.start_j,
                agent.goal_i,
                agent.goal_j
            )
            if not res:
                return False, []

            path, length = self.search_function.make_path(goal_node)
            self.makespan = max(self.makespan, length)
            self.flowtime += length

            self.grid_map.apply_dynamic_obstacles([path])
            agent_paths.append(path)

        return True, agent_paths
