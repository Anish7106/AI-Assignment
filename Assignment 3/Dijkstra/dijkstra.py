import csv
import heapq


def load_graph(filename):
    graph = {}

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            src = row["Source"].strip()
            dest = row["Destination"].strip()
            dist = int(row["Distance"])

            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []

            # Undirected graph
            graph[src].append((dest, dist))
            graph[dest].append((src, dist))

    return graph


def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {city: float("inf") for city in graph}
    dist[start] = 0

    while pq:
        current_dist, current_city = heapq.heappop(pq)

        # Skip outdated queue entries
        if current_dist > dist[current_city]:
            continue

        for neighbor, weight in graph[current_city]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


if __name__ == "__main__":
    filename = "cities.csv"
    graph = load_graph(filename)

    start_city = input("Enter starting city: ").strip()

    if start_city not in graph:
        print("City not found in dataset!")
    else:
        result = dijkstra(graph, start_city)

        print(f"\nShortest Road Distances from {start_city}")
        print("-" * 40)

        sorted_results = sorted(result.items(), key=lambda x: x[1])

        for i, (city, distance) in enumerate(sorted_results, start=1):
            print(f"{i:2}. {city:<20} {distance:>5} km")
