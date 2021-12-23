import random

from util.draw import Draw
from multiagent.MAPF import MAPF
from entity.Map import Map, TimestampSearchMap
from entity.Task import Task
from search_functions.AStar import AStar
from util.movingai_parser import *
from random import choices
from entity.Agent import Agent
from tqdm import tqdm


def run_scens(map_filename, scen_filename, cnt_agents, search_function, stats, cnt_runs=10, draw_path=None, mapf_tl=10):
    random.seed(243)
    grid_map = read_map_from_movingai_file(map_filename)
    if isinstance(search_function, AStar):
        grid_map = TimestampSearchMap(grid_map)

    tasks = read_tasks_from_movingai_file(scen_filename)

    for _ in tqdm(range(cnt_runs)):
        agents = list(map(lambda x: Agent(x[1].start_y, x[1].start_x, x[1].goal_y, x[1].goal_x, x[0]),
                          enumerate(choices(tasks, k=cnt_agents))))
        res, paths, makespan, flowtime = MAPF(agents, grid_map, search_function, time_bound=mapf_tl).find_solution()
        stats.add_stat(cnt_agents, res, makespan, flowtime)
        if res and draw_path is not None:
            Draw(grid_map, paths, [], filename=draw_path)
            draw_path = None


