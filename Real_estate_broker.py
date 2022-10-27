'''You are a real estate broker in ancient Knossos. You have  unsold houses, and each house  has an area, , and a minimum price, . You also have  clients, and each client  wants a house with an area greater than  and a price less than or equal to .

Each client can buy at most one house, and each house can have at most one owner. What is the maximum number of houses you can sell?'''

class GFG:
    def __init__(self, graph):
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
        
    def bpm(self, u, matchR, seen):
        for v in range(self.jobs):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
    
    def maxBPM(self):
        matchR = [-1] * self.jobs
        result = 0
        for i in range(self.ppl):
            seen = [False] * self.jobs
            if self.bpm(i, matchR, seen):
                result += 1
        return result
                    

def realEstateBroker(clients, houses):
    #
    # Write your code here.
    #
    
    m, n = len(clients), len(houses)
    bpGraph = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if houses[j][0] >= clients[i][0] and houses[j][1] <= clients[i][1]:
                bpGraph[i][j] = 1
    g = GFG(bpGraph)
    return g.maxBPM()
            