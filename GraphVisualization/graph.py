import networkx as nx
g=nx.DiGraph()
g.add_edge('X','Y')
print nx.info(g)
print "Nodes :",g.nodes()
print "Edges :",g.edges()

print "X props:", g.node['X']
print "Y props:", g.node['Y']

# Get edge properties

print "X=>Y props:", g['X']['Y']
print

# Update a node property

g.node['X'].update({'prop1' : 'value1'})
print "X props:", g.node['X']
print

# Update an edge property

g['X']['Y'].update({'label' : 'label1'})
print "X=>Y props:", g['X']['Y']

g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)

for sg in stargazers:
    g.add_node(sg.login + '(user)', type='user')
    g.add_edge(sg.login + '(user)', repo.name + '(repo)', type='gazes')
