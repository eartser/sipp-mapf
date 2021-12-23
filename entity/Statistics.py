from dataclasses import dataclass


@dataclass
class Statistics:
    success_count = {}
    runs_count = {}
    sum_makespan = {}
    sum_flowtime = {}

    def add_stat(self, cnt_agents, success, makespan, flowtime):
        if cnt_agents not in self.runs_count:
            self.runs_count[cnt_agents] = 0
            self.success_count[cnt_agents] = 0
            self.sum_flowtime[cnt_agents] = 0
            self.sum_makespan[cnt_agents] = 0

        self.runs_count[cnt_agents] += 1
        if success:
            self.success_count[cnt_agents] += 1
            self.sum_makespan[cnt_agents] += makespan
            self.sum_flowtime[cnt_agents] += flowtime

    def __str__(self):
        s = ""
        for key, value in self.runs_count.items():
            s += f'number of agents: {key}, success rate: {self.success_count[key] / value}'
            if self.success_count[key] != 0:
                s += f', mean makespan: {self.sum_makespan[key] / self.success_count[key]}, '
                s += f'mean flowtime: {self.sum_flowtime[key] / self.success_count[key]}\n'
        return s

    def __repr__(self):
        return str(self)

