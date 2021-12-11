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
