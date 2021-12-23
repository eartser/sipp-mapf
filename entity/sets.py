import heapq
from entity.Node import Node


class Open:

    def __init__(self):
        self.data = []
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes.values())

    def is_empty(self):
        return len(self) == 0

    def add_node(self, node: Node, *args):
        pos = node.get_pos()
        if pos in self.nodes:
            cur_node = self.nodes[pos]
            if cur_node.g <= node.g:
                return
        self.nodes[pos] = node
        heapq.heappush(self.data, node)

    def get_best_node(self, *args):
        while True:
            best = self.data[0]
            heapq.heappop(self.data)
            if best.get_pos() in self.nodes:
                break
        del self.nodes[best.get_pos()]
        return best


class Closed:

    def __init__(self):
        self.nodes = {}

    def __iter__(self):
        return iter(self.nodes.values())

    def __len__(self):
        return len(self.nodes)

    def add_node(self, item: Node):
        self.nodes[item.get_pos()] = item

    def was_expanded(self, item: Node):
        return item.get_pos() in self.nodes


class OpenAndClosed:

    def __init__(self):
        self.data = []
        self.nodes = {}
        self.exp = {}
        self.reexp = {}
        self.reexp_cnt = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def __len__(self):
        return len(self.nodes)

    def is_empty(self):
        return len(self.data) == 0

    def expand(self, node):
        pos = node.get_pos()
        if pos in self.exp:
            self.reexp_cnt += 1
            self.reexp[pos] = node
        self.exp[pos] = node

    def add_node(self, node):
        pos = node.get_pos()
        if pos in self.nodes:
            cur_node = self.nodes[pos]
            if cur_node.g <= node.g:
                return
            if cur_node in self.data:
                self.data.remove(cur_node)
        self.nodes[pos] = node
        if pos in self.exp:
            self.exp[pos] = node
        if pos in self.reexp:
            self.reexp[pos] = node
        heapq.heappush(self.data, node)

    def get_best_node(self):
        best = self.data[0]
        heapq.heappop(self.data)
        self.expand(best)
        return best

    def get_node(self, node):
        if node in self.data:
            ind = self.data.index(node)
            self.data[ind] = self.data[-1]
            self.data.pop()
            if ind < len(self.data):
                heapq._siftup(self.data, ind)
                heapq._siftdown(self.data, 0, ind)
        self.expand(node)
        return node

    @property
    def expanded(self):
        return self.exp.values()

    @property
    def reexpanded(self):
        return self.reexp.values()

    @property
    def number_of_reexpansions(self):
        return self.reexp_cnt

    @property
    def best_f_value(self):
        return self.data[0].f


class Focal:

    def __init__(self, heuristic_func, goal_i, goal_j):
        self.heuristic_func = heuristic_func
        self.goal_i = goal_i
        self.goal_j = goal_j
        self.data = []
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes.values())

    def is_empty(self):
        return len(self) == 0

    def add_node(self, node: Node):
        pos = node.get_pos()
        if pos in self.nodes:
            cur_node = self.nodes[pos]
            if cur_node.g <= node.g:
                return
        self.nodes[pos] = node
        heapq.heappush(self.data, (self.heuristic_func(node.i, node.j, self.goal_i, self.goal_j), node))

    def get_best_node(self):
        while True:
            best = self.data[0]
            heapq.heappop(self.data)
            if best[1].get_pos() in self.nodes:
                break
        del self.nodes[best[1].get_pos()]
        return best[1]
