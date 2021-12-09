from dataclasses import dataclass
import numpy as np


@dataclass
class Statistics:
    map: str
    correctness: [int]
    path_length: [float]
    optimal_length: [float]
    nodes_created: [int]
    nodes_expanded: [int]

    def add_stat(self, correctness=0, path_length=0, optimal_length=1, nodes_created=0, nodes_expanded=0):
        self.correctness.append(correctness)
        self.path_length.append(path_length)
        self.optimal_length.append(optimal_length)
        self.nodes_created.append(nodes_created)
        self.nodes_expanded.append(nodes_expanded)

    def correctness_rate(self):
        return np.mean(self.correctness)

    def length_ratio(self):
        ratio = np.array(self.path_length) / np.array(self.optimal_length)
        return ratio.tolist()

    # TODO: Additional statistic functions
