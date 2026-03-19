
README – Path Planning & Graph Algorithms Assignment 3

Name:Anish Bandaru
Roll No:SE24UCSE007

--------------------------------------------------

OVERVIEW

This project contains implementations of three important algorithms related to path finding and graph traversal:

1. Dijkstra’s Algorithm – to find shortest distances between Indian cities
2. Grid-based Path Planning (A* Algorithm) – for navigating a robot in a grid with obstacles
3. Dynamic Grid Handling – ensuring a valid path exists using safe grid generation

The objective of this assignment is to understand how shortest path algorithms work in both real-world map data and simulated environments.

--------------------------------------------------

1. DIJKSTRA’S ALGORITHM (Cities Dataset)

In this section, a graph of Indian cities is created using a CSV file.

Each city acts as a node, and the distances between cities represent weighted edges.

The algorithm computes the shortest distance from a selected starting city to every other city in the dataset.

Key Idea:
Dijkstra’s algorithm always expands the node with the smallest known distance using a priority queue. This guarantees that the final distances calculated are the minimum possible travel distances.

--------------------------------------------------

2. GRID-BASED PATH PLANNING (A* Algorithm)

In this part, we simulate robot navigation using a grid.

• A 70 × 70 grid represents a battlefield or environment.
• Each cell can be:
  - Free space (0)
  - Obstacle (1)

The robot must travel from the start location (top-left corner) to the goal location (bottom-right corner).

Why A*?
The A* algorithm improves search efficiency by using a heuristic function (Manhattan distance) to estimate the remaining distance to the goal. This helps guide the search toward the destination faster than basic algorithms like BFS.

--------------------------------------------------

3. SAFE GRID GENERATION (Improvement)

Random obstacle placement can sometimes block all possible paths between the start and goal.

To avoid this situation:

• A grid is generated randomly.
• The algorithm checks if a valid path exists.
• If no path exists, the grid is discarded.
• A new grid is generated until a valid path is found.

This guarantees that the program always produces a valid result during execution.

--------------------------------------------------

VISUALIZATION

The grid environment is displayed using matplotlib for better understanding.

Color scheme used:

White → Free space
Black → Obstacles
Red → Shortest path
Green → Start position
Blue → Goal position

This visualization makes the algorithm’s behavior easy to interpret and suitable for screenshots in reports.

--------------------------------------------------

HOW TO RUN THE PROGRAM

Step 1: Install Python (Python 3 recommended)

Step 2: Install required libraries

pip install matplotlib numpy

Step 3: Run the Python program

python filename.py

Replace "filename.py" with the actual name of the Python file.

--------------------------------------------------

EXPLANATION OF OUTPUTS

1. DIJKSTRA’S ALGORITHM OUTPUT

The output lists the shortest distance from the selected starting city to every other city in the dataset.

Each line shows:

City → Distance (km)

Example:

Delhi → 0 km
Mumbai → 1415 km
Jaipur → 281 km

This means the shortest route from the starting city to Mumbai is 1415 km.

This confirms that the algorithm correctly finds minimum cost paths in a weighted graph.

--------------------------------------------------

2. GRID PATH PLANNING OUTPUT (A*)

The output contains:

• A message indicating that a path was found
• The number of steps required to reach the goal
• A visual grid plot

In the visualization:

White cells represent free space
Black cells represent obstacles
Red cells show the shortest path found
Green marks the starting point
Blue marks the goal

The red path shows how the robot navigates around obstacles to reach the goal.

--------------------------------------------------

3. SAFE GRID GENERATION OUTPUT

This feature guarantees that the program always runs on a valid environment.

If a randomly generated grid blocks all possible routes:

• That grid is discarded
• A new grid is generated
• The process continues until a valid path exists

Final result:
The program always displays a valid path and its length.

--------------------------------------------------

OVERALL UNDERSTANDING

This project demonstrates:

Dijkstra → shortest distances in a city network
A* → shortest path planning in a grid environment
Safe grid generation → ensures valid test environments

Together these algorithms demonstrate how graph-based methods solve navigation problems.

--------------------------------------------------

CONCLUSION

This project shows how shortest path algorithms can be applied in real-world applications such as:

• GPS navigation systems
• Autonomous robots
• Game AI pathfinding
• Battlefield route planning

Efficient algorithms like Dijkstra and A* are essential for solving large-scale navigation problems.

--------------------------------------------------

FINAL NOTE

The code is written in a clear and simple manner to focus on understanding the concepts and practical implementation of shortest path algorithms.
