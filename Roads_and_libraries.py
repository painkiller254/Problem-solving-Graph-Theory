''' Determine the minimum cost to provide library access to all citizens of Hackerland. There are n cities numbered from 1 to n. Currently there are no libraries and the cities are not connected. Bidirectional roads may be built between any cuty pair listed in cities. A citizen has access to a library if:

Their city contains a library
They can travel by road from their city to a city containing a library

Function Description

Complete the function roadsAndLibraries in the editor below.
roadsAndLibraries has the following parameters:

int n: integer, the number of cities
int c_lib: integer, the cost to build a library
int c_road: integer, the cost to repair a road
int cities[m][2]: each  contains two integers that represent cities that can be connected by a new road
Returns
- int: the minimal cost'''

def roadsAndLibraries(n, c_lib, c_road, cities):
    import queue
    # Write your code here
    # if roads are expensive just buy libs
    if c_lib <= c_road:
        return c_lib * n
    
    # build an adjacency structure (dict of lists)
    m = {}
    for i in cities:
        if i[0] not in m:
            m[i[0]] = []
        if i[1] not in m:
            m[i[1]] = []
        m[i[0]].append(i[1])
        m[i[1]].append(i[0])
        
    seen = set()
    libs = 0
    roads = 0
    # loop through All possible cities
    for i in range(1, n+1):
        # if seen, skip
        if i in seen:
            continue
        libs += 1
        # if not in m, then ni roads possinle (so just buy the lib and continue)
        if i not in m:
            continue
        # put the first city of this group in the queue (and mark it seen)
        q = queue.Queue()
        q.put(i)
        seen.add(i)
        while not q.empty():
            x = q.get()
            # add all adjancent cities (if not yest seen) and mark them seen
            
            for j in m[x]:
                if j in seen:
                    continue
                seen.add(j)
                roads += 1
                q.put(j)
                
    return (libs*c_lib)+(roads*c_road)