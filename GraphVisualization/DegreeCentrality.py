from operator import itemgetter
import networkx as nx
from IPython.display import HTML
from IPython.core.display import display
display(HTML('<img src="files/resources/ch07-github/kite-graph.png" width="400px">'))
# The classic Krackhardt kite graph
kkg = nx.generators.small.krackhardt_kite_graph()
print "Degree Centrality"
print sorted(nx.degree_centrality(kkg).items(),
key=itemgetter(1), reverse=True)

print
print "Betweenness Centrality"
print sorted(nx.betweenness_centrality(kkg).items(),
key=itemgetter(1), reverse=True)
print
print "Closeness Centrality"
print sorted(nx.closeness_centrality(kkg).items(),
key=itemgetter(1), reverse=True)
