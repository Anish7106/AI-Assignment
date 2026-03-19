#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
import random
import time
import math
import copy

GRID_ROWS = 70
GRID_COLS = 70
FREE = 0
BLOCKED = 1
SENSOR_RANGE = 5
OBSTACLE_CHANCE = 0.0005   # probability per cell per step

def calc_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

MOVES = [
    (-1, 0, 1.0), (1, 0, 1.0),
    (0, -1, 1.0), (0, 1, 1.0),
    (-1, -1, 1.414), (-1, 1, 1.414),
    (1, -1, 1.414), (1, 1, 1.414)
]

def neighbours(r, c):
    nbs = []
    for dr, dc, cost in MOVES:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < GRID_ROWS and 0 <= nc < GRID_COLS:
            nbs.append((nr, nc, cost))

    return nbs

def find_path(grid, start, goal):
    g_scores = {start: 0.0}
    pq = [(calc_dist(start, goal), 0.0, start)]
    came_from = {}
    visited_nodes = set()

    while pq:
        f, g, current = heapq.heappop(pq)

        if current in visited_nodes:
            continue
        visited_nodes.add(current)

        if current == goal:
            path = []
            cur = goal

            while cur != start:
                path.append(cur)
                cur = came_from.get(cur)
                if cur is None:
                    return []

            path.append(start)
            path.reverse()
            return path

        for nr, nc, move_cost in neighbours(current[0], current[1]):
            nb = (nr, nc)

            if grid[nr][nc] == BLOCKED:
                continue

            # prevent corner cutting for diagonal movement
            if abs(nr - current[0]) == 1 and abs(nc - current[1]) == 1:
                if grid[current[0]][nc] == BLOCKED or grid[nr][current[1]] == BLOCKED:
                    continue

            tentative_g = g + move_cost

            if tentative_g < g_scores.get(nb, float("inf")):
                g_scores[nb] = tentative_g
                came_from[nb] = current
                h = calc_dist(nb, goal)
                heapq.heappush(pq, (tentative_g + h, tentative_g, nb))

    return []

class UGV:
    def __init__(self, real_map, start, goal, sensor_range=SENSOR_RANGE, seed=99):
        self.real_map = real_map
        self.start = start
        self.goal = goal
        self.pos = start
        self.sensor_range = sensor_range
        self.known = [[FREE] * GRID_COLS for _ in range(GRID_ROWS)]
        self.known[goal[0]][goal[1]] = FREE
        self.path = []
        self.history = [start]
        self.steps = 0
        self.replans = 0
        self.dist = 0.0
        random.seed(seed)

    def scan(self):
        r, c = self.pos
        found_problem = False
        path_cells = set(self.path)

        for rr in range(max(0, r - self.sensor_range), min(GRID_ROWS, r + self.sensor_range + 1)):
            for cc in range(max(0, c - self.sensor_range), min(GRID_COLS, c + self.sensor_range + 1)):
                if calc_dist((r, c), (rr, cc)) <= self.sensor_range:
                    if self.real_map[rr][cc] == BLOCKED and self.known[rr][cc] == FREE:
                        self.known[rr][cc] = BLOCKED
                        if (rr, cc) in path_cells:
                            found_problem = True

        return found_problem

    def add_random_obstacles(self):
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                cell = (r, c)

                if cell == self.start or cell == self.goal or cell == self.pos:
                    continue

                if self.real_map[r][c] == FREE:
                    if random.random() < OBSTACLE_CHANCE:
                        self.real_map[r][c] = BLOCKED

    def step_forward(self):
        if len(self.path) < 2:
            return None

        nxt = self.path[1]

        # real-world safety check
        if self.real_map[nxt[0]][nxt[1]] == BLOCKED:
            self.known[nxt[0]][nxt[1]] = BLOCKED
            return self.pos

        step_cost = calc_dist(self.pos, nxt)

        self.dist += step_cost
        self.pos = nxt
        self.path = self.path[1:]
        self.history.append(nxt)
        self.steps += 1

        return nxt

    def run(self, max_steps=5000):
        print(f"Starting UGV from {self.start} -> {self.goal}")
        print(f"(sensor={self.sensor_range}, obstacle chance={OBSTACLE_CHANCE})")

        self.path = find_path(self.known, self.pos, self.goal)

        if not self.path:
            print("No path found at start")
            return False

        t0 = time.perf_counter()

        for i in range(max_steps):
            blocked = self.scan()

            if blocked:
                self.replans += 1
                self.path = find_path(self.known, self.pos, self.goal)
                if not self.path:
                    print(f"Stopped at step {i}, no path anymore")
                    break

            new_pos = self.step_forward()

            if new_pos is None:
                print("Ran out of path")
                break

            if new_pos == self.pos and self.pos != self.goal:
                self.replans += 1
                self.path = find_path(self.known, self.pos, self.goal)
                if not self.path:
                    print("No path possible after new obstacle")
                    break

            if self.pos == self.goal:
                elapsed = (time.perf_counter() - t0) * 1000
                print("Reached goal")
                self.report(elapsed, True)
                return True

            self.add_random_obstacles()

        elapsed = (time.perf_counter() - t0) * 1000
        print("Timeout or failed")
        self.report(elapsed, False)
        return False

    def report(self, elapsed, success):
        straight = calc_dist(self.start, self.goal)
        efficiency = (straight / self.dist * 100) if self.dist > 0 else 0
        known_obs = sum(self.known[r][c] for r in range(GRID_ROWS) for c in range(GRID_COLS))

        print("Result:", "Success" if success else "Fail")
        print("Steps:", self.steps)
        print("Distance:", round(self.dist, 2))
        print("Efficiency:", round(efficiency, 1), "%")
        print("Replans:", self.replans)
        print("Known Obstacles:", known_obs)
        print("Time (ms):", round(elapsed, 2))

if __name__ == "__main__":
    print("=" * 50)
    print("UGV simulation (dynamic obstacles)")
    print("=" * 50)

    random.seed(42)

    while True:
        base_map = []
        for _ in range(GRID_ROWS):
            row = []
            for _ in range(GRID_COLS):
                if random.random() < 0.2:
                    row.append(BLOCKED)
                else:
                    row.append(FREE)
            base_map.append(row)

        start = (2, 2)
        goal = (67, 67)

        base_map[start[0]][start[1]] = FREE
        base_map[goal[0]][goal[1]] = FREE

        # ensure at least one path exists initially
        if find_path(base_map, start, goal):
            break

    robot = UGV(copy.deepcopy(base_map), start, goal)
    robot.run()