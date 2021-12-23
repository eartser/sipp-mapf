class Statistics:

    def __init__(self):
        self.success_count = {}
        self.runs_count = {}
        self.sum_makespan = {}
        self.sum_flowtime = {}

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

    def success_rate(self, agents_number):
        return self.success_count[agents_number] / self.runs_count[agents_number]

    def makespan(self, agents_number):
        return self.sum_makespan[agents_number] / self.success_count[agents_number]

    def flowtime(self, agents_number):
        return self.sum_flowtime[agents_number] / self.success_count[agents_number]

    def __str__(self):
        s = ""
        for key, value in self.runs_count.items():
            s += f'number of agents: {key}, success rate: {self.success_count[key] / value}'
            if self.success_count[key] != 0:
                s += f', mean makespan: {self.sum_makespan[key] / self.success_count[key]}, '
                s += f'mean flowtime: {self.sum_flowtime[key] / self.success_count[key]}'
            s += '\n'
        return s

    def __repr__(self):
        return str(self)

