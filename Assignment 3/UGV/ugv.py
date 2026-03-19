import random
import heapq
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

size = 70
block_chance = 0.18

start = (0, 0)
end = (size - 1, size - 1)


def get_shortest_path(grid, start, end):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows = len(grid)
    cols = len(grid[0])

    queue = []
    heapq.heappush(queue, (0, start))

    came_from = {}
    cost = {start: 0}

    while queue:
        current = heapq.heappop(queue)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()
            return path

        x, y = current

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            next_cell = (nx, ny)

            if not (0 <= nx < rows and 0 <= ny < cols):
                continue

            if grid[nx][ny] == 1:
                continue

            new_cost = cost[current] + 1

            if next_cell not in cost or new_cost < cost[next_cell]:
                cost[next_cell] = new_cost
                priority = new_cost + distance(next_cell, end)
                heapq.heappush(queue, (priority, next_cell))
                came_from[next_cell] = current

    return None


def generate_grid():
    while True:
        grid = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                if random.random() < block_chance:
                    grid[i][j] = 1

        grid[start[0]][start[1]] = 0
        grid[end[0]][end[1]] = 0

        path = get_shortest_path(grid, start, end)

        if path:
            return grid, path


grid_map, path = generate_grid()

print("Path found!")
print("Number of cells in path:", len(path))
print("Number of steps needed:", len(path) - 1)

display = np.array(grid_map)

for r, c in path:
    display[r][c] = 2

cmap = ListedColormap(['white', 'black', 'red'])

plt.figure(figsize=(10, 10), dpi=150)
plt.imshow(display, cmap=cmap, interpolation='nearest')

ys = [c for r, c in path]
xs = [r for r, c in path]
plt.plot(ys, xs, color='red', linewidth=2)

plt.scatter(start[1], start[0], color='green', s=80, label='Start')
plt.scatter(end[1], end[0], color='blue', s=80, label='Goal')

plt.grid(color='gray', linestyle='-', linewidth=0.2)
plt.title("A* Path Planning in 70x70 Grid")
plt.legend()
plt.show()