import networkx as nx
import matplotlib.pyplot as plt
#Tasmania has no neighbouring state so it wont show in graph but its colour is shown in output1

states = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'QLD'],
    'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['QLD', 'SA', 'VIC'],
    'VIC': ['SA', 'NSW'],
    'TAS': []
}

colors = ['red', 'green', 'blue']
def is_valid(state, color, assignment):
    for n in neighbors[state]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(states):
        return assignment

    for s in states:
        if s not in assignment:

            for color in colors:
                if is_valid(s, color, assignment):
                    assignment[s] = color

                    result = solve(assignment)
                    if result:
                        return result

                    del assignment[s]

            return None


solution = solve({})

print("Solution:", solution)


G = nx.Graph()

for s in neighbors:
    for n in neighbors[s]:
        G.add_edge(s, n)


node_colors = [solution[node] for node in G.nodes()]

plt.figure(figsize=(6,6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=10,
    font_weight='bold'
)
plt.title("australia map coloring")
plt.savefig("australia_graph.png")
plt.show()