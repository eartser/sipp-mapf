from entity.Task import Task
from entity.Map import Map
from entity.SafeInterval import SafeInterval

TRAVERSABLE_TERRAIN = '.G'
NOT_TRAVERSABLE_TERRAIN = '@OT'


def read_map_from_movingai_file(path):
    with open(path) as f:
        f.readline()
        h = int(f.readline().split()[1])
        w = int(f.readline().split()[1])
        f.readline()
        safe_intervals = [[[] for _ in range(w)] for _ in range(h)]
        for i in range(h):
            line = f.readline()
            for j in range(w):
                if line[j] in TRAVERSABLE_TERRAIN:
                    safe_intervals[i][j].append(SafeInterval())
                elif line[j] in NOT_TRAVERSABLE_TERRAIN:
                    continue
                else:
                    raise ValueError(f"Error while parsing a map from MovingAI file: unexpected symbol '{line[j]}' "
                                     f"occurred.")

    grid_map = Map()
    grid_map.set_map_properties(w, h, safe_intervals)
    return grid_map


def read_tasks_from_movingai_file(path):
    tasks = []

    with open(path) as f:
        f.readline()
        for line in f:
            types = (int, str, int, int, int, int, int, int, float)
            task = Task(*[type(item) for type, item in zip(types, line.split())])
            tasks.append(task)

    return tasks
