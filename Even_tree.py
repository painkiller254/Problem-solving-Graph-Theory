'''You are given a tree (a simple connected graph with no cycles).

Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.

As an example, the following tree with  nodes can be cut at most  time to create an even forest.

Function Description

Complete the evenForest function in the editor below. It should return an integer as described.

evenForest has the following parameter(s):

t_nodes: the number of nodes in the tree
t_edges: the number of undirected edges in the tree
t_from: start nodes for each edge
t_to: end nodes for each edge, (Match by index to t_from.)'''

class Graph:
    def __init__(self, n, t_from, t_to):
        self.n_nodes = n
        self.adj_list = {i:set() for i in range(n)}
        for w, v in zip(t_from, t_to):
            self.adj_list[w-1].add(v-1)
            self.adj_list[v-1].add(w-1)
        self.out = 0
        
    def dfs(self, v, p):
        s = (1 + sum(self.dfs(w, v) for w in self.adj_list[v] if w != p)) % 2
        self.out += not s
        return s
    

def evenForest(t_nodes, t_edges, t_from, t_to):
    g = Graph(t_nodes, t_from, t_to)
    g.dfs(0, 0)
    return g.out-1