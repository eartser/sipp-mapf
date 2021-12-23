import signal
from contextlib import contextmanager


class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class MAPF:
    def __init__(self, agents, grid_map, search_function, time_bound=10):
        self.grid_map = grid_map
        self.agents = sorted(agents)
        self.search_function = search_function
        self.time_bound = time_bound
        self.makespan = 0
        self.flowtime = 0
        self.success = False
        self.paths = []

    def find_solution(self):
        try:
            with time_limit(self.time_bound):
                self._find_solution()
        finally:
            return self.success, self.paths, self.makespan, self.flowtime

    def publish_solution(self, success, paths):
        self.success = success
        self.paths = paths

    def _find_solution(self):
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
                self.publish_solution(False, [])
                return

            path, length = self.search_function.make_path(goal_node)
            self.makespan = max(self.makespan, length)
            self.flowtime += length

            self.grid_map.apply_dynamic_obstacles([path])
            agent_paths.append(path)

        self.publish_solution(True, agent_paths)
        return
