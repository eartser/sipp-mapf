# Prioritized Multi-Agent Path Finding (MAPF) using Safe Interval Path Planning (SIPP) and modifications

## Description
Multi-Agent Path Finding (MAPF) problem is a common problem in different areas (e.g. automated storages, unmanned vehicles etc). One way to solve it is Prioritezed MAPF algorithms. 
The main principle of those algorithms is to add agents one by one according to their priority. In the lowest level of these algorithms we need to solve path planning problem in
environment with dynamic obstacles.

Safe Interval Path Planning (SIPP) solves such problem. The greatest advantage of this algorithm is the time complexity as it is not dependend on the time horizon. 

In this work we implemented SIPP algorithm and its modifications and compared their perfomance to baseline algorithm: A* with timestamps (it's exactly an A* where timestamp is
one more parameter of the state).

SIPP modifications that we implemented:
- Bounded suboptimal SIPP:
    - Weighted SIPP with duplicate states
    - Weighted SIPP with Re-expansions
    - Focal SIPP
- Anytime SIPP

To learn more abot the algorithms view articles in [References](#references) section.

## Installation and guidance

First, you need to clone the repository:
```bash
git clone https://github.com/eartser/sipp-mapf/
```

After that to run the tests on the map given a number of agents you can use script:
```bash
python3 main.py [map_filename] [scen_filename] [agents_n] [algorithm]
```

It has some optional arguments that you can use:
```
--weight WEIGHT       floating point to use in suboptimal algorithms
--tasks_n TASKS_N     number of random tasks to generate and run
--time_limit TIME_LIMIT
                      time limit for a single task in seconds
--gif_filename GIF_FILENAME
                      path to save a .gif file representing one of the tasks in motion
```

Use the following command for detailed information on arguments:
```
python3 main.py --help
```

Brief example:
```
python3 main.py data/arena.map data/arena.map.scen 50 wdsipp --tasks_n 5 --weight 1.25 --gif_filename arena
```
will print out some statistic of path planning including success rate, mean makespan and mean flowtime:
```
number of agents: 50, success rate: 1.0, mean makespan: 71.2, mean flowtime: 34.58
```
and save arena.gif file with the planned agents' paths in motion, similar to the one below.

![](https://github.com/eartser/sipp-mapf/blob/master/gifs/arena.gif)


## References
[1] Phillips, M. and Likhachev, M., 2011, May. [SIPP: Safe interval path planning for dynamic environments.](http://www.cs.cmu.edu/~maxim/files/sipp_icra11.pdf)

[2] Venkatraman, N., Phillips, M. and Likhachev, M., 2012, Oct., [Anytime Safe Interval Path Planning for dynamic environments.](https://ieeexplore.ieee.org/document/6386191/)

[3] Yakovlev, K., Andreychuk, A. and Stern, R., 2020, Jun., [Revisiting Bounded-Suboptimal Safe Interval Path Planning.](https://arxiv.org/abs/2006.01195)

