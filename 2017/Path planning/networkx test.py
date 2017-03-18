# Import networkx and initialize the graph.
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('D', 'C')
G.add_edge('D', 'B')

pos = nx.spring_layout(G)

nx.draw(G)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')


# Show the plot.
plt.show()
