'''Given an undirected weighted connected graph, find the Really Special SubTree in it. The Really Special SubTree is defined as a subgraph consisting of all the nodes in the graph and:

There is only one exclusive path from a node to every other node.
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
No cycles are formed
To create the Really Special SubTree, always pick the edge with smallest weight. Determine if including it will create a cycle. If so, ignore the edge. If there are edges of equal weight available:

Choose the edge that minimizes the sum  where  and  are vertices and  is the edge weight.
If there is still a collision, choose any of them.
Print the overall weight of the tree formed using the rules.

Function Description

Complete the  function in the editor below. It should return an integer that represents the total weight of the subtree formed.

kruskals has the following parameters:

g_nodes: an integer that represents the number of nodes in the tree
g_from: an array of integers that represent beginning edge node numbers
g_to: an array of integers that represent ending edge node numbers
g_weight: an array of integers that represent the weights of each edge'''

def find(a):
    ans=[]
    while par[a]>0:
        ans.append(a)
        a=par[a]

    for i in ans:
        par[i]=a
    return a

def union(a,b):
    par[a]+=par[b]
    par[b]=a


n,m=map(int,input().split())
l=[]
par={i:-1 for i in range(1,n+1)}
for i in range(m):
    a,b,c=map(int,input().split())
    l.append([a,b,c])
l.sort(key=lambda x:x[2])
s=0
for i in l:
    a,b,c=i
    x,y=find(a),find(b)
    if x!=y:
        union(x,y)
        s+=c
print(s)