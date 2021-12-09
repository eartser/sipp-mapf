from dataclasses import dataclass


@dataclass
class Task:
    bucket: int
    map: str
    map_width: int
    map_height: int
    start_x: int
    start_y: int
    goal_x: int
    goal_y: int
    optimal_length: float
