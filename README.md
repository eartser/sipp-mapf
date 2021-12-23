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

To learn more abot the algorithms view articles in References section.

## Installation

First, you need to clone the repository:
```bash
git clone https://github.com/eartser/sipp-mapf/
```

After that to run the tests on the map given a number of agents you can use script:
```bash
python3 main.py 
```


It has some arguments that you can use:
```bash
  -h, --help            show this help message and exit
  
```

## References
[1] Phillips, M. and Likhachev, M., 2011, May. SIPP: Safe interval path planning for dynamic environments.
[**Link**](http://www.cs.cmu.edu/~maxim/files/sipp_icra11.pdf).

[2] Venkatraman, N., Phillips, M. and Likhachev, M., 2012, Oct., Anytime Safe Interval Path Planning for dynamic environments.
[**Link**](https://ieeexplore.ieee.org/document/6386191/).

[3] Yakovlev, K., Andreychuk, A. and Stern, R., 2020, Jun., Revisiting Bounded-Suboptimal Safe Interval Path Planning.
[**Link**](https://arxiv.org/abs/2006.01195).

