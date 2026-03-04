"""
Missionaries & Cannibals (3,3)
Implement: BFS, UCS, DFS, DLS, IDDFS (uninformed search)

State = (M_left, C_left, boat)
boat: 0 = left bank, 1 = right bank
"""

from collections import deque
import heapq

start = (3, 3, 0)
goal  = (0, 0, 1)

# Safety check for states
def safe(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True

# Successor function
def next_moves(state):
    m_left, c_left, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    children = []

    for m, c in moves:
        if m + c == 0:
            continue

        if boat == 0:  
            new_state = (m_left - m, c_left - c, 1)
        else:          
            new_state = (m_left + m, c_left + c, 0)

        if safe(new_state):
            children.append(new_state)

    return children

# BFS
def bfs():
    q = deque([(start, [])])   
    visited = set()

    while q:
        current, path = q.popleft()

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for child in next_moves(current):
                q.append((child, path + [current]))

# Uniform Cost Search (UCS)
def ucs():
    heap = []
    heapq.heappush(heap, (0, start, [])) 
    best_cost = {start: 0}

    while heap:
        cost, current, path = heapq.heappop(heap)

        # ignore outdated heap entries
        if cost != best_cost.get(current, float("inf")):
            continue

        if current == goal:
            return path + [current]

        for child in next_moves(current):
            new_cost = cost + 1
            if new_cost < best_cost.get(child, float("inf")):
                best_cost[child] = new_cost
                heapq.heappush(heap, (new_cost, child, path + [current]))

# DFS
def dfs():
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for child in next_moves(current):
                stack.append((child, path + [current]))

# Depth Limited Search (DLS)
def dls(current, limit, path, visited):
    if current == goal:
        return path + [current]

    if limit == 0:
        return None

    visited.add(current)

    for child in next_moves(current):
        if child not in visited:
            result = dls(child, limit - 1, path + [current], visited)
            if result is not None:
                return result

    visited.remove(current)
    return None

# Iterative Deepening DFS (IDDFS)
def iddfs(max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, depth, [], set())
        if result is not None:
            return result

print("BFS solution:")
print(bfs())

print("\nUniform Cost Search solution:")
print(ucs())

print("\nDFS solution:")
print(dfs())

print("\nDepth Limited Search where limit is 12:")
print(dls(start, 12, [], set()))

print("\nIterative Deepening DFS where max depth is 12:")
print(iddfs(12))
