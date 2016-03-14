import os
import json
from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import json_graph
import networkx as nx
g=nx.DiGraph()

print "Stats on the full graph"
print nx.info(g)

# Create a subgraph from a collection of nodes. In this case, the
# collection is all of the users in the original interest graph
mtsw_users = [n for n in g if g.node[n]['type'] == 'user']
h = g.subgraph(mtsw_users)
print "Stats on the extracted subgraph"
print nx.info(h)
# Visualize the social network of all people from the original interest graph.
d = json_graph.node_link_data(h)
json.dump(d, open('/home/astha/Desktop/3rdSem/DMw/dm/resources.json', 'w'))
# IPython Notebook can serve files and display them into
# inline frames. Prepend the path with the 'files' prefix.
# A D3 template for displaying the graph data.
viz_file = '/home/astha/Desktop/3rdSem/DMw/dm/force.html'
# Display the D3 visualization.
display(IFrame(viz_file, '100%', '600px'))
